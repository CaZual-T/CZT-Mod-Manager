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

function setStatus(msg) {
  const status = document.getElementById("status");
  status.textContent = msg || "";
}

function renderEvent(payload) {
  const emptyState = document.getElementById("emptyState");
  const eventState = document.getElementById("eventState");

  if (!payload) {
    emptyState.style.display = "block";
    eventState.style.display = "none";
    return;
  }

  emptyState.style.display = "none";
  eventState.style.display = "block";

  document.getElementById("game").textContent = String(payload.game || "");
  document.getElementById("modName").textContent = String(payload.modName || "");
  document.getElementById("modId").textContent = String(payload.modId || "");
  document.getElementById("fileId").textContent = String(payload.fileId || "");
  document.getElementById("buttonText").textContent = String(payload.buttonText || "");

  const when = payload.timestamp ? new Date(Number(payload.timestamp)) : null;
  document.getElementById("time").textContent = when ? when.toLocaleString() : "";
}

async function loadData() {
  const obj = await chrome.storage.local.get({
    lastManualDownloadEvent: null,
    protocolStatus: true
  });
  renderEvent(obj.lastManualDownloadEvent);
  const protocolEnabled = document.getElementById("protocolEnabled");
  protocolEnabled.checked = Boolean(obj.protocolStatus);

  document.getElementById("launchNow").addEventListener("click", async () => {
    const data = obj.lastManualDownloadEvent;
    if (!data) {
      setStatus("No event to launch yet.");
      return;
    }
    const protocolUrl = buildCztProtocolUrl(data);
    try {
      await chrome.runtime.sendMessage({ type: "launch-czt-protocol", protocolUrl });
      setStatus("Launch requested. Check browser prompt.");
    } catch {
      // Fallback in popup context for browsers that restrict service worker launches.
      window.location.href = protocolUrl;
      setStatus("Launch requested.");
    }
  });

  protocolEnabled.addEventListener("change", async () => {
    await chrome.storage.local.set({ protocolStatus: protocolEnabled.checked });
    setStatus(protocolEnabled.checked ? "CZT protocol enabled." : "CZT protocol disabled.");
  });
}

loadData().catch((err) => setStatus(String(err || "Failed to load popup.")));
