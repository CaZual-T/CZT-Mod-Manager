const SLOW_DOWNLOAD_LAUNCH_DELAY_MS = 5500;
const RECENT_MANUAL_LAUNCH_WINDOW_MS = 9000;
let pendingLaunchTimer = null;
let lastManualLaunchAt = 0;

function buildCztProtocolUrl(payload) {
  const p = payload || {};
  const query = new URLSearchParams({
    game: String(p.game || ""),
    mod_id: String(p.modId || ""),
    file_id: String(p.fileId || ""),
    page_url: String(p.pageUrl || ""),
    source: "nexus-manual-download"
  });
  if (p.nxmKey) {
    query.set("key", String(p.nxmKey));
  }
  if (p.nxmExpires) {
    query.set("expires", String(p.nxmExpires));
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
    timestamp: Date.now(),
    source: latest.source || base.source || "nexus-manual-download"
  };
}

async function maybeLaunchCzt(payload, delayMs = 0) {
  const shouldLaunch = await isProtocolEnabled();
  if (!shouldLaunch) {
    return;
  }

  const protocolUrl = buildCztProtocolUrl(payload);
  if (delayMs > 0) {
    if (pendingLaunchTimer) {
      clearTimeout(pendingLaunchTimer);
      pendingLaunchTimer = null;
    }
    pendingLaunchTimer = setTimeout(() => {
      pendingLaunchTimer = null;
      launchProtocolUrl(protocolUrl);
    }, delayMs);
    return;
  }

  launchProtocolUrl(protocolUrl);
}

function launchProtocolUrl(protocolUrl) {
  chrome.tabs.create({ url: protocolUrl, active: true }, () => {
    if (chrome.runtime.lastError) {
      // Keep this silent; popup provides explicit feedback paths.
    }
  });
}

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message && message.type === "launch-czt-protocol") {
    try {
      launchProtocolUrl(String(message.protocolUrl || ""));
      sendResponse({ ok: true });
    } catch (err) {
      sendResponse({ ok: false, error: String(err || "unknown error") });
    }
    return true;
  }

  if (!message || message.type !== "manual-download-click") {
    if (!message || message.type !== "slow-download-click") {
      return;
    }

    // If manual just launched, skip a duplicate delayed slow launch.
    if (Date.now() - lastManualLaunchAt < RECENT_MANUAL_LAUNCH_WINDOW_MS) {
      sendResponse({ ok: true, skipped: "recent-manual-launch" });
      return true;
    }

    const payload = message.payload || {};
    readLastEvent()
      .then((last) => mergePayload(last, payload))
      .then((merged) => saveLastEvent(merged).then(() => merged))
      .then((merged) => maybeLaunchCzt(merged, SLOW_DOWNLOAD_LAUNCH_DELAY_MS).then(() => merged))
      .then((merged) => {
        sendResponse({ ok: true, protocolUrl: buildCztProtocolUrl(merged) });
      })
      .catch((err) => {
        sendResponse({ ok: false, error: String(err || "unknown error") });
      });

    return true;
  }

  const payload = message.payload || {};
  saveLastEvent(payload)
    .then(() => {
      lastManualLaunchAt = Date.now();
      return maybeLaunchCzt(payload, 0);
    })
    .then(() => {
      sendResponse({ ok: true, protocolUrl: buildCztProtocolUrl(payload) });
    })
    .catch((err) => {
      sendResponse({ ok: false, error: String(err || "unknown error") });
    });

  return true;
});
