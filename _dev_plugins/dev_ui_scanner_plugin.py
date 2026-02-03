# CZT Mod Manager
# Developer tool: UI layout scanner. This will display the widget/layout hierarchy of the main window and tabs.

ui_plugin = True

from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QApplication, QCheckBox,)
from PyQt5.QtCore import Qt

from plugins_.Global_Plugin_API import PluginContextAPI

def _widget_label(widget):
    name = widget.objectName() or "<unnamed>"
    return f"{widget.__class__.__name__}  ({name})"


def _layout_label(layout):
    name = layout.objectName() or "<unnamed>"
    return f"{layout.__class__.__name__}  ({name})"


def _add_widget_tree(parent_item, widget, show_unnamed):
    name = widget.objectName() or "<unnamed>"
    if not show_unnamed and name == "<unnamed>":
        return
    label = _widget_label(widget)
    w_item = QTreeWidgetItem(parent_item, [label])
    w_item.setData(0, Qt.UserRole, label)
    # Layout attached to this widget
    layout = widget.layout() if hasattr(widget, "layout") else None
    if layout is not None:
        layout_name = layout.objectName() or "<unnamed>"
        if show_unnamed or layout_name != "<unnamed>":
            layout_label = f"layout: {_layout_label(layout)}"
            layout_item = QTreeWidgetItem(w_item, [layout_label])
            layout_item.setData(0, Qt.UserRole, layout_label)
    # Recurse into child widgets only
    for child in widget.children():
        if hasattr(child, "layout"):
            _add_widget_tree(w_item, child, show_unnamed)


def _build_tree(tree, plugin_api, show_unnamed, include_tabs):
    tree.clear()
    targets = [("main_window", plugin_api.main_window)]
    if include_tabs:
        targets = [
            ("user_setup_tab", plugin_api.user_setup_tab),
            ("mod_manager_tab", plugin_api.mod_manager_tab),
            ("main_window", plugin_api.main_window),
        ]
    for label, widget in targets:
        root = QTreeWidgetItem(tree, [label])
        root.setData(0, Qt.UserRole, label)
        if widget is None:
            QTreeWidgetItem(root, ["<not available>"])
            continue
        _add_widget_tree(root, widget, show_unnamed)
    tree.expandAll()


