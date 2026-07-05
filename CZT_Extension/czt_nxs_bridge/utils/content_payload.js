(() => {
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

  function findFileIdFromElementChain(trigger) {
    // Walk strictly up the clicked element's ancestors. This stays on the path
    // of the file the user actually clicked and never drifts to a sibling file,
    // so multi-file pages resolve the correct file id.
    let current = trigger;
    while (current && current instanceof Element) {
      const dataFileId = String(current.getAttribute("data-file-id") || "").trim();
      if (/^\d+$/.test(dataFileId)) {
        return dataFileId;
      }
      const dataId = String(current.getAttribute("data-id") || "").trim();
      if (/^\d+$/.test(dataId)) {
        return dataId;
      }
      const idMatch = String(current.id || "").match(/file[-_a-z]*?(\d{2,})/i);
      if (idMatch && idMatch[1]) {
        return idMatch[1];
      }
      current = current.parentElement;
    }
    return "";
  }

  function findFileIdFromScope(trigger) {
    const dom = globalThis.CztNexusBridgeDom;
    const scope = dom && typeof dom.getFileScope === "function" ? dom.getFileScope(trigger) : null;
    if (!scope || typeof scope.querySelectorAll !== "function") {
      return "";
    }
    const links = scope.querySelectorAll("a[href*='file_id='], a[href*='/files/']");
    for (const link of links) {
      const id = findFileIdFromUrl(link.getAttribute("href") || "");
      if (id) {
        return id;
      }
    }
    return "";
  }

  function findNxmProtocolFromTrigger(trigger) {
    if (!trigger) {
      return "";
    }
    const attrs = ["href", "data-href", "data-download-url", "data-url"];
    let current = trigger;
    while (current && current instanceof Element) {
      for (const attr of attrs) {
        const raw = String(current.getAttribute(attr) || "").trim();
        if (!raw) {
          continue;
        }
        if (raw.toLowerCase().startsWith("nxm://")) {
          return raw;
        }
      }
      current = current.parentElement;
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

  function collectPayload(trigger, options) {
    const opts = options || {};
    const dom = globalThis.CztNexusBridgeDom;
    const modInfo = parseModPage(window.location.href);
    const href = trigger ? trigger.getAttribute("href") || "" : "";
    const nxmHref = findNxmProtocolFromTrigger(trigger);
    const nxm = parseNxmProtocol(nxmHref);
    const dataFileId = trigger ? trigger.getAttribute("data-file-id") || "" : "";
    const pendingManualPayload = opts.pendingManualPayload || null;
    const fileId =
      nxm.fileId ||
      dataFileId ||
      findFileIdFromUrl(href) ||
      findFileIdFromElementChain(trigger) ||
      findFileIdFromScope(trigger) ||
      String((pendingManualPayload && pendingManualPayload.fileId) || "");

    const game = nxm.game || modInfo.game || String((pendingManualPayload && pendingManualPayload.game) || "");
    const modId =
      nxm.modId || modInfo.modId || String((pendingManualPayload && pendingManualPayload.modId) || "");

    // Prefer the name read from THIS file's container; if the click happened in
    // a popup that doesn't expose the name, reuse what the original per-file
    // "Manual download" click captured rather than guessing the first file.
    const fileName =
      dom.readFileNameFromPage(trigger) ||
      String((pendingManualPayload && pendingManualPayload.fileName) || "");

    return {
      source: "nexus-manual-download",
      pageUrl: window.location.href,
      game,
      modName: dom.readModName(),
      modId,
      fileId,
      buttonText: dom.triggerLabelText(trigger),
      href,
      fileName,
      nxmUrl: nxm.nxmUrl,
      nxmKey: nxm.nxmKey,
      nxmExpires: nxm.nxmExpires,
      timestamp: Date.now()
    };
  }

  globalThis.CztNexusBridgePayload = {
    collectPayload,
    parseNxmProtocol
  };
})();