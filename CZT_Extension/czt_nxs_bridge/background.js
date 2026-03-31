const SLOW_DOWNLOAD_LAUNCH_DELAY_MS = 5500;
let pendingLaunchTimer = null;
let pendingLaunchTabId = null;
const NEXUS_VALIDATE_URL = "https://api.nexusmods.com/v1/users/validate.json";

function normalizeAccountDownloadMode(value) {
  if (value === "direct" || value === "standard") {
    return value;
  }
  return "unknown";
}

function inferAccountTier(apiUser) {
  const user = apiUser || {};
  if (user.is_premium === true) {
    return "premium";
  }
  if (user.is_supporter === true) {
    return "supporter";
  }

  const roles = Array.isArray(user.membership_roles) ? user.membership_roles : [];
  for (const role of roles) {
    const text = String(role || "").toLowerCase();
    if (text.includes("premium")) {
      return "premium";
    }
    if (text.includes("support")) {
      return "supporter";
    }
  }

  return "standard";
}

function tierToAccountMode(tier) {
  return tier === "premium" ? "direct" : "standard";
}

async function validateNexusApiKey(apiKey) {
  const key = String(apiKey || "").trim();
  if (!key) {
    throw new Error("API key is required.");
  }

  const response = await fetch(NEXUS_VALIDATE_URL, {
    method: "GET",
    headers: {
      apikey: key,
      accept: "application/json",
      "application-name": "CZT Nexus Bridge",
      "application-version": "0.1.0"
    }
  });

  if (!response.ok) {
    if (response.status === 401 || response.status === 403) {
      throw new Error("Nexus API key rejected. Check the key and try again.");
    }
    throw new Error(`Nexus API request failed (${response.status}).`);
  }

  return response.json();
}

function buildCztProtocolUrl(payload) {
  const p = payload || {};
  const query = new URLSearchParams({
    game: String(p.game || ""),
    mod_id: String(p.modId || ""),
    file_id: String(p.fileId || ""),
    event_ts_ms: String(Number(p.timestamp || 0) || 0),
    page_url: String(p.pageUrl || ""),
    source: "nexus-manual-download"
  });
  if (p.fileName) {
    query.set("file_name", String(p.fileName));
  }
  if (p.nxmKey) {
    query.set("key", String(p.nxmKey));
  }
  if (p.nxmExpires) {
    query.set("expires", String(p.nxmExpires));
  }
  if (p.accountMode) {
    query.set("account_mode", String(p.accountMode));
  }
  return `cztmm://nexus/manual_download?${query.toString()}`;
}

async function isProtocolEnabled() {
  const obj = await chrome.storage.local.get({ protocolStatus: true });
  return Boolean(obj.protocolStatus);
}

async function saveLastEvent(payload) {
  await chrome.storage.local.set({
    lastManualDownloadEvent: payload || null,
    lastUpdatedAt: Date.now()
  });
}

async function readLastEvent() {
  const obj = await chrome.storage.local.get({ lastManualDownloadEvent: null });
  return obj.lastManualDownloadEvent || null;
}

function mergePayload(basePayload, latestPayload) {
  const base = basePayload || {};
  const latest = latestPayload || {};
  return {
    ...base,
    ...latest,
    game: String(latest.game || base.game || ""),
    modId: String(latest.modId || base.modId || ""),
    fileId: String(latest.fileId || base.fileId || ""),
    nxmKey: String(latest.nxmKey || base.nxmKey || ""),
    nxmExpires: String(latest.nxmExpires || base.nxmExpires || ""),
    accountMode: String(latest.accountMode || base.accountMode || ""),
    // Preserve original click timestamp so the app can detect files downloaded before app launch.
    timestamp: Number(latest.timestamp || base.timestamp || Date.now()),
    source: latest.source || base.source || "nexus-manual-download"
  };
}

async function maybeLaunchCzt(payload, delayMs = 0, tabId = null) {
  const shouldLaunch = await isProtocolEnabled();
  if (!shouldLaunch) {
    return;
  }

  const protocolUrl = buildCztProtocolUrl(payload);
  if (delayMs > 0) {
    if (pendingLaunchTimer) {
      clearTimeout(pendingLaunchTimer);
      pendingLaunchTimer = null;
      pendingLaunchTabId = null;
    }
    pendingLaunchTabId = tabId;
    pendingLaunchTimer = setTimeout(() => {
      pendingLaunchTimer = null;
      const runTabId = pendingLaunchTabId;
      pendingLaunchTabId = null;
      launchProtocolUrl(protocolUrl, runTabId);
    }, delayMs);
    return;
  }

  launchProtocolUrl(protocolUrl, tabId);
}