def run(plugin_api: PluginContextAPI):
    host = plugin_api.main_window or plugin_api.user_setup_tab or plugin_api.mod_manager_tab
    if host is None:
        plugin_api.czt_log("[UI Scanner][DEV] UI not ready; cannot open scanner")
        return

    dlg = QDialog(host)
    dlg.setWindowTitle("CZT UI Scanner")
    dlg.setMinimumSize(700, 500)
    dlg.setWindowFlags(dlg.windowFlags() & ~Qt.WindowContextHelpButtonHint)
    try:
        dlg.setStyleSheet(plugin_api.ui_context.popup_dialog_stylesheet())
    except Exception:
        pass

    layout = QVBoxLayout(dlg)
    tree = QTreeWidget()
    tree.setHeaderLabels(["Widget / Layout"])
    tree.setHeaderHidden(True)
    tree.setUniformRowHeights(True)
    tree.setAlternatingRowColors(False)
    tree.setIndentation(18)
    tree.setRootIsDecorated(False)
    tree.setExpandsOnDoubleClick(False)
    tree.itemClicked.connect(lambda item, _col: item.setExpanded(not item.isExpanded()) if item.childCount() > 0 else None)
    tree.setStyleSheet(
        "QTreeWidget { background: #000000; color: #e5e7eb; font-family: Consolas, 'Segoe UI', Arial; font-size: 15px;"
        " border: 1px solid #2b2f33; border-radius: 6px; }"
        "QTreeWidget::item { padding: 2px 4px; background: transparent; }"
        "QTreeWidget::item:selected { background: #2c3e50; color: #ffffff; }"
        "QTreeView::branch { background: transparent; }"
        "QTreeView::branch:hover { background: transparent; }"
        "QTreeView::branch:has-children { image: none; width: 0px; height: 0px; }"
        "QTreeView::branch:adjoins-item { background: transparent; }"
        "QTreeView::branch:closed, QTreeView::branch:open { background: transparent; }"
    )
    # Options row (above tree)
    options_row = QHBoxLayout()
    cb_show_unnamed = QCheckBox("Show <unnamed>")
    cb_show_unnamed.setChecked(False)
    cb_include_tabs = QCheckBox("Include tab refs")
    cb_include_tabs.setChecked(False)
    options_row.addWidget(cb_show_unnamed)
    options_row.addWidget(cb_include_tabs)
    options_row.addStretch(1)
    layout.addLayout(options_row)

    layout.addWidget(tree)

    btn_row = QHBoxLayout()
    btn_refresh = QPushButton("Refresh")
    btn_expand = QPushButton("Expand All")
    btn_collapse = QPushButton("Collapse All")
    btn_copy = QPushButton("Copy to Clipboard")
    btn_close = QPushButton("Close")
    for b in (btn_refresh, btn_expand, btn_collapse, btn_copy, btn_close):
        b.setMinimumWidth(140)
    try:
        btn_style = plugin_api.ui_context.button_stylesheet()
        for b in (btn_refresh, btn_expand, btn_collapse, btn_copy, btn_close):
            b.setStyleSheet(btn_style)
        cb_show_unnamed.setStyleSheet(plugin_api.ui_context.checkbox_stylesheet(font_size=13))
        cb_include_tabs.setStyleSheet(plugin_api.ui_context.checkbox_stylesheet(font_size=13))
    except Exception:
        pass
    btn_row.addWidget(btn_refresh)
    btn_row.addWidget(btn_expand)
    btn_row.addWidget(btn_collapse)
    btn_row.addWidget(btn_copy)
    btn_row.addStretch(1)
    btn_row.addWidget(btn_close)
    layout.addLayout(btn_row)

    def set_prefix(item, expanded):
        base = item.data(0, Qt.UserRole) or item.text(0)
        if item.childCount() == 0:
            item.setText(0, base)
            return
        prefix = "[−] " if expanded else "[+] "
        item.setText(0, f"{prefix}{base}")

    def update_prefixes(root_item):
        if root_item is None:
            return
        set_prefix(root_item, root_item.isExpanded())
        for i in range(root_item.childCount()):
            update_prefixes(root_item.child(i))

    def refresh():
        _build_tree(tree, plugin_api, cb_show_unnamed.isChecked(), cb_include_tabs.isChecked())
        for i in range(tree.topLevelItemCount()):
            update_prefixes(tree.topLevelItem(i))

    def copy_tree():
        def walk(item, depth=0, lines=None):
            if lines is None:
                lines = []
            lines.append("  " * depth + item.text(0))
            for i in range(item.childCount()):
                walk(item.child(i), depth + 1, lines)
            return lines
        lines = []
        for i in range(tree.topLevelItemCount()):
            lines.extend(walk(tree.topLevelItem(i), 0))
        QApplication.clipboard().setText("\n".join(lines))
        plugin_api.czt_log("[UI Scanner][DEV] Copied widget tree to clipboard")

    btn_refresh.clicked.connect(refresh)
    cb_show_unnamed.stateChanged.connect(lambda _state: refresh())
    cb_include_tabs.stateChanged.connect(lambda _state: refresh())
    btn_expand.clicked.connect(tree.expandAll)
    btn_collapse.clicked.connect(tree.collapseAll)
    btn_copy.clicked.connect(copy_tree)
    btn_close.clicked.connect(dlg.close)
    tree.itemExpanded.connect(lambda item: set_prefix(item, True))
    tree.itemCollapsed.connect(lambda item: set_prefix(item, False))

    refresh()
    tree.collapseAll()
    for i in range(tree.topLevelItemCount()):
        update_prefixes(tree.topLevelItem(i))
    dlg.show()
    plugin_api.czt_log("[UI Scanner][DEV] Opened UI scanner dialog")
    plugin_api.czt_log("[UI Scanner][DEV] Press Shift+U to reopen the scanner if closed.")
    # Hotkey to reopen if closed
    try:
        plugin_api.register_hotkey("Shift+U", lambda: run(plugin_api))
    except Exception:
        pass
