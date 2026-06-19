# CZT Mod Manager Plugin API v2 (Unified Reference)

This is the canonical plugin authoring reference for the v2 plugin system.

If you are migrating from older plugin scripts that used `run(plugin_api)` and
`Global_Plugin_API`, read the migration section below first.

## 1) v2 at a glance

- Plugins are discovered from folders under `CZT_ROOT/plugins/`.
- Each plugin folder must contain a `plugin.json` manifest.
- Your Python entry module must export `register(host) -> Plugin`.
- The returned plugin instance can implement lifecycle methods:
  - `enable()`
  - `disable()`
  - `unload()`

## 2) Folder layout

```text
CZT_ROOT/
  plugins/
    my_plugin/
      plugin.json
      plugin.py
      optional_asset.png
      optional_native.dll
```

Notes:

- Root-level legacy folders like `plugins/scripts` and
  `plugins/exe_standalone` are not required by v2 discovery.
- Keep all plugin assets next to your plugin module (or in subfolders inside
  your plugin folder).

## 3) Minimal plugin (working v2 example)

```python
from czt_plugins import Host, Plugin


class HelloPlugin(Plugin):
    def __init__(self, host: Host) -> None:
        super().__init__(host)

    def enable(self) -> None:
        self.host.log.info("HelloPlugin enabled")

    def disable(self) -> None:
        self.host.log.info("HelloPlugin disabled")


def register(host: Host) -> Plugin:
    return HelloPlugin(host)
```

## 4) Manifest (`plugin.json`)

`manifest_version` is currently `1`.

```json
{
  "manifest_version": 1,
  "id": "author.hello_plugin",
  "name": "Hello Plugin",
  "version": "1.0.0",
  "entry": "plugin.py",
  "author": "Your Name",
  "description": "Example plugin",
  "homepage": "https://example.com",
  "ui": false,
  "min_czt_version": "",
  "permissions": [],
  "native_lib": "",
  "native_abi": 0,
  "contributes": {
    "engines": []
  }
}
```

Required fields:

- `manifest_version` (int, must be `1`)
- `id` (non-empty string, no whitespace or path separators)
- `name` (non-empty string)
- `version` (non-empty string)
- `entry` (existing file path relative to plugin folder)

Optional fields:

- `ui` marks plugins that require the main window before load.
- `native_lib` requires a valid `native_abi`.
- `contributes.engines` supports engine-module registration.

Current implementation note:

- `contributes.menu_items` exists in manifest parsing but is not currently
  auto-applied by the loader. For menu entries, use `host.ui.add_menu_item(...)`.

## 5) Host API surface (what `host` provides)

The `host` object is the supported public contract.

- `host.id`: plugin id string
- `host.czt_root`: resolved CZT root path
- `host.app_version`: current app version string
- `host.log`: plugin-prefixed logging
- `host.events`: event bus namespace with ownership tracking
- `host.config`: config read/write plus per-plugin storage
- `host.profiles`: profile info and engine lookup
- `host.mods`: checked/all mods + refresh helper
- `host.ui`: UI helpers, styles, and Plugins dropdown integration
- `host.hotkeys`: hotkey registration
- `host.C`: native DLL loader

### 5.1 Logging

```python
self.host.log.info("message")
self.host.log.warning("warning")
self.host.log.error("error")
```

### 5.2 Config + plugin data

```python
# read
theme = self.host.config.get("theme", "default")

# update and persist
self.host.config.update({"my_key": 123})

# plugin-private storage
data = self.host.config.plugin_data()
data["run_count"] = int(data.get("run_count", 0)) + 1
self.host.config.save_plugin_data()
```

### 5.3 Profiles

```python
current = self.host.profiles.current()
all_profiles = self.host.profiles.all()
profile_cfg = self.host.profiles.get(current)
engine_spec = self.host.profiles.engine(current)
```

### 5.4 Mods

```python
mods_all = self.host.mods.list()
mods_checked = self.host.mods.checked()
self.host.mods.refresh()
```

### 5.5 UI integration

Main window + dropdown action:

