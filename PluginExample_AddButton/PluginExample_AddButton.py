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