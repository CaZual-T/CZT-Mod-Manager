(() => {
  function StandardizeFileName(value) {
    const raw = String(value || "").replace(/\r/g, "\n");
    const lines = raw
      .split("\n")
      .map((line) => line.trim())
      .filter(Boolean);

    const skipLabels = new Set([
      "cloud_download",
      "downloaded",
      "date uploaded",
      "file size",
      "unique dls",
      "total dls",
      "version"
    ]);

    for (const line of lines) {
      const normalized = line.replace(/\s+/g, " ").trim();
      const lowered = normalized.toLowerCase();
      if (!normalized || normalized.length > 180) {
        continue;
      }
      if (skipLabels.has(lowered)) {
        continue;
      }
      if (/^[+_\-\s]+$/.test(normalized)) {
        continue;
      }
      return normalized;
    }

    return "";
  }

  function getClickTrigger(event) {
    const actionSelectors = "a,button,[role='button']";
    const dataSelectors = "[data-download-url],[data-href],[data-url]";
    const path = typeof event.composedPath === "function" ? event.composedPath() : [];

    // First pass: prefer actual clickable action elements.
    for (const item of path) {
      if (!(item instanceof Element)) {
        continue;
      }
      if (item.matches(actionSelectors)) {
        return item;
      }
      if (typeof item.closest === "function") {
        const found = item.closest(actionSelectors);
        if (found) {
          return found;
        }
      }
    }

    // Fallback pass: support pages that use data-* clickable wrappers.
    for (const item of path) {
      if (!(item instanceof Element)) {
        continue;
      }
      if (item.matches(dataSelectors)) {
        return item;
      }
      if (typeof item.closest === "function") {
        const found = item.closest(dataSelectors);
        if (found) {
          return found;
        }
      }
    }

    return null;
  }

  function triggerLabelText(trigger) {
    const target =
      (trigger && trigger.closest && trigger.closest("a,button,[role='button']")) ||
      trigger;
    if (!target) {
      return "";
    }
    const text = String(target.textContent || "").toLowerCase();
    const aria = String(target.getAttribute("aria-label") || "").toLowerCase();
    return `${text} ${aria}`.trim();
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

  function readFileNameFromPage(trigger) {
    // Try the slow download button href — Nexus CDN links end with the actual filename.
    const href = trigger ? trigger.getAttribute("href") || "" : "";
    if (href) {
      try {
        const url = new URL(href, window.location.origin);
        const lastSegment = url.pathname.split("/").filter(Boolean).pop() || "";
        if (lastSegment && lastSegment.includes(".")) {
          return StandardizeFileName(decodeURIComponent(lastSegment));
        }
      } catch {
        // continue
      }
    }

    // Try common Nexus DOM selectors for the displayed file name.
    const selectors = [
      "[data-file-name]",
      ".popup-file-name",
      ".file-expander-header",
      ".download-file-name"
    ];
    for (const sel of selectors) {
      const el = document.querySelector(sel);
      if (el) {
        const name = StandardizeFileName(el.getAttribute("data-file-name") || el.textContent || "");
        if (name) {
          return name;
        }
      }
    }

    // Last resort: parse page title "Download - FileName - Nexus Mods".
    const titleMatch = String(document.title || "").match(/^Download\s*[-\u2013]\s*(.+?)\s*[-\u2013]/i);
    if (titleMatch && titleMatch[1]) {
      return StandardizeFileName(titleMatch[1]);
    }

    return "";
  }

  function isManualButtonClick(trigger) {
    const label = triggerLabelText(trigger);
    return label.includes("manual") && label.includes("download");
  }

  function isSlowButtonClick(trigger) {
    const label = triggerLabelText(trigger);
    return label.includes("slow") && label.includes("download");
  }

  function hasSlowDownloadOption(trigger) {
    const roots = [];
    if (trigger && typeof trigger.closest === "function") {
      const scopedRoot = trigger.closest("[role='dialog'], .modal, .popup, .download, .download-panel");
      if (scopedRoot) {
        roots.push(scopedRoot);
      }
    }
    roots.push(document);

    for (const root of roots) {
      if (!root || typeof root.querySelectorAll !== "function") {
        continue;
      }
      const nodes = root.querySelectorAll("a,button,[role='button']");
      for (const node of nodes) {
        const text = String(node.textContent || "").toLowerCase();
        const aria = String(node.getAttribute("aria-label") || "").toLowerCase();
        const label = `${text} ${aria}`.trim();
        if (label.includes("slow") && label.includes("download")) {
          return true;
        }
      }
    }

    return false;
  }

  globalThis.CztNexusBridgeDom = {
    getClickTrigger,
    hasSlowDownloadOption,
    isManualButtonClick,
    isSlowButtonClick,
    readFileNameFromPage,
    readModName,
    StandardizeFileName,
    triggerLabelText
  };
})();