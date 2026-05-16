# CZT Mod Manager — UnleashTheMods plugin (v2 API)
# Wraps the bundled UnleashTheMods_Plugin.exe so that running the plugin merges
# the currently checked mods into the active profile's mods folder.
from __future__ import annotations

import os
import shutil
import subprocess

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from czt_plugins import Host, Plugin
from utilities_global.czt_root_file_system.Required_Folders import (
    build_profile_folder_paths,
    build_required_root_paths,
)


class UnleashTheModsPlugin(Plugin):
    def enable(self) -> None:
        # Run on demand from the Plugins menu.
        self.host.ui.add_menu_item("Run UnleashTheMods Merge", self._run_merge)
        self.host.log.info(
            "UnleashTheMods plugin enabled — choose 'Plugins → Run UnleashTheMods Merge' to merge checked mods."
        )

    # -------------------------------------------------------------- workflow
    def _run_merge(self) -> None:
        try:
            self._do_merge()
        except Exception as exc:
            self.host.log.error(f"Unhandled exception: {exc}")

    def _do_merge(self) -> None:
        root = self.host.czt_root or self.host.config.get("czt_root_folder", "")
        local_exe = os.path.join(os.path.dirname(__file__), "UnleashTheMods_Plugin.exe")
        exe_path = local_exe
        # Legacy fallback for older installations that still keep binaries in /plugins/scripts/.
        if not os.path.isfile(exe_path):
            exe_path = os.path.join(root, "plugins", "scripts", "UTM_plugin", "UnleashTheMods_Plugin.exe")

        profile = self.host.profiles.current() or self.host.config.get("current_game_profile", "") or ""
        profile = str(profile).strip()
        resolved_paths = self.host.config.get("resolved_profile_paths", {}) or {}
        source = resolved_paths.get(profile) or self.host.config.get("set_profile_path")

        profile_for_paths = profile or "default"
        profile_cfg = self.host.profiles.get(profile_for_paths) or {}
        profile_paths = build_profile_folder_paths(root, profile_for_paths, profile_cfg)
        root_paths = build_required_root_paths(root)

        mods = profile_paths.get("mods_dir", "")
        staging_root = str(root_paths.get("mods_src", "") or "")
        staging_area = os.path.join(staging_root, "_utm_temp") if staging_root else ""

        if not source or not os.path.isdir(source):
            self.host.log.error(f"Source folder not found: {source}")
            return
        if not os.path.isfile(exe_path):
            self.host.log.error(f"Plugin EXE not found: {exe_path}")
            return
        if not os.path.isdir(mods):
            self.host.log.error(f"Mods folder not found: {mods}")
            return
        if not staging_area:
            self.host.log.error("Staging path is not configured.")
            return

        selected_mods = [
            str(m.get("relpath") or "").strip()
            for m in self.host.mods.checked()
            if (m.get("relpath") or "").strip()
        ]
        if not selected_mods:
            self.host.log.info("No mods selected. Check the mods you want to merge first.")
            return

        selected_mods_dir = os.path.join(staging_area, "_selected_mods")
        if os.path.exists(selected_mods_dir):
            shutil.rmtree(selected_mods_dir)
        os.makedirs(selected_mods_dir, exist_ok=True)

        for relpath in selected_mods:
            src = os.path.join(mods, relpath)
            dst = os.path.join(selected_mods_dir, relpath)
            if not os.path.exists(src):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        if not os.listdir(selected_mods_dir):
            self.host.log.info("None of the selected mods were found on disk.")
            shutil.rmtree(selected_mods_dir, ignore_errors=True)
            return

        cmd = [exe_path, source, selected_mods_dir, staging_area, mods]
        try:
            proc = subprocess.Popen(cmd)
        except Exception as exc:
            self.host.log.error(f"Failed to launch EXE: {exc}")
            return

        self.host.log.info("Merge started. Waiting for completion...")
        QTimer.singleShot(300, lambda: self._poll_proc(proc))

    # ----------------------------------------------------------- async tail
    def _poll_proc(self, proc: subprocess.Popen) -> None:
        try:
            code = proc.poll()
        except Exception as exc:
            self.host.log.warning(f"Could not monitor merge completion: {exc}")
            return
        if code is None:
            QTimer.singleShot(300, lambda: self._poll_proc(proc))
            return
        if code != 0:
            self.host.log.warning(f"Merge process exited with code {code}.")
            return
        self._refresh_when_idle()

    def _refresh_when_idle(self, retries: int = 30) -> None:
        try:
            modal = QApplication.activeModalWidget()
        except Exception:
            modal = None
        if modal is not None and retries > 0:
            QTimer.singleShot(300, lambda: self._refresh_when_idle(retries - 1))
            return
        if self.host.mods.refresh():
            QTimer.singleShot(700, self.host.mods.refresh)
            self.host.log.info("Merge complete. Mod list refreshed.")
        else:
            self.host.log.warning("Merge complete, but refresh was not available.")


def register(host: Host) -> Plugin:
    return UnleashTheModsPlugin(host)
