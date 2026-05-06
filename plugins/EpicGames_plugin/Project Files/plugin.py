# CZT Mod Manager — Epic Games Plugin (v2 API)
# Adds an "Epic Games" path mode to the User Setup tab and a Shift+E hotkey
# that scans local drives for Epic manifests and resolves the active profile's
# install/exe paths.
from __future__ import annotations

import json
import os
import threading

from PySide6.QtWidgets import QCheckBox

from plugins_ import Host, Plugin


PATH_MODE_TAG = "epic-games_plugin"


class EpicGamesPlugin(Plugin):
    def enable(self) -> None:
        self._checkbox: QCheckBox | None = None
        self._main_menu_tab = None

        win = self.host.ui.main_window()
        if win is None:
            self.host.log.error("UI not ready; cannot install Epic checkbox.")
            return
        self._main_menu_tab = getattr(win, "main_menu_tab", None)
        if self._main_menu_tab is None:
            self.host.log.error("main_menu_tab not available; aborting.")
            return

        self.host.hotkeys.register("Shift+E", self._scan)

        cb = QCheckBox("Epic Games")
        is_epic = (
            self.host.profiles.current()
            and self.host.config.get("profile_path_mode", {}).get(self.host.profiles.current(), "").strip().lower() == PATH_MODE_TAG
        )
        cb.setChecked(bool(is_epic))
        layout = getattr(self._main_menu_tab, "path_mode_layout", None)
        if layout is None:
            self.host.log.error("path_mode_layout not found on main_menu_tab.")
            return
        layout.addWidget(cb)
        cb.stateChanged.connect(self._on_toggle)
        if hasattr(self._main_menu_tab, "register_pathing_checkbox"):
            self._main_menu_tab.register_pathing_checkbox(PATH_MODE_TAG, cb)
        self._checkbox = cb

        self.host.log.info(
            "Epic Games plugin enabled. Select a profile, choose 'Epic Games' path mode, then press Shift+E to scan."
        )

    def disable(self) -> None:
        cb = getattr(self, "_checkbox", None)
        if cb is not None:
            try:
                cb.setParent(None)
                cb.deleteLater()
            except Exception:
                pass
        self._checkbox = None

    # ---------------------------------------------------------------- toggle
    def _on_toggle(self, state) -> None:
        profile = self.host.profiles.current()
        if not profile:
            return
        cfg_modes = dict(self.host.config.get("profile_path_mode", {}) or {})
        if state:
            cfg_modes[profile] = PATH_MODE_TAG
            self.host.config.update({"profile_path_mode": cfg_modes})
            self.host.log.info(f"Epic path mode selected for profile '{profile}'.")
            self._scan()
        else:
            if cfg_modes.get(profile) == PATH_MODE_TAG:
                cfg_modes[profile] = ""
                self.host.config.update({"profile_path_mode": cfg_modes})

    # ------------------------------------------------------------------ scan
    def _scan(self) -> None:
        profile = self.host.profiles.current()
        if not profile:
            self.host.log.error("No profile selected; scan canceled.")
            return
        mode = (self.host.config.get("profile_path_mode", {}) or {}).get(profile, "").strip().lower()
        if mode != PATH_MODE_TAG:
            self.host.log.warning("Epic Games path mode is not selected; scan canceled.")
            return
        self.host.log.info(f"Scanning drives for Epic manifests for profile '{profile}'...")
        threading.Thread(target=self._scan_worker, args=(profile,), daemon=True).start()

    def _scan_worker(self, profile: str) -> None:
        manifests = self._find_manifests(profile)
        if not manifests:
            self.host.log.info("No Epic Games manifest data found.")
            return
        self.host.log.info(f"Saved Epic manifest data for profile '{profile}':")
        for fpath, install_dir, exe_name in manifests:
            self.host.log.info(f"  - {fpath}\n      Game folder: {install_dir}\n      Executable:  {exe_name}")

    # --------------------------------------------------------------- helpers
    def _find_manifests(self, profile: str):
        found: list[tuple[str, str, str]] = []
        profile_info = self.host.profiles.get(profile)
        profile_path = profile_info.get("path")
        if isinstance(profile_path, list) and profile_path:
            profile_subfolder = profile_path[0]
        elif isinstance(profile_path, str):
            profile_subfolder = profile_path
        else:
            profile_subfolder = None

        for d in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            drive_root = f"{d}:/"
            if not os.path.exists(drive_root):
                continue
            for root, _dirs, files in os.walk(drive_root):
                if os.path.basename(root).lower() != "manifests":
                    continue
                for fname in files:
                    if not fname.endswith(".item"):
                        continue
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            data = json.load(f)
                    except Exception as exc:
                        self.host.log.warning(f"Could not read {fpath}: {exc}")
                        continue
                    install_dir = data.get("InstallLocation") or data.get("ManifestLocation") or ""
                    exe_name = data.get("LaunchExecutable") or ""
                    manifest_name = data.get("DisplayName") or os.path.basename(os.path.normpath(install_dir))
                    if not self._matches_profile(profile, manifest_name, install_dir, profile_subfolder):
                        continue
                    if not (install_dir and exe_name and exe_name.strip()):
                        continue
                    final_profile_path = self._build_install_path(install_dir, profile_subfolder, profile)
                    exe_path = os.path.join(install_dir, exe_name)

                    resolved_exe = dict(self.host.config.get("resolved_exe_paths", {}) or {})
                    resolved_profiles = dict(self.host.config.get("resolved_profile_paths", {}) or {})
                    resolved_exe[profile] = exe_path
                    resolved_profiles[profile] = final_profile_path
                    self.host.config.update({
                        "resolved_exe_paths": resolved_exe,
                        "resolved_profile_paths": resolved_profiles,
                        "set_profile_path": final_profile_path,
                    })
                    found.append((fpath, install_dir, exe_name))
        return found

    @staticmethod
    def _norm(s: str) -> str:
        return str(s).replace(" ", "").replace("-", "").replace("_", "").lower()

    def _matches_profile(self, profile: str, manifest_name: str, install_dir: str, subfolder) -> bool:
        n_profile = self._norm(profile)
        n_name = self._norm(manifest_name)
        if n_profile and n_name and (n_profile in n_name or n_name in n_profile):
            return True
        if subfolder:
            sub = subfolder[0] if isinstance(subfolder, list) else subfolder
            n_sub = self._norm(sub)
            n_dir = self._norm(install_dir)
            if n_sub and n_dir and (n_sub in n_dir or n_dir in n_sub):
                return True
        return False

    def _build_install_path(self, install_dir: str, subfolder, profile: str) -> str:
        if not subfolder:
            return os.path.normpath(install_dir)
        if isinstance(subfolder, list):
            if not subfolder:
                return os.path.normpath(install_dir)
            sub = subfolder[0].lstrip("\\/")
        else:
            sub = subfolder.lstrip("\\/")
        install_last = os.path.basename(os.path.normpath(install_dir))
        parts = os.path.normpath(sub).split(os.sep)
        if parts and self._norm(parts[0]) == self._norm(install_last):
            tail = os.path.join(*parts[1:]) if len(parts) > 1 else ""
        elif parts and profile and self._norm(profile) in self._norm(install_last):
            tail = os.path.join(*parts[1:]) if len(parts) > 1 else ""
        else:
            tail = sub
        if tail:
            return os.path.normpath(os.path.join(install_dir, tail))
        return os.path.normpath(install_dir)


def register(host: Host) -> Plugin:
    return EpicGamesPlugin(host)
