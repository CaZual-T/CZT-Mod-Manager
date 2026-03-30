(() => {
  let pendingManualPayload = null;
  let protocolEnabledCache = true;

  chrome.storage.local
    .get({ protocolStatus: true, lastManualDownloadEvent: null })
    .then((obj) => {
      protocolEnabledCache = Boolean(obj.protocolStatus);
      const last = obj.lastManualDownloadEvent;
      if (last && typeof last === "object") {
        pendingManualPayload = last;
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
    if (changes.lastManualDownloadEvent) {
      const latest = changes.lastManualDownloadEvent.newValue;
      if (latest && typeof latest === "object") {
        pendingManualPayload = latest;
      }
    }
  });

  function getClickTrigger(event) {
    const selectors = "a,button,[role='button'],[data-download-url],[data-href],[data-url]";
    const path = typeof event.composedPath === "function" ? event.composedPath() : [];
    for (const item of path) {
      if (!(item instanceof Element)) {
        continue;
      }
      if (item.matches(selectors)) {
        return item;
      }
      if (typeof item.closest === "function") {
        const found = item.closest(selectors);
        if (found) {
          return found;
        }
      }
    }
    return null;
  }

  function isActionTrigger(trigger) {
    if (!trigger || !(trigger instanceof Element)) {
      return false;
    }
    return trigger.matches("a,button,[role='button']");
  }

  function parseModPage(urlString) {
    try {
      const url = new URL(urlString);
      const parts = url.pathname.split("/").filter(Boolean);
      const modsIndex = parts.indexOf("mods");
      if (modsIndex <= 0 || modsIndex + 1 >= parts.length) {
        return { game: "", modId: "" };
      }
      return {
        game: parts[modsIndex - 1] || "",
        modId: parts[modsIndex + 1] || ""
      };
    } catch {
      return { game: "", modId: "" };
    }
  }

  function findFileIdFromUrl(urlString) {
    if (!urlString) {
      return "";
    }
    try {
      const url = new URL(urlString, window.location.origin);
      const qFile = url.searchParams.get("file_id") || url.searchParams.get("id");
      if (qFile && /^\d+$/.test(qFile)) {
        return qFile;
      }
      const match = url.pathname.match(/\/files\/(\d+)/i);
      if (match && match[1]) {
        return match[1];
      }
      return "";
    } catch {
      return "";
    }
  }

  function findNxmProtocolFromTrigger(trigger) {
    if (!trigger) {
      return "";
    }
    const attrs = ["href", "data-href", "data-download-url", "data-url"];
    for (const attr of attrs) {
      const raw = String(trigger.getAttribute(attr) || "").trim();
      if (!raw) {
        continue;
      }
      if (raw.toLowerCase().startsWith("nxm://")) {
        return raw;
      }
    }

    return "";
  }

  function parseNxmProtocol(nxmUrl) {
    const out = {
      nxmUrl: "",
      game: "",
      modId: "",
      fileId: "",
      nxmKey: "",
      nxmExpires: ""
    };

    const value = String(nxmUrl || "").trim();
    if (!value.toLowerCase().startsWith("nxm://")) {
      return out;
    }

    out.nxmUrl = value;
    const pathMatch = value.match(/^nxm:\/\/([^/]+)\/mods\/(\d+)(?:\/files\/(\d+))?/i);
    if (pathMatch) {
      out.game = String(pathMatch[1] || "").toLowerCase();
      out.modId = String(pathMatch[2] || "");
      out.fileId = String(pathMatch[3] || "");
    }

    const queryStart = value.indexOf("?");
    if (queryStart >= 0) {
      const params = new URLSearchParams(value.slice(queryStart + 1));
      out.nxmKey = String(params.get("key") || "");
      out.nxmExpires = String(params.get("expires") || "");
    }

    return out;
  }

  function readModName() {
    const heading = document.querySelector("h1");
    const headingText = heading && heading.textContent ? heading.textContent.trim() : "";
    if (headingText) {
      return headingText;
    }

    const ogTitle = document.querySelector("meta[property='og:title']");
    const ogText = ogTitle ? String(ogTitle.getAttribute("content") || "").trim() : "";
    if (ogText) {
      return ogText;
    }

    const title = String(document.title || "").trim();
    if (!title) {
      return "";
    }
    return title.replace(/\s+at\s+.*$/i, "").trim();
  }

  function looksLikeManualDownloadClick(trigger) {
    if (!trigger) {
      return false;
    }
    if (!isActionTrigger(trigger)) {
      return false;
    }

    const text = (trigger.textContent || "").toLowerCase();
    const aria = (trigger.getAttribute("aria-label") || "").toLowerCase();
    const classes = (trigger.className || "").toString().toLowerCase();
    const href = ((trigger.getAttribute("href") || "") + "").toLowerCase();

    const textSignal = text.includes("manual") && text.includes("download");
    const ariaSignal = aria.includes("manual") && aria.includes("download");
    const classSignal = classes.includes("manual") && classes.includes("download");
    const hrefSignal = href.includes("manual") || href.includes("downloads") || href.includes("file_id=");

    return textSignal || ariaSignal || classSignal || hrefSignal;
  }

  function looksLikeSlowDownloadClick(trigger) {
    if (!trigger) {
      return false;
    }
    if (!isActionTrigger(trigger)) {
      return false;
    }

    const text = (trigger.textContent || "").toLowerCase();
    const aria = (trigger.getAttribute("aria-label") || "").toLowerCase();
    const id = (trigger.id || "").toLowerCase();
    const classes = (trigger.className || "").toString().toLowerCase();
    const href = ((trigger.getAttribute("href") || "") + "").toLowerCase();
    const nxmUrl = findNxmProtocolFromTrigger(trigger).toLowerCase();

    const textSignal = text.includes("slow") && text.includes("download");
    const ariaSignal = aria.includes("slow") && aria.includes("download");
    const idSignal = id.includes("slow") && id.includes("download");
    const classSignal = classes.includes("slow") && classes.includes("download");
    const hrefSignal = href.includes("slow") && href.includes("download");
    const nxmSignal = nxmUrl.startsWith("nxm://");

    if (text.includes("manual") || aria.includes("manual")) {
      return false;
    }

    if (nxmSignal) {
      return true;
    }

    return textSignal || ariaSignal || idSignal || classSignal || hrefSignal;
  }

  function collectPayload(trigger) {
    const modInfo = parseModPage(window.location.href);
    const href = trigger ? trigger.getAttribute("href") || "" : "";
    const nxmHref = findNxmProtocolFromTrigger(trigger);
    const nxm = parseNxmProtocol(nxmHref);
    const dataFileId = trigger ? trigger.getAttribute("data-file-id") || "" : "";
    const fileId =
      nxm.fileId ||
      dataFileId ||
      findFileIdFromUrl(href) ||
      String((pendingManualPayload && pendingManualPayload.fileId) || "");

    const game = nxm.game || modInfo.game || String((pendingManualPayload && pendingManualPayload.game) || "");
    const modId = nxm.modId || modInfo.modId || String((pendingManualPayload && pendingManualPayload.modId) || "");

    return {
      source: "nexus-manual-download",
      pageUrl: window.location.href,
      game,
      modName: readModName(),
      modId,
      fileId,
      buttonText: (trigger && trigger.textContent ? trigger.textContent.trim() : ""),
      href,
      nxmUrl: nxm.nxmUrl,
      nxmKey: nxm.nxmKey,
      nxmExpires: nxm.nxmExpires,
      timestamp: Date.now()
    };
  }

  document.addEventListener(
    "click",
    (event) => {
      const trigger = getClickTrigger(event);
      const isManualDownload = looksLikeManualDownloadClick(trigger);
      const isSlowDownload = looksLikeSlowDownloadClick(trigger);

      if (!isManualDownload && !isSlowDownload) {
        return;
      }

      const payload = collectPayload(trigger);
      pendingManualPayload = payload;

      if (isSlowDownload) {
        if (!protocolEnabledCache) {
          return;
        }
        // Queue delayed protocol launch in the background so Nexus countdown can complete first.
        chrome.runtime.sendMessage({ type: "slow-download-click", payload });
        return;
      }

      chrome.runtime.sendMessage({ type: "manual-download-click", payload });
    },
    true
  );
})();
