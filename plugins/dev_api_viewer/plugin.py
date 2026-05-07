# CZT Mod Manager — Dev API Viewer (v2 API)
# Press Ctrl+L for the documented event catalog, Ctrl+I for a live host snapshot.
from __future__ import annotations

from plugins_ import Host, Plugin


class DevApiViewer(Plugin):
    def enable(self) -> None:
        self.host.hotkeys.register("Ctrl+L", self._dump_events)
        self.host.hotkeys.register("Ctrl+I", self._dump_host_info)
        self.host.events.on("profile_mode_changed", self._on_profile_mode_changed)
        self.host.events.on("toggle_path_mode", self._on_toggle_path_mode)
        self.host.events.on("config_saved", self._on_config_saved)
        self.host.log.info("Press Ctrl+L for known events, Ctrl+I for host snapshot.")

    # -------------------------------------------------------------- handlers
    def _on_profile_mode_changed(self, **kw):
        self.host.log.info(f"event profile_mode_changed: {kw}")

    def _on_toggle_path_mode(self, **kw):
        self.host.log.info(f"event toggle_path_mode: {kw}")

    def _on_config_saved(self, **kw):
        self.host.log.info(f"event config_saved: {kw}")

    # ----------------------------------------------------------------- dumps
    def _dump_events(self) -> None:
        events = self.host.events.known()
        if not events:
            self.host.log.info("No known events registered.")
            return
        self.host.log.info("Known events:")
        for name, doc in sorted(events.items()):
            self.host.log.info(f"  - {name}: {doc}")

    def _dump_host_info(self) -> None:
        sep = "=" * 60
        log = self.host.log.info
        log(sep)
        log(f"plugin id     : {self.host.id}")
        log(f"czt root      : {self.host.czt_root}")
        log(f"app version   : {self.host.app_version}")
        log(f"current profile: {self.host.profiles.current() or '<none>'}")
        engine = self.host.profiles.engine()
        log(f"engine spec   : {engine.display_name if engine else '<none>'}")
        log(f"checked mods  : {len(self.host.mods.checked())} / {len(self.host.mods.list())} total")
        log(f"plugin_data   : {dict(self.host.config.plugin_data())}")
        log(f"czt_root_folder cfg : {self.host.config.get('czt_root_folder')}")
        log(f"set_profile_path     : {self.host.config.get('set_profile_path')}")
        log(sep)


def register(host: Host) -> Plugin:
    return DevApiViewer(host)
