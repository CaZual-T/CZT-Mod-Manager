# CZT Mod Manager Plugin API Reference
This document summarizes what the core plugin API exposes and how to use the event signal helpers. All symbols here come from the main app; plugins should avoid importing from internal modules directly unless listed below.

## Quick start (short version)
1) Put this at the top of your plugin file:

```python
ui_plugin = False (or True for plugins that edit/add ui elements)
from plugins_.Global_Plugin_API import PluginContextAPI, czt_log
```

2) Make a `run(plugin_api)` function; the app calls it and passes `plugin_api`:

```python
def run(plugin_api: PluginContextAPI):
	plugin_api.czt_log("Hello from my plugin")
```

> The app passes one argument: the `PluginContextAPI` instance. We standardize on the name `plugin_api` to match the loader.

That is the minimum you need. See the Signal section for events and the UI reference for adding widgets: [._PLUGIN_API_UI_REFERENCE.md](._PLUGIN_API_UI_REFERENCE.md).

## What is `plugin_api`?
- `plugin_api` is the `PluginContextAPI` object the app creates for you and passes as the single argument to your plugin’s `run(...)`.
- In the loader it is built and stored as `plugin_api`: [plugins_/plugin_auto_loader.py#L63-L90](plugins_/plugin_auto_loader.py#L63-L90).
- `run_script_plugin` calls your `run(plugin_api)`: [plugins_/Global_Run_Plugins.py#L37-L78](plugins_/Global_Run_Plugins.py#L37-L78).
- We standardize on the name `plugin_api` so examples match what you see in the app; you can technically name the parameter anything, but sticking to `plugin_api` avoids confusion.

## Importing the API
Standard entry point:

```python
from plugins_.Global_Plugin_API import (
	PluginContextAPI,
	GAME_PROFILES,
	DEFAULT_CFG,
	load_cfg,
	save_cfg,
	czt_log,
	czt_log_synced,
	resource_path,
	import_czt_version_file,
	open_link,
	register_hotkey,
	convert_timestamp_to_readable_format,
	get_available_drives,
	os,
	sys,
	json,
	Path,
	datetime,
	Qt,
	QTimer,
	QIcon,
	QCheckBox,
	QPushButton,
	QLabel,
	QLineEdit,
	QComboBox,
	QDialog,
	QMessageBox,
	QVBoxLayout,
	QHBoxLayout,
	QGridLayout,
)
```
[NOTE:]
- `DEFAULT_CFG` is a baseline config dict; do not mutate it directly.
- `GAME_PROFILES` is a dict of supported game profiles.

## PluginContextAPI
`PluginContextAPI` gives a live handle to app state and utilities. It is typically instantiated by the host and passed into your plugin entrypoints.

### Constructor fields
- `cfg`: initial config dict (a live UI-backed dict when available).
- `game_profiles`: optional override for `GAME_PROFILES`.
- `app_version`: current app version string.
- `mod_manager_tab`: reference to the Mod Manager tab UI (if constructed).
- `user_setup_tab`: reference to the User Setup tab UI (if constructed).
- `profile_combo`: live profile combobox (optional).
- `main_app` / `main_window`: reference to the main window/app instance.
- `**kwargs`: anything extra is attached to the instance verbatim.

### Properties
- `current_profile`: resolves to the UI combobox value when available, otherwise `cfg['current_game_profile']` fallback.
- `cfg`: prefers live UI config (shared), falls back to `main_app.cfg`, then to disk reload when only a root path is known.
- `GAME_PROFILES`: returns the provided `game_profiles` or the global default.

### Attached utilities
Injected as instance attributes for convenience:

- Config helpers: `load_cfg`, `save_cfg`.
- Logging: `czt_log`, `czt_log_synced`.
- Paths/version: `resource_path`, `import_czt_version_file`.
- UX/helpers: `open_link`, `register_hotkey`, `convert_timestamp_to_readable_format`, `get_available_drives`.
	- `open_link(url)`: open a URL using the OS default browser.
	- `register_hotkey(combo, callback)`: register a global app hotkey (e.g., `"Ctrl+L"`) that calls `callback`.
	- `convert_timestamp_to_readable_format(ts)`: convert a timestamp to a readable string.
	- `get_available_drives()`: return a list of available drive roots on the system.
- Stdlib/UI: `os`, `sys`, `json`, `Path`, `datetime`, `Qt`, `QTimer`, `QIcon`, `QCheckBox`, `QPushButton`, 
`QLabel`, `QLineEdit`, `QComboBox`, `QDialog`, `QMessageBox`, `QVBoxLayout`, `QHBoxLayout`, `QGridLayout`.
- UI helpers: `plugin_api.ui_context` (styles + colors for consistent plugin UI).

### Common tasks (actual use)
```python
def run(plugin_api):
	# Log to the app log window
	plugin_api.czt_log("Plugin loaded")

	# Read config + profile
	cfg = plugin_api.cfg
	profile = plugin_api.current_profile

	# Save config changes
	cfg["my_plugin_flag"] = True
	plugin_api.save_cfg(cfg, cfg.get("czt_root_folder", ""))

	# Open a link
	plugin_api.open_link("https://example.com")
```

See the UI reference for styling helpers, layouts, and widget examples: [._PLUGIN_API_UI_REFERENCE.md](._PLUGIN_API_UI_REFERENCE.md).

## Optional cleanup hook: `on_unload()`
If your plugin adds UI elements, threads, or modifies in-memory state, define `on_unload()` to clean up. The Plugin Manager’s Unload button calls this (best-effort), then removes the module from memory.

```python
def on_unload():
	# Remove added UI, stop threads, disconnect signals, etc.
	pass
```

Notes:
- Unload cannot automatically undo changes made by a plugin.
- Use `on_unload()` to remove anything you added at runtime (widgets, profiles, signals, hotkeys, threads).

## Global Plugin Signal Bus
Plugins and the host can exchange events through the global event bus in `plugins_.Global_Plugin_Signal`.

### Available functions
- `connect_event(event_name, callback)`: subscribe a callable to an event.
- `cancel_event(event_name, callback)`: unsubscribe a callable.
- `emit_event_signal(event_name, *args, **kwargs)`: broadcast to all subscribers.
- `list_events()`: returns the current registry `{event_name: [callbacks...]}`.

### Example: listen and emit
```python
# signal_example.py

from plugins_.Global_Plugin_Signal import connect_event, emit_event_signal, cancel_event

def run(plugin_api):
	def on_mod_installed(mod_name, profile):
		plugin_api.czt_log(f"Mod installed: {mod_name} on profile {profile}")

	# Listen for an install event
	connect_event("mod_installed", on_mod_installed)

	# Emit a custom event
	emit_event_signal("plugin_ready", plugin_api.current_profile)

	# Later, if you want to stop listening
	# cancel_event("mod_installed", on_mod_installed)
```