```python
win = self.host.ui.main_window()
if self.host.ui.is_ready():
    self.host.ui.add_menu_item("Run My Action", self._run_action)
```

Style helpers for native-looking plugin widgets:

```python
btn_style = self.host.ui.button_style()
cb_style = self.host.ui.checkbox_style(font_size=13)
popup_btn_style = self.host.ui.popup_button_style()
```

Behavior notes:

- Menu actions added via `host.ui.add_menu_item` are auto-removed on plugin disable/unload.
- Single-action plugins appear as top-level entries; multi-action plugins are grouped.

### 5.6 Events

Subscribe, unsubscribe, emit:

```python
def _on_profile_changed(*args, **kwargs):
    self.host.log.info(f"profile_changed payload: {kwargs}")

self.host.events.on("profile_changed", _on_profile_changed)
self.host.events.emit("plugin_ready", plugin_id=self.host.id)
self.host.events.off("profile_changed", _on_profile_changed)
```

Known events are available from:

```python
known = self.host.events.known()
```

Documented event names (current):

- `profile_mode_changed`
- `toggle_path_mode`
- `config_saved`
- `mod_installed`
- `mod_uninstalled`
- `mod_enabled`
- `mod_disabled`
- `mod_list_refreshed`
- `profile_changed`
- `plugin_loaded`
- `plugin_unloaded`
- `app_shutdown`

### 5.7 Hotkeys

```python
self.host.hotkeys.register("Ctrl+Shift+M", self._run_action)
```

Hotkeys registered through `host.hotkeys` are tracked and cleaned up as part
of plugin teardown.

### 5.8 Native libraries

```python
lib = self.host.C.load(dll_path="path/to/my.dll", abi_version=1)
if lib is None:
    self.host.log.error("Native lib failed to load")
```

When loaded through `host.C`, native shutdown is called during teardown.

## 6) Lifecycle behavior

Loader flow:

1. Discover plugin folders containing `plugin.json`.
2. Validate manifest.
3. Import entry module.
4. Call `register(host)`.
5. Expect a `Plugin` instance.
6. Call `enable()` when activated.

Disable/unload flow:

- `disable()` is called when plugin is deactivated.
- Host teardown runs after disable:
  - event subscriptions are unbound
  - menu items are removed
  - hotkeys and native resources are torn down
- `unload()` is called before module removal.

## 7) UI plugins (`ui: true`)

Set `"ui": true` in your manifest if your plugin requires a ready main window
at load time.

Guidelines:

- Guard against missing UI anchors.
- Keep references to injected widgets so you can remove them if needed.
- Prefer `host.ui` helpers for styles and menu integration.
- Avoid deleting/reparenting host-owned widgets.

## 8) Migration from legacy `run(plugin_api)` plugins

Old model:

- Entry point: `run(plugin_api)`
- Imports like `czt_plugins.Global_Plugin_API`

New model:

- Entry point: `register(host) -> Plugin`
- Imports from `czt_plugins` (`Host`, `Plugin`, events/helpers as needed)

Minimal migration template:

```python
from czt_plugins import Host, Plugin


class MyPlugin(Plugin):
    def __init__(self, host: Host) -> None:
        super().__init__(host)

    def enable(self) -> None:
        self.host.log.info("enabled")

    def disable(self) -> None:
        self.host.log.info("disabled")


def register(host: Host) -> Plugin:
    return MyPlugin(host)
```

## 9) Troubleshooting checklist

- Plugin not discovered:
  - folder is under `CZT_ROOT/plugins/`
  - `plugin.json` exists and is valid JSON
- Plugin fails to load:
  - `entry` path exists
  - `register(host)` exists and returns a `Plugin`
- Plugin loads but no UI:
  - set `"ui": true` if main window is required
  - guard for missing UI references
- Event callback never fires:
  - verify event name via `host.events.known()`
  - confirm callback signature accepts emitted payload

## 10) Canonical imports

```python
from czt_plugins import Host, Plugin
```

Optional direct imports:

```python
from czt_plugins import KNOWN_EVENTS, PluginEventNamespace
```

Use `czt_plugins` as the stable public surface. Avoid relying on unrelated internal
modules unless there is no host API for your use case.
