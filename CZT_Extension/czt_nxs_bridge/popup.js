function setStatus(msg) {
  const status = document.getElementById("status");
  status.textContent = msg || "";
}

function renderProtocolState(enabled) {
  const state = document.getElementById("protocolStateText");
  state.textContent = enabled ? "Enabled" : "Disabled";
  state.classList.toggle("on", Boolean(enabled));
  state.classList.toggle("off", !enabled);
}

function normalizeAccountMode(value) {
  if (value === "direct" || value === "standard") {
    return value;
  }
  return "unknown";
}

function modeLabel(mode) {
  if (mode === "direct") {
    return "Premium API";
  }
  if (mode === "standard") {
    return "Standard API";
  }
  return "N/A";
}

function renderAccountModeSummary(obj) {
  const row = document.getElementById("accountModeSummary");
  const mode = normalizeAccountMode(obj.accountDownloadMode);
  const cfg = obj.nexusApiConfig || null;
  row.textContent = "";

  const label = document.createElement("span");
  label.className = "account-type-label";
  label.textContent = "Account Type: ";

  const value = document.createElement("span");
  const mappedClass = mode === "direct" ? "premium" : mode === "standard" ? "standard" : "standard";
  value.className = `account-type-value ${mappedClass}`;
  value.textContent = modeLabel(mode);

  row.appendChild(label);
  row.appendChild(value);

  if (cfg && cfg.userName) {
    const userText = document.createElement("span");
    userText.textContent = ` | User: ${String(cfg.userName)}`;
    row.appendChild(userText);
  }
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

  const when = payload.timestamp ? new Date(Number(payload.timestamp)) : null;
  document.getElementById("time").textContent = when ? when.toLocaleString() : "";
}

async function loadData() {
  const obj = await chrome.storage.local.get({
    lastManualDownloadEvent: null,
    protocolStatus: true,
    accountDownloadMode: "unknown",
    nexusApiConfig: null
  });
  renderEvent(obj.lastManualDownloadEvent);
  renderAccountModeSummary(obj);
  const protocolEnabled = document.getElementById("protocolEnabled");
  protocolEnabled.checked = Boolean(obj.protocolStatus);
  renderProtocolState(Boolean(obj.protocolStatus));
  const setupApi = document.getElementById("setupApi");
  const resetApi = document.getElementById("resetApi");

  protocolEnabled.addEventListener("change", async () => {
    await chrome.storage.local.set({ protocolStatus: protocolEnabled.checked });
    renderProtocolState(protocolEnabled.checked);
  });

  setupApi.addEventListener("click", async () => {
    const raw = window.prompt(
      "- Go to: https://www.nexusmods.com/settings/api-keys \n- Scroll down to CZT Mod Manager and click 'Request Key'\n- Enter the API key below:",
      ""
    );
    if (raw === null) {
      return;
    }
    const apiKey = String(raw || "").trim();
    if (!apiKey) {
      setStatus("Setup canceled: API key is empty.");
      return;
    }

    setStatus("Validating API key...");
    try {
      const res = await chrome.runtime.sendMessage({
        type: "nexus-api-setup",
        apiKey
      });

      if (!res || !res.ok) {
        const msg = res && res.error ? String(res.error) : "API setup failed.";
        setStatus(msg);
        return;
      }

      const latest = await chrome.storage.local.get({
        accountDownloadMode: "unknown",
        nexusApiConfig: null
      });
      renderAccountModeSummary(latest);

      setStatus(
        `API setup complete. Account mode locked to ${modeLabel(normalizeAccountMode(res.accountDownloadMode))}.`
      );
    } catch (err) {
      setStatus(String(err || "API setup failed."));
    }
  });

  resetApi.addEventListener("click", async () => {
    try {
      const res = await chrome.runtime.sendMessage({ type: "nexus-api-reset" });
      if (!res || !res.ok) {
        const msg = res && res.error ? String(res.error) : "Failed to reset API.";
        setStatus(msg);
        return;
      }

      const latest = await chrome.storage.local.get({
        accountDownloadMode: "unknown",
        nexusApiConfig: null
      });
      renderAccountModeSummary(latest);
      setStatus("API setup reset. Account mode returned to auto detect.");
    } catch (err) {
      setStatus(String(err || "Failed to reset API."));
    }
  });
}

loadData().catch((err) => setStatus(String(err || "Failed to load popup.")));
