# CZT Mod Manager Plugin UI Reference
This file focuses only on UI-related plugin guidance: styles, layouts, and safe widget injection.

## UI helpers (styles + colors)
- `plugin_api.ui_context.colors()`
- `plugin_api.ui_context.button_stylesheet()`
- `plugin_api.ui_context.checkbox_stylesheet(font_size=12)`
- `plugin_api.ui_context.user_setup_tab_stylesheet()`
- `plugin_api.ui_context.popup_dialog_stylesheet()`
- `plugin_api.ui_context.popup_button_stylesheet()`
- `plugin_api.ui_context.popup_textedit_stylesheet()`
- `plugin_api.ui_context.popup_frame_stylesheet()`

```python
def run(plugin_api):
    btn_style = plugin_api.ui_context.button_stylesheet()
    cb_style = plugin_api.ui_context.checkbox_stylesheet()
    colors = plugin_api.ui_context.colors()

    # Example: apply to a new button
    my_btn.setStyleSheet(btn_style)
```

### Popup styles (dialogs)
Use these for consistent dialog styling:

```python
def run(plugin_api):
    dialog_style = plugin_api.ui_context.popup_dialog_stylesheet()
    button_style = plugin_api.ui_context.popup_button_stylesheet()
    frame_style = plugin_api.ui_context.popup_frame_stylesheet()
```

## UI plugin surface (adding widgets)
- Mark UI plugins with `ui_plugin = True` so they load after the UI exists.
- Anchors you can attach to (if present): `plugin_api.user_setup_tab`, `plugin_api.mod_manager_tab`, or `plugin_api.main_window`.
- Grab a layout from the host: try `host.layout()` first; if your team exposes a specific layout attribute (e.g., `mainLayout`), use that. Add widgets; do not delete or reparent existing ones.
- Guard against duplicates (store a reference) and bail gracefully if no layout is available.

### Example: add a button to the User Setup tab
```python
# ui_button_plugin.py
ui_plugin = True

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from plugins_.Global_Plugin_API import PluginContextAPI

def run(plugin_api: PluginContextAPI):
    host = plugin_api.user_setup_tab or plugin_api.mod_manager_tab or plugin_api.main_window
    if not host:
        plugin_api.czt_log("UI not ready; skipping")
        return

  layout = None
  if plugin_api.user_setup_tab is not None:
    ui = getattr(plugin_api.user_setup_tab, "ui", None)
    if ui is not None and hasattr(ui, "gridLayout_2"):
      layout = ui.gridLayout_2
    elif hasattr(plugin_api.user_setup_tab, "path_mode_layout"):
      layout = plugin_api.user_setup_tab.path_mode_layout
  if layout is None and callable(getattr(host, "layout", None)):
    layout = host.layout()
  if layout is None:
    plugin_api.czt_log("No layout found on host; skipping")
    return

    if getattr(host, "_my_plugin_button", None):
        return  # already added

    btn = QPushButton("My Plugin Action")
    btn.setStyleSheet(plugin_api.ui_context.button_stylesheet())
    btn.clicked.connect(lambda: plugin_api.czt_log("My button clicked"))
  try:
    if hasattr(layout, "columnCount"):
      col = max(0, layout.columnCount())
      layout.addWidget(btn, 0, col, 1, 1, Qt.AlignLeft)
    else:
      layout.addWidget(btn, 0, Qt.AlignLeft)
  except TypeError:
    layout.addWidget(btn)
    host._my_plugin_button = btn
```

## Known layout anchors (current UI)
- User Setup tab (TabMainMenu):
  - Root layout: `plugin_api.user_setup_tab.layout()`.
  - Pathing menu layout: `plugin_api.user_setup_tab.path_mode_layout`.
  - Button row layout: `plugin_api.user_setup_tab.ui.gridLayout_2` (the bottom row containing `btnUpdateCZT`, `btnManageMods`, etc.).
  - Refresh profile list: `plugin_api.user_setup_tab.refresh_profile_dropdown()` (rebuilds the profile combobox).
  - Install logic (advanced): `plugin_api.user_setup_tab.install_logic`
    - Current staged mods list (source): `plugin_api.user_setup_tab.install_logic.mods_list`
    - Refresh staged mods list: `plugin_api.user_setup_tab.install_logic._refresh_mods_list()`
- Manage Mods tab:
  - Mods grid: `plugin_api.mod_manager_tab.mods_grid` (set from `ui.mods_grid`).
  - Progress bar layout: `plugin_api.mod_manager_tab.ui.progress_layout`.
  - Refresh manager list: `utilities_global._RefreshManagerWinList.RefreshManagerWinList.refresh_managerWin_list(...)` (refresh manager tab ui elements and mod list).
- Settings tab:
  - Not Ready.
