# CZT Mod Manager — Dev UI Scanner (v2 API)
# Walks the main window's widget hierarchy in a QDialog tree.  Useful for
# discovering objectName()s and layouts when authoring UI plugins.
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QHBoxLayout,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
)

from plugins_ import Host, Plugin


def _widget_label(w):
    return f"{w.__class__.__name__}  ({w.objectName() or '<unnamed>'})"


def _layout_label(lay):
    return f"{lay.__class__.__name__}  ({lay.objectName() or '<unnamed>'})"


def _has_named_descendant(widget):
    for child in widget.children():
        if not hasattr(child, "objectName"):
            continue
        if child.objectName():
            return True
        if hasattr(child, "children") and _has_named_descendant(child):
            return True
    return False


def _add_widget_tree(parent_item, widget, show_unnamed):
    name = widget.objectName() or "<unnamed>"
    if not show_unnamed and name == "<unnamed>" and not _has_named_descendant(widget):
        return
    label = _widget_label(widget)
    w_item = QTreeWidgetItem(parent_item, [label])
    w_item.setData(0, Qt.ItemDataRole.UserRole, label)
    layout = widget.layout() if hasattr(widget, "layout") else None
    if layout is not None:
        layout_name = layout.objectName() or "<unnamed>"
        if show_unnamed or layout_name != "<unnamed>":
            ll = f"layout: {_layout_label(layout)}"
            li = QTreeWidgetItem(w_item, [ll])
            li.setData(0, Qt.ItemDataRole.UserRole, ll)
    for child in widget.children():
        if hasattr(child, "setLayout"):
            _add_widget_tree(w_item, child, show_unnamed)


class DevUiScanner(Plugin):
    def enable(self) -> None:
        self.host.hotkeys.register("Shift+U", self._open)
        self.host.ui.add_menu_item("Run UI Scanner", self._open)
        self._open()

    # --------------------------------------------------------------- dialog
    def _open(self) -> None:
        win = self.host.ui.main_window()
        if win is None:
            self.host.log.warning("UI not ready; cannot open scanner.")
            return

        dlg = QDialog(win)
        dlg.setWindowTitle("CZT UI Scanner")
        dlg.setMinimumSize(700, 500)
        dlg.setWindowFlags(dlg.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)

        layout = QVBoxLayout(dlg)
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        tree.setUniformRowHeights(True)
        tree.setIndentation(18)
        tree.setRootIsDecorated(False)
        tree.setStyleSheet(
            "QTreeWidget { background:#000; color:#e5e7eb; font-family:Consolas,'Segoe UI',Arial; "
            "font-size:14px; border:1px solid #2b2f33; border-radius:6px; }"
            "QTreeWidget::item { padding:2px 4px; }"
            "QTreeWidget::item:selected { background:#2c3e50; color:#fff; }"
        )

        opt_row = QHBoxLayout()
        cb_unnamed = QCheckBox("Show <unnamed>")
        cb_tabs = QCheckBox("Include tab refs")
        opt_row.addWidget(cb_unnamed)
        opt_row.addWidget(cb_tabs)
        opt_row.addStretch(1)
        layout.addLayout(opt_row)
        layout.addWidget(tree)

        btn_row = QHBoxLayout()
        b_refresh = QPushButton("Refresh")
        b_expand = QPushButton("Expand All")
        b_collapse = QPushButton("Collapse All")
        b_copy = QPushButton("Copy")
        b_close = QPushButton("Close")
        for b in (b_refresh, b_expand, b_collapse, b_copy, b_close):
            b.setMinimumWidth(120)
            btn_row.addWidget(b)
        layout.addLayout(btn_row)

        def build():
            tree.clear()
            targets = [("main_window", win)]
            if cb_tabs.isChecked():
                targets = [
                    ("main_menu_tab", getattr(win, "main_menu_tab", None)),
                    ("mod_manager_tab", getattr(win, "mod_manager_tab", None)),
                    ("main_window", win),
                ]
            for label, widget in targets:
                root = QTreeWidgetItem(tree, [label])
                if widget is None:
                    QTreeWidgetItem(root, ["<not available>"])
                    continue
                _add_widget_tree(root, widget, cb_unnamed.isChecked())
            tree.expandAll()

        def copy_tree():
            def walk(item, depth, lines):
                lines.append("  " * depth + item.text(0))
                for i in range(item.childCount()):
                    walk(item.child(i), depth + 1, lines)
            lines: list[str] = []
            for i in range(tree.topLevelItemCount()):
                walk(tree.topLevelItem(i), 0, lines)
            QApplication.clipboard().setText("\n".join(lines))
            self.host.log.info("Widget tree copied to clipboard.")

        b_refresh.clicked.connect(build)
        cb_unnamed.stateChanged.connect(lambda _s: build())
        cb_tabs.stateChanged.connect(lambda _s: build())
        b_expand.clicked.connect(tree.expandAll)
        b_collapse.clicked.connect(tree.collapseAll)
        b_copy.clicked.connect(copy_tree)
        b_close.clicked.connect(dlg.close)

        build()
        dlg.show()


def register(host: Host) -> Plugin:
    return DevUiScanner(host)