function launchProtocolUrl(protocolUrl, tabId = null) {
  if (typeof tabId === "number") {
    chrome.tabs.sendMessage(
      tabId,
      { type: "launch-czt-protocol-in-page", protocolUrl },
      () => {
        if (!chrome.runtime.lastError) {
          return;
        }
        // Fallback if content script is not available on this tab.
        chrome.tabs.create({ url: protocolUrl, active: true }, () => {
          // Keep this silent; popup provides explicit feedback paths.
        });
      }
    );
    return;
  }

  chrome.tabs.create({ url: protocolUrl, active: true }, () => {
    if (chrome.runtime.lastError) {
      // Keep this silent; popup provides explicit feedback paths.
    }
  });
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message && message.type === "nexus-api-setup") {
    const apiKey = String((message && message.apiKey) || "").trim();
    validateNexusApiKey(apiKey)
      .then((userData) => {
        const accountTier = inferAccountTier(userData);
        const accountDownloadMode = normalizeAccountDownloadMode(tierToAccountMode(accountTier));
        const now = Date.now();
        return chrome.storage.local
          .set({
            accountDownloadMode,
            accountDownloadModeSource: "api",
            nexusApiConfig: {
              configured: true,
              configuredAt: now,
              validatedAt: now,
              accountTier,
              userName: String(userData.name || ""),
              userId: Number(userData.user_id || 0) || 0
            },
            nexusApiKey: apiKey
          })
          .then(() => ({ accountDownloadMode, accountTier }));
      })
      .then((saved) => {
        sendResponse({
          ok: true,
          accountDownloadMode: saved.accountDownloadMode,
          accountTier: saved.accountTier
        });
      })
      .catch((err) => {
        sendResponse({ ok: false, error: String((err && err.message) || err || "unknown error") });
      });
    return true;
  }

  if (message && message.type === "nexus-api-reset") {
    chrome.storage.local
      .set({
        accountDownloadMode: "unknown",
        accountDownloadModeSource: "auto",
        nexusApiConfig: null,
        nexusApiKey: ""
      })
      .then(() => {
        sendResponse({ ok: true });
      })
      .catch((err) => {
        sendResponse({ ok: false, error: String((err && err.message) || err || "unknown error") });
      });
    return true;
  }

  if (message && message.type === "cache-manual-download") {
    const payload = message.payload || {};
    saveLastEvent(payload)
      .then(() => {
        sendResponse({ ok: true, cached: true });
      })
      .catch((err) => {
        sendResponse({ ok: false, error: String(err || "unknown error") });
      });
    return true;
  }

  if (!message || message.type !== "manual-download-click") {
    if (!message || message.type !== "slow-download-click") {
      return;
    }

    const payload = message.payload || {};
    const senderTabId = sender && sender.tab ? sender.tab.id : null;
    readLastEvent()
      .then((last) => mergePayload(last, payload))
      .then((merged) => saveLastEvent(merged).then(() => merged))
      .then((merged) => maybeLaunchCzt(merged, SLOW_DOWNLOAD_LAUNCH_DELAY_MS, senderTabId).then(() => merged))
      .then((merged) => {
        sendResponse({ ok: true, protocolUrl: buildCztProtocolUrl(merged) });
      })
      .catch((err) => {
        sendResponse({ ok: false, error: String(err || "unknown error") });
      });

    return true;
  }

  // Legacy/manual direct launch path (kept for compatibility).
  const payload = message.payload || {};
  const senderTabId = sender && sender.tab ? sender.tab.id : null;
  saveLastEvent(payload)
    .then(() => {
      return maybeLaunchCzt(payload, 0, senderTabId);
    })
    .then(() => {
      sendResponse({ ok: true, protocolUrl: buildCztProtocolUrl(payload) });
    })
    .catch((err) => {
      sendResponse({ ok: false, error: String(err || "unknown error") });
    });

  return true;
});
