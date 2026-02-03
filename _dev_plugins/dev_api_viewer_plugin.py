"""
Plugin: event_dev_tool.py
Description: All-in-one developer tool for CZT Mod Manager plugins.
"""

ui_plugin = True

from plugins_.Global_Plugin_Signal import connect_event, cancel_event, list_events

_HANDLERS = {}
_HOTKEYS_REGISTERED = False


def _log(plugin_api, msg):
    plugin_api.czt_log_synced(f"[DEV TOOL] {msg}")


def _make_handlers(plugin_api):
    def on_profile_mode_changed(current_profile, mode):
        _log(plugin_api, f"profile_mode_changed: Profile={current_profile}, Mode={mode}")

    def on_toggle_path_mode(mode_name=None, state=None, **_kwargs):
        _log(plugin_api, f"toggle_path_mode: Mode={mode_name}, State={state}")

    def on_config_saved(summary):
        _log(plugin_api, f"config_saved:\n{summary}")

    return {
        "profile_mode_changed": on_profile_mode_changed,
        "toggle_path_mode": on_toggle_path_mode,
        "config_saved": on_config_saved,
    }


def _register_handlers(plugin_api):
    global _HANDLERS
    try:
        for event_name, handler in _HANDLERS.items():
            try:
                cancel_event(event_name, handler)
            except Exception:
                pass

        _HANDLERS = _make_handlers(plugin_api)
        for event_name, handler in _HANDLERS.items():
            connect_event(event_name, handler)
    except Exception as e:
        _log(plugin_api, f"Error initializing event handlers: {e}")


def _print_listeners(plugin_api):
    events = list_events()
    if not events:
        _log(plugin_api, "No event listeners are currently registered.")
        return
    _log(plugin_api, "Event Bus Listeners:")
    for event, handlers in events.items():
        for idx, handler in enumerate(handlers, 1):
            handler_name = getattr(handler, "__name__", str(handler))
            handler_module = getattr(handler, "__module__", "unknown")
            _log(plugin_api, f"  - {event} [{idx}]: {handler_name} (module: {handler_module})")


def _print_plugin_api_info(plugin_api):
    sep = "=" * 70

    def section(title):
        return f"\n{sep}\n[DEV TOOL] {title}\n{sep}"

    cfg = getattr(plugin_api, "cfg", {})
    game_profiles = getattr(plugin_api, "GAME_PROFILES", {})
    current_game = cfg.get("current_game_profile")
    out = []

    out.append(section("Current Game/Profile Info"))
    out.append(f"Current Game/Profile: {current_game}")
    profile_info = game_profiles.get(current_game, {})
    if profile_info:
        out.append(f"  Mod Folder(s): {profile_info.get('path')}")
        out.append("  Allowed File Types:")
        out.append(f"    .pak: {profile_info.get('allow_file_type_pak', False)}")
        out.append(f"    .dll: {profile_info.get('allow_file_type_dll', False)}")
        out.append(f"    .asi: {profile_info.get('allow_file_type_asi', False)}")
        out.append(f"  Launch Executable(s): {profile_info.get('launch_exe')}")
        out.append(f"  Steam AppID: {profile_info.get('steam_appid')}")
        out.append(f"  Nexus Link: {profile_info.get('nexus_game_link')}")
    else:
        out.append("  [No profile info found]")

    out.append(section("Paths"))
    out.append(f"Root Folder: {cfg.get('czt_root_folder')}")
    out.append(f"Mods Source Folder: {cfg.get('czt_source_folder')}")
    out.append(f"UnRAR Tool Path: {cfg.get('unrar_path')}")
    out.append(f"Steam Library Path(s): {cfg.get('steam_library_path')}")

    out.append(section("Utility Functions & New API"))
    util_funcs = [
        "czt_log_synced(msg)",
        "save_cfg(cfg)",
        "load_cfg(path)",
        "resource_path(rel_path)",
        "import_czt_version_file()",
        "open_link(url)",
        "register_hotkey(key_sequence, callback)",
        "convert_timestamp_to_readable_format(ts)",
        "get_available_drives()",
        "limit_game_profile_text(text, max_len=13)",
        "ui_context.popup_dialog_stylesheet()",
        "ui_context.popup_button_stylesheet()",
        "ui_context.popup_frame_stylesheet()",
    ]
    out.append("Available utility functions for plugins:")
    for f in util_funcs:
        out.append(f"  - {f}")
    out.append("")
    out.append("Examples:")
    out.append("  plugin_api.czt_log_synced('Hello from my plugin!')")
    out.append("  cfg = plugin_api.cfg; cfg['my_plugin_setting'] = True; plugin_api.save_cfg(cfg)")
    out.append("  new_cfg = plugin_api.load_cfg('D:/CZT Mod Manager')")
    out.append("  icon_path = plugin_api.resource_path('resources_/img_/app_icon.ico')")
    out.append("  version = plugin_api.import_czt_version_file()")
    out.append("  plugin_api.open_link('https://nexusmods.com')")
    out.append("  plugin_api.register_hotkey('Ctrl+Shift+M', lambda: print('Hotkey!'))")
    out.append("  readable = plugin_api.convert_timestamp_to_readable_format(1700000000)")
    out.append("  drives = plugin_api.get_available_drives()")
    out.append("  short_name = plugin_api.limit_game_profile_text('Dying Light 2', max_len=8)")
    out.append("  dialog_css = plugin_api.ui_context.popup_dialog_stylesheet()")
    out.append("  btn_css = plugin_api.ui_context.popup_button_stylesheet()")
    out.append("  frame_css = plugin_api.ui_context.popup_frame_stylesheet()")

    out.append(section("Minimal Config (Relevant Settings)"))
    minimal_keys = [
        "czt_root_folder",
        "current_game_profile",
        "user_enabled_plugins",
        "steam_library_path",
        "set_profile_path",
    ]
    for k in minimal_keys:
        out.append(f"- {k}: {cfg.get(k)}")
    out.append("")
    out.append("Examples:")
    out.append("  root = plugin_api.cfg['czt_root_folder']")
    out.append("  profile = plugin_api.cfg['current_game_profile']")
    out.append("  plugins = plugin_api.cfg['user_enabled_plugins']")
    out.append("  steam_libs = plugin_api.cfg['steam_library_path']")
    out.append("  profile_path = plugin_api.cfg['set_profile_path']")
    out.append(f"\n{sep}\n[DEV TOOL] plugin_api Quick Reference Complete\n{sep}\n")

    plugin_api.czt_log("\n".join(out))


def _register_hotkeys(plugin_api):
    global _HOTKEYS_REGISTERED
    if _HOTKEYS_REGISTERED:
        return
    plugin_api.register_hotkey("Ctrl+L", lambda: _print_listeners(plugin_api))
    plugin_api.register_hotkey("Ctrl+I", lambda: _print_plugin_api_info(plugin_api))
    _HOTKEYS_REGISTERED = True


def run(plugin_api):
    plugin_api.czt_log("[DEV TOOL] Press Ctrl+L to list event listeners, Ctrl+I for plugin API info.")
    _register_handlers(plugin_api)
    _register_hotkeys(plugin_api)
