# CZT Plugin API v2 — Author Guide

## Plugin layout

Each plugin lives in its own folder under `<czt_root>/plugins/`:

```
<czt_root>/plugins/
  my_plugin/
    plugin.json     # required manifest
    plugin.py       # required entry module (exports `register(host)`)
    my_lib.dll      # optional native code (declared in plugin.json)
    README.md       # optional
```

A reference plugin lives in `.misc/plugin_examples/hello_czt/`.

## plugin.json schema (manifest_version 1)

| Field | Type | Required | Description |
|---|---|---|---|
| `manifest_version` | int | yes | Must be `1`. |
| `id` | string | yes | Reverse-DNS unique id, e.g. `"jane.tools.bulk_renamer"`. |
| `name` | string | yes | Display name shown in the Plugin Manager. |
| `version` | string | yes | Plugin version (semver-ish). |
| `entry` | string | yes | Path to the Python entry module, relative to the plugin folder. |
| `author` | string | no | Plugin author. |
| `description` | string | no | One-line summary shown in the Plugin Manager. |
| `homepage` | string | no | URL. |
| `ui` | bool | no | If `true`, plugin needs the main window — loaded after UI is ready. |
| `min_czt_version` | string | no | Refuse to load on older CZT (reserved). |
| `permissions` | string[] | no | Reserved for future sandboxing. |
| `native_lib` | string | no | DLL filename (relative to plugin folder). |
| `native_abi` | int | required when `native_lib` is set | Must be `1`. |
| `contributes.engines` | string[] | no | List of `"submodule:ClassName"` engine handlers to register. |
| `contributes.menu_items` | object[] | no | Reserved — declarative menu entries. |

## Python entry module

The entry module **must** define:

```python
from plugins_ import Host, Plugin

class MyPlugin(Plugin):
    def enable(self):  ...
    def disable(self): ...
    def unload(self):  ...

def register(host: Host) -> Plugin:
    return MyPlugin(host)
```

## Host API surface

The single `host` argument is the only thing your plugin should touch from
CZT internals. Anything outside `host.*` is unsupported and may change.

| Namespace | Purpose |
|---|---|
| `host.id` | Your plugin id (from manifest). |
| `host.czt_root` | Absolute path to the CZT root folder. |
| `host.app_version` | Current CZT version string. |
| `host.log` | `info(msg)` / `warning(msg)` / `error(msg)`. |
| `host.events` | `on(event, cb)`, `off(...)`, `emit(...)`, `known()`. |
| `host.config` | `get(key, default)`, `update(patch)`, `plugin_data()`, `save_plugin_data()`. |
| `host.profiles` | `current()`, `all()`, `get(name)`, `engine(name=None)`. |
| `host.mods` | `list()`, `checked()`, `refresh()`. |
| `host.ui` | `main_window()`, `is_ready()`, `add_menu_item(label, cb)`, style helpers. |
| `host.hotkeys` | `register(key, cb)`. |
| `host.native` | `load(dll_path, abi_version=1)`. |

### Documented events

Subscribe via `host.events.on(name, callback)`. Callbacks receive `**kwargs`
matching the documented payload. Full list: see
[plugins_/events.py](../../plugins_/events.py) `KNOWN_EVENTS`.

### Per-plugin storage

Use `host.config.plugin_data()` to get a dict scoped to your plugin id.
Mutate it in place and call `host.config.save_plugin_data()` to persist.
Stored under `cfg["plugin_data"][<your_id>]`.

## Lifecycle

1. **discover** — manifest loaded from disk.
2. **load**     — entry module imported, `register(host)` called.
3. **enable**   — `Plugin.enable()` called.
4. **disable**  — `Plugin.disable()` called; `host.events`, `host.ui`,
   `host.hotkeys`, `host.native` registrations are auto-removed.
5. **unload**   — `Plugin.unload()` called; module removed from `sys.modules`.

A crash in any step auto-disables the plugin and surfaces the error in the
Plugin Manager dialog.

## Shipping a native DLL

1. Implement the C ABI defined in
   [.misc/plugin_examples/czt_plugin.h](czt_plugin.h).
2. Compile to a Windows DLL exporting `czt_plugin_init` and
   `czt_plugin_shutdown`.
3. Reference it in `plugin.json`:
   ```json
   "native_lib": "my_plugin.dll",
   "native_abi": 1
   ```
4. Load it from your Python `enable()`:
   ```python
   def enable(self):
       lib = self.host.native.load("my_plugin.dll", abi_version=1)
       if lib is None:
           self.host.log.error("native lib failed to load")
   ```
5. The library is automatically `czt_plugin_shutdown`'d when the plugin is
   disabled or unloaded.

## Shipping a custom game engine

Drop an engine handler module next to `plugin.py` and reference it:

```json
"contributes": {
  "engines": ["godot_engine:GodotEngine"]
}
```

Your `godot_engine.py` looks like a built-in engine module:

```python
from utilities_global.engines.engine_base import EngineBase, EngineSpec
from utilities_global.engines.registry import register_engine

@register_engine
class GodotEngine(EngineBase):
    ENGINE_ID = "Godot"
    SPEC = EngineSpec(
        display_name="Godot",
        aliases=frozenset({"godot", "godot4"}),
        family="godot",
        mod_extensions=frozenset({".pck", ".gdextension", ".gd"}),
        # ...
    )
```

Profiles can then opt in with `"engine": "godot"`.

## Migrating from the v1 API

The legacy `plugins_.Global_Plugin_API.PluginContextAPI`, `Global_Run_Plugins`,
`F3_Menu`, and `plugin_auto_loader` modules are **gone**. Old `.py`, `.bat`,
and `.exe` plugins are no longer loaded. Rewrite as a v2 plugin:

| Legacy concept | v2 replacement |
|---|---|
| `def run(context):` | `class MyPlugin(Plugin): def enable(self): ...` + `register(host)` |
| Top-level `ui_plugin = True` | `"ui": true` in plugin.json |
| `context.cfg`, `context.czt_log` | `host.config.get(...)`, `host.log.info(...)` |
| Direct Qt class imports from `plugins_.Global_Plugin_API` | Import Qt directly from `PySide6` |
| `connect_event(...)` (module level) | `host.events.on(...)` |
| `cfg["startup_enabled_plugins"]` | `cfg["plugin_autoload"]` |
| `cfg["global_enabled_plugins"]` | `cfg["plugin_enabled_global"]` |
| `cfg["profile_enabled_plugins"]` | `cfg["plugin_enabled_per_profile"]` |
