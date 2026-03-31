(() => {
  const dom = globalThis.CztNexusBridgeDom;
  const payloadUtils = globalThis.CztNexusBridgePayload;
  let pendingManualPayload = null;
  let protocolEnabledCache = true;
  let accountDownloadModeCache = "unknown";
  let accountDownloadModeSourceCache = "auto";
  let lastDownloadIntent = "none";
  let lastDownloadIntentAt = 0;
  const DOWNLOAD_INTENT_WINDOW_MS = 60000;

  chrome.storage.local
    .get({
      protocolStatus: true,
      accountDownloadMode: "unknown",
      accountDownloadModeSource: "auto",
      lastManualDownloadEvent: null
    })
    .then((obj) => {
      protocolEnabledCache = Boolean(obj.protocolStatus);
      accountDownloadModeCache = normalizeAccountDownloadMode(obj.accountDownloadMode);
      accountDownloadModeSourceCache = normalizeAccountDownloadModeSource(obj.accountDownloadModeSource);
      const last = obj.lastManualDownloadEvent;
      if (last && typeof last === "object") {
        pendingManualPayload = last;
        // Restore manual intent across page navigation if the cached event is still within the window and not yet consumed.
        const age = Date.now() - Number(last.timestamp || 0);
        if (!last.consumed && age <= DOWNLOAD_INTENT_WINDOW_MS) {
          lastDownloadIntent = "manual";
          lastDownloadIntentAt = Number(last.timestamp || 0);
        }
      }
    })
    .catch(() => {
      // Keep default enabled if storage is unavailable.
    });

  chrome.storage.onChanged.addListener((changes, area) => {
    if (area !== "local") {
      return;
    }
    if (changes.protocolStatus) {
      protocolEnabledCache = Boolean(changes.protocolStatus.newValue);
    }
    if (changes.accountDownloadMode) {
      accountDownloadModeCache = normalizeAccountDownloadMode(changes.accountDownloadMode.newValue);
    }
    if (changes.accountDownloadModeSource) {
      accountDownloadModeSourceCache = normalizeAccountDownloadModeSource(
        changes.accountDownloadModeSource.newValue
      );
    }
    if (changes.lastManualDownloadEvent) {
      const latest = changes.lastManualDownloadEvent.newValue;
      if (latest && typeof latest === "object") {
        pendingManualPayload = latest;
      } else {
        pendingManualPayload = null;
      }
    }
  });

  function normalizeAccountDownloadMode(value) {
    if (value === "direct" || value === "standard") {
      return value;
    }
    return "unknown";
  }

  function normalizeAccountDownloadModeSource(value) {
    if (value === "api") {
      return "api";
    }
    return "auto";
  }

  function cacheAccountDownloadMode(mode) {
    const normalized = normalizeAccountDownloadMode(mode);
    if (accountDownloadModeSourceCache === "api") {
      return;
    }
    if (normalized === "unknown" || normalized === accountDownloadModeCache) {
      return;
    }
    accountDownloadModeCache = normalized;
    chrome.storage.local.set({ accountDownloadMode: normalized });
  }

  function isDirectAccountTrigger(payload) {
    const p = payload || {};
    const nxmUrl = String(p.nxmUrl || "").toLowerCase();
    const href = String(p.href || "").toLowerCase();
    if (nxmUrl.startsWith("nxm://") || href.startsWith("nxm://")) {
      return true;
    }
    return Boolean(p.nxmKey || p.nxmExpires);
  }

  function isLikelyPremiumByUi(trigger, payload) {
    const label = dom.triggerLabelText(trigger);
    if (label.includes("premium")) {
      return true;
    }

    const p = payload || {};
    const href = String(p.href || "").toLowerCase();
    if (href.includes("premium")) {
      return true;
    }

    let current = trigger;
    while (current && current instanceof Element) {
      const className = String(current.className || "").toLowerCase();
      const id = String(current.id || "").toLowerCase();
      const dataTier = String(current.getAttribute("data-tier") || "").toLowerCase();
      if (className.includes("premium") || id.includes("premium") || dataTier === "premium") {
        return true;
      }
      current = current.parentElement;
    }

    return !dom.hasSlowDownloadOption(trigger);
  }

  function shouldLaunchOnManualClick(payload, trigger) {
    if (isDirectAccountTrigger(payload)) {
      cacheAccountDownloadMode("direct");
      return true;
    }
    if (accountDownloadModeCache === "unknown" && isLikelyPremiumByUi(trigger, payload)) {
      cacheAccountDownloadMode("direct");
      return true;
    }
    return accountDownloadModeCache === "direct";
  }

  function withAccountMode(payload, accountMode) {
    return {
      ...(payload || {}),
      accountMode: normalizeAccountDownloadMode(accountMode)
    };
  }

  function clearIntentAndMarkConsumed(payload) {
    lastDownloadIntent = "none";
    lastDownloadIntentAt = 0;
    chrome.storage.local.set({ lastManualDownloadEvent: { ...payload, consumed: true } });
  }

  document.addEventListener(
    "click",
    (event) => {
      const trigger = dom.getClickTrigger(event);
      if (!trigger) {
        return;
      }

      if (dom.isManualButtonClick(trigger)) {
        lastDownloadIntent = "manual";
        lastDownloadIntentAt = Date.now();

        const payload = payloadUtils.collectPayload(trigger, { pendingManualPayload });
        pendingManualPayload = payload;

        // Cache context for popup/debug regardless of mode.
        chrome.runtime.sendMessage({ type: "cache-manual-download", payload });

        if (shouldLaunchOnManualClick(payload, trigger)) {
          if (!protocolEnabledCache) {
            return;
          }
          const directPayload = withAccountMode(payload, "direct");
          pendingManualPayload = directPayload;
          clearIntentAndMarkConsumed(directPayload);
          chrome.runtime.sendMessage({ type: "manual-download-click", payload: directPayload });
          return;
        }

        // Standard path: launch occurs on Slow Download click.
        return;
      }

      const isSlowDownload = dom.isSlowButtonClick(trigger);
      if (!isSlowDownload) {
        return;
      }

      const payload = payloadUtils.collectPayload(trigger, { pendingManualPayload });
      pendingManualPayload = payload;

      const withinIntentWindow = Date.now() - lastDownloadIntentAt <= DOWNLOAD_INTENT_WINDOW_MS;
      if (!withinIntentWindow || lastDownloadIntent !== "manual") {
        return;
      }
      if (!protocolEnabledCache) {
        return;
      }

      cacheAccountDownloadMode("standard");
      const standardPayload = withAccountMode(payload, "standard");
      pendingManualPayload = standardPayload;
      clearIntentAndMarkConsumed(standardPayload);
      // Queue delayed protocol launch in the background so Nexus countdown can complete first.
      chrome.runtime.sendMessage({ type: "slow-download-click", payload: standardPayload });
      return;
    },
    true
  );

  chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    if (!message || message.type !== "launch-czt-protocol-in-page") {
      return;
    }

    const protocolUrl = String(message.protocolUrl || "").trim();
    if (!protocolUrl) {
      sendResponse({ ok: false, error: "missing protocol url" });
      return;
    }

    try {
      window.location.assign(protocolUrl);
      sendResponse({ ok: true });
    } catch (err) {
      sendResponse({ ok: false, error: String(err || "launch failed") });
    }
  });
})();
