# ui_button_plugin.py
ui_plugin = True

from plugins_.Global_Plugin_API import PluginContextAPI, QPushButton, QSizePolicy, Qt

def run(plugin_api: PluginContextAPI):
    host = plugin_api.user_setup_tab
    if not host or not hasattr(host, "ui"):
        plugin_api.czt_log("UI not ready; skipping")
        return

    ui = getattr(host, "ui", None)
    layout = getattr(ui, "gridLayout_4", None)
    if layout is None:
        plugin_api.czt_log("Main menu toolbar layout not found; skipping")
        return

    if getattr(host, "_my_plugin_button_mainmenu", None):
        return  # already added

    btn = QPushButton("My Plugin Action")
    btn.setStyleSheet(plugin_api.ui_context.button_stylesheet())
    btn.setMinimumWidth(30)
    btn.setMaximumWidth(140)
    btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    btn.clicked.connect(lambda: plugin_api.czt_log("My button clicked"))

    layout.addWidget(btn, 0, 6, 1, 1, Qt.AlignmentFlag.AlignLeft)

    host._my_plugin_button_mainmenu = btn