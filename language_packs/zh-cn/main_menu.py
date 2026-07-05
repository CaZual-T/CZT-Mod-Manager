# Main Menu Tab - English strings

# General
STATUS_GAME_NOT_DETECTED = "未检测到游戏"

# Main tab button tooltips
TIP_BTN_GAME_BROWSE = "打开当前配置文件的模组文件夹，以及符号链接目标位置。"
TIP_BTN_OPEN_CUSTOM_SETTINGS = "启动选项和自定义设置。"
TIP_BTN_FIRST_TIME_SETUP = "创建根目录、安装 UnRAR、设置 API 密钥。"
TIP_BTN_SELECT_ALL = "[全选/取消全选]"
TIP_BTN_DELETE_SELECTED = (
    "从安装源文件夹中删除选中的模组。\n"
    "> 此操作不可撤销！（删除前会弹出警告提示）"
)
TIP_BTN_INSTALL_SELECTED = (
    "手动将选中的模组安装到当前配置文件。\n"
    "> 手动安装过程中不会保存元数据。\n"
    "   > 若安装的是新模组，安装后需打开管理标签页，\n"
    "   > 右键点击该文件并手动设置模组的 Nexus ID/URL，以便 CZT 检索并保存模组元数据。\n"
    "> 可安全安装已存在的模组以完成更新。\n"
)
TIP_PATH_MODE_MANUAL = (
    "已启用 = 用户可手动设置 EXE 文件路径，以及模组在启动时应链接到的位置。\n"
    "[重要] 选择此选项后，请阅读弹出的日志了解更多信息。"
)
TIP_PATH_MODE_STEAM = (
    "已启用（默认）= CZT 将利用您的 STEAM library.vdf 文件自动设置所有必要路径。\n"
    "点击「检测 Steam」使用自动路径配置。"
)
TIP_BTN_MANAGE_MODS = "加入 CZT 模组管理器 Discord 服务器获取更新和支持。"
TIP_BTN_CLEAN_MOD_LIST = (
    "4 个选项：\n"
    "- 删除当前配置文件的现有符号链接。\n"
    "- 删除崩溃监控日志。\n"
    "- 删除下载历史记录。\n"
    "- 移除模组列表文件中的失效条目。"
)
TIP_BTN_DONATIONS = "感谢您使用 CZT！\n点击此处打开捐赠页面（Paypal）"
TIP_BTN_UPDATE_CZT = (
    "点击此处打开 CZT 模组管理器使用指南。\n\n"
    "[快捷键]\n"
    "- 按下 SHIFT + H 显示可用快捷键。\n"
    "- 按下 F2 打开加载顺序菜单。"
)

# Main tab labels
LBL_PATH_MODE_MANUAL = "手动"
LBL_PATH_MODE_STEAM = "Steam"
TAB_TITLE_MAIN_MENU = "主菜单"

# Main tab button/section labels
LBL_PATH_MODES = "游戏路径"
LBL_BTN_DETECT_STEAM = "检测 Steam"
LBL_BTN_SAVE_CONFIG = "保存配置"
LBL_BTN_SET_INSTALL_DIRECTORY = "设置游戏安装目录"
LBL_BTN_SET_EXE_PATH = "设置游戏 EXE 路径"
LBL_BTN_LAUNCH_GAME = "启动游戏"
LBL_BTN_BROWSE = "浏览"
LBL_BTN_SETTINGS = "设置"
LBL_BTN_SETUP = "初始化"
LBL_BTN_GUIDE = "指南"
LBL_BTN_DISCORD = "Discord"
LBL_BTN_CLEAN = "清理"
LBL_BTN_DONATIONS = "捐赠"
LBL_BTN_PATCH_NOTES = "更新日志"
TIP_BTN_PATCH_NOTES = "查看 CZT 模组管理器更新日志并检查更新。"

# Main tab storage stats labels
LBL_STORAGE_OVERVIEW = "[存储概览]"
LBL_STATS_DISK_USAGE_TOTAL = "磁盘使用量（总计）:"
LBL_STATS_MODS_ENABLED = "已启用模组:"
LBL_STATS_MODS_DISABLED = "已禁用模组:"
LBL_STATS_MODS_ENABLED_VALUE_FMT = "磁盘占用：{size}"
LBL_STATS_MODS_DISABLED_VALUE_FMT = "磁盘占用：{size}"
LBL_STATS_UPDATES_AVAILABLE = "可用更新:"
LBL_STATS_APP_CPU_USAGE = "CZT - CPU 使用率："
LBL_STATS_APP_RAM_USAGE = "CZT - 内存使用："
LBL_STATS_NETWORK_SPEED = "网络速度："
LBL_STATS_DISK_RW_SPEED = "读取 | 写入速度："
LBL_STATS_DISK_TRANSFER_RATE = "传输速率："
LBL_STATS_UPDATES_VALUE_FMT = "扫描时间：{date}"
LBL_STATS_LAST_CHECKED_NEVER = "从未"
LBL_STATS_NETWORK_VALUE_FMT = "↑ {sent} | ↓ {recv}"
LBL_STATS_DISK_RW_VALUE_FMT = "读 {read} | 写 {write}"
LBL_STATS_DISK_TRANSFER_VALUE_FMT = "{total}"
LBL_STATS_UNAVAILABLE = "不可用"

TIP_STORAGE_OVERVIEW_CUSTOMIZE = "点击自定义 CZT 概览组件：可调整顺序或替换显示项。"
TIP_OVERVIEW_ITEM_UPDATES_AVAILABLE = "显示有可用更新的模组数量。\n ↳ scanned: (date) 为最近一次完整/自动扫描时间。"
TIP_OVERVIEW_ITEM_MODS_ENABLED = "当前配置文件已启用模组数量：\n ↳ 当前配置文件 enabled 模组文件夹总大小。"
TIP_OVERVIEW_ITEM_MODS_DISABLED = "当前配置文件已禁用模组数量：\n ↳ 当前配置文件 disabled 模组文件夹总大小。"
TIP_OVERVIEW_ITEM_DISK_USAGE_TOTAL = "CZT 根目录大小 / 承载该根目录的磁盘容量。"
TIP_OVERVIEW_ITEM_APP_CPU_USAGE = "CZT CPU 使用率 | 系统 CPU 使用率 | 当前 CPU 频率。"
TIP_OVERVIEW_ITEM_APP_RAM_USAGE = "CZT 内存占用 | 系统总内存。"
TIP_OVERVIEW_ITEM_NETWORK_SPEED = "系统实时上传与下载速度。"
TIP_OVERVIEW_ITEM_DISK_RW_SPEED = "所选磁盘（drive）实时读写速度。"
TIP_OVERVIEW_ITEM_DISK_TRANSFER_RATE = "所选磁盘（drive）实时读写总传输速率。"

DLG_TITLE_STORAGE_WIDGETS = "自定义 CZT 概览"
DLG_STORAGE_WIDGETS_DESC = "拖拽条目可调整顺序。勾选的行会显示在 CZT 概览中。"
LBL_STORAGE_WIDGETS_DRIVE_LABEL = "选择用于 R/W 与传输速率概览的磁盘："
LBL_STORAGE_WIDGETS_DRIVE_ALL = "全部"
BTN_STORAGE_WIDGETS_RESTORE_DEFAULT = "恢复默认"
BTN_STORAGE_WIDGETS_CANCEL = "取消"
BTN_STORAGE_WIDGETS_APPLY = "应用"
MSG_STORAGE_WIDGETS_NONE_SELECTED_TITLE = "未选择组件"
MSG_STORAGE_WIDGETS_NONE_SELECTED_BODY = "请至少选择一个要显示的组件。"
MSG_STORAGE_WIDGETS_TOO_MANY_TITLE = "组件过多"
MSG_STORAGE_WIDGETS_TOO_MANY_BODY = "该面板一次最多支持显示 {max_visible} 个组件。"

# Main tab setup popup titles
DLG_TITLE_CUSTOM_SETTINGS = "自定义设置"
DLG_TITLE_FIRST_TIME_SETUP = "首次初始化设置"

# Main tab log messages
LOG_ROOT_MISSING = (
    "\n❌ [错误] 根目录未设置/文件夹不存在！\n"
    "⚠️ [警告] 在创建根目录前，您尝试应用的任何设置都不会保存！\n"
    "❓ [提示] 点击上方的「初始化」按钮...\n"
    "  1: 点击「创建根目录」并选择您偏好的磁盘，以创建所需文件夹。\n"
    "  2: 创建根目录文件夹后，点击「安装 UnRAR」。\n"
    "    - 安装完成后，再次点击「安装 UnRAR」以设置其路径。\n"
    "  3: 安装 UnRAR.exe 后重启 CZT\n"
)

# Clean utility messages
MSG_ROOT_NOT_SET_CLEAN = "根目录未设置，无法清理模组列表。"
MSG_NO_VALID_INSTALL_DIR = (
    "No valid install directory set!\n \n- Path Mode [STEAM]:\n   > Click 'Detect Steam'\n "
    "\n- Path Mode [Manual]:\n   > Click 'SET INSTALL' and 'SET EXE' to configure."
)
LOG_CLEAN_HISTORY_CLEARED = "[清理] 已清空 {history_path} 中的历史记录。"
LOG_CLEAN_HISTORY_CLEAR_FAILED = "[清理] 无法清空 {history_path} 下的 {history_name}：{error}"
LOG_CLEAN_CRASH_LOG_CLEARED =  "[清理] 已清空崩溃监控日志：{log_path}"
LOG_CLEAN_CRASH_LOG_CLEAR_FAILED = "[清理] 无法清空 {log_path} 下的崩溃监控日志 {log_name}：{error}"
LOG_CLEAN_MOD_LIST_UPDATE_FAILED =  "[清理] 无法更新模组列表：{error}"
LOG_CLEAN_STALE_ENTRIES_REMOVED = "[清理] 已从配置文件 '{profile_name}' 的 mod_list.json 中移除 {removed} 条失效模组条目。"
LOG_CLEAN_NO_OPTIONS_SELECTED = "[清理] 未选择任何选项。"
LOG_PER_FILE_SYMLINK_DISABLED = "[按文件] 已禁用符号链接：{path}"
LOG_PER_FILE_SYMLINK_REMOVE_FAILED = "[按文件] 无法移除符号链接 {path}：{error}"
LOG_PER_FOLDER_LINK_DISABLED = "[按文件夹] 已禁用符号链接/连接点：{path}"
LOG_PER_FOLDER_LINK_REMOVE_FAILED = "[按文件夹] 无法移除符号链接/连接点 {path}：{error}"
LOG_LINK_MODS_JUNCTION_DISABLED =  "[链接] 已禁用 Mods 连接点：{path}"
LOG_LINK_MODS_SYMLINK_DISABLED = "[链接] 已禁用 Mods 符号链接：{path}"
LOG_LINK_MODS_SYMLINK_REMOVE_FAILED = "[链接] 无法移除 Mods 符号链接：{error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED = "[清理] 已移除配置文件 '{profile_name}' 的现有符号链接。"
LOG_CLEAN_EXE_TYPE_LINKS_REMOVED = "[{mod_type}] 已取消链接 {count} 个模组。"
LOG_CLEAN_TYPE_SYMLINKS_REMOVED = "[{mod_type}] 已取消链接 {count} 个模组。"
LOG_CLEAN_PER_FILE_REMOVE_FAILED_SUMMARY = "[清理] 移除失败：{count} 个模组符号链接。"
LOG_CLEAN_PER_FOLDER_LINKS_REMOVED = "[按文件夹] 已取消链接 {count} 个模组。"
LOG_CLEAN_PER_FOLDER_REMOVE_FAILED_SUMMARY = "[清理] 移除失败：{count} 个模组文件夹链接。"
LOG_CLEAN_ERRORS_OMITTED = "[清理] 另有 {count} 个错误未展示。"
LOG_CLEAN_CONTENT_LINKS_REMOVE_FAILED = "[清理] 无法移除内容模组链接：{error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED_SUMMARY = "[清理] 已移除配置文件 '{profile_name}' 的 {count} 个现有链接。"

# Clean options popup
DLG_TITLE_CLEAN_OPTIONS = "清理选项"
CLEAN_OPTIONS_PROMPT = "选择一个或多个选项："
CLEAN_OPTION_STALE_ENTRIES = "移除 mods_list.json 中的失效条目。"
CLEAN_OPTION_BROWSER_HISTORY = "删除本地 CZT 浏览器下载历史记录。"
CLEAN_OPTION_CRASH_LOGS = "删除崩溃监控日志。"
CLEAN_OPTION_SYMLINKS = "删除当前配置文件的现有符号链接。"
CLEAN_OPTIONS_APPLY = "应用"
CLEAN_OPTIONS_CANCEL = "取消"

# First-time setup popup
LBL_FTS_CREATE_ROOT = "创建根目录"
LBL_FTS_INSTALL_UNRAR = "安装 UnRAR"
LBL_FTS_NEXUS_API_KEY = "Nexus API  Key"
LBL_FTS_SAVE_KEY = "保存 Key"
LBL_FTS_SET_PATH = "设置路径"
LBL_FTS_OPEN_ROOT = "打开根目录"

TIP_CREATE_ROOT = (
    "点击「创建根目录」，然后选择您偏好的磁盘。\n"
    "CZT 将自动创建根目录文件夹并设置源路径。"
)
TIP_INSTALL_UNRAR = (
    "下载并安装 UnRAR.exe 以启用模组解压功能。\n"
    "安装路径 > 为 CZT 根目录选择的磁盘/CZT Mod Manager/czt_tools/UnRAR.exe \n"
    "注意：安装完成后，可再次点击此按钮自动检测其路径。"
)
TIP_BROWSE_UNRAR = (
    "设置位于电脑任意位置的 UnRAR.exe（或 WinRAR.exe）的路径。\n"
    "浏览到该文件，或将其完整路径粘贴到输入框中并按 Enter 保存。"
)
TIP_NEXUS_API = (
    "获取您的 Nexus Mods API Key\n"
    "将自动打开 Nexus 网站\n"
    "在打开的页面底部找到您的 Key"
)
MSG_API_KEY_SAVED_TITLE = "API Key已保存"
MSG_API_KEY_SAVED_TEXT = "Nexus API Key 已保存至配置文件."
MSG_UNRAR_PATH_INVALID_TITLE = "无效的 UnRAR 路径"
MSG_UNRAR_PATH_INVALID_TEXT = (
    "该路径未指向有效的 UnRAR.exe 或 WinRAR.exe。\n"
    "请浏览到该文件，或粘贴其完整路径并按回车。"
)

# Custom settings popup

SETTINGS_RESET_BUTTON_TEXT = "重置"
SETTINGS_FONT_BUTTON_VALUE_TEXT = "{label}: {value}"

# UI text overrides — maps widget objectName to display text
SETTINGS_UI_TEXT = {
    # Group headers
    "General_Settings": "常规设置",
    "groupBox": "高级设置",
    "startupGroup_2": "颜色选项",
    "startupGroup_3": "字体选项",
    # Color button labels
    "groupBoxBorderColorBtn": "日志框边框颜色",
    "logBoxBackgroundColorBtn": "日志框背景颜色",
    "storageOverviewBorderColorBtn": "存储概览边框颜色",
    "lineSeparatorColorBtn": "分隔线颜色",
    "selectedModBorderColorBtn": "选中模组边框颜色",
    "entryBorderColorBtn": "条目边框颜色",
    "entrySelectedBorderColorBtn": "选中条目边框颜色",
    "entryBorderHoverColorBtn": "条目边框悬浮颜色",
    "entryBackgroundColorBtn": "条目背景颜色",
    "descriptionBackgroundColorBtn": "描述背景颜色",
    "descriptionBorderColorBtn": "描述边框颜色",
    "installListBorderColorBtn": "安装列表边框颜色",
    "scrollbarHandleBgBtn": "滚动条滑块背景色",
    "scrollbarHandleHoverBgBtn": "滚动条滑块悬浮背景色",
    "scrollbarBorderBtn": "滚动条滑块边框颜色",
    "tabBgColorBtn": "标签页背景色",
    "tabHoverBgBtn": "标签页悬浮背景色",
    "tabSelectedBgBtn": "选中标签页背景色",
    "tabTextColorBtn": "标签页文字颜色",
    "tabHoverTextBtn": "标签页悬浮文字颜色",
    "tabSelectedTextColorBtn": "选中标签页文字颜色",
    "customTabBorderColorBtn": "窗口边框颜色",
    "modListBorderColorBtn": "模组列表边框颜色",
    "progressBarColorBtn": "进度条颜色",
    "customColorLogBoxTextBtn": "日志框文字颜色",
    "dropdownDisplayColorBtn": "下拉框显示颜色",
    "dropdownHoverColorBtn": "下拉框悬浮颜色",
    "dropdownBorderColorBtn": "下拉框边框颜色",
    "dropdownBorderHoverColorBtn": "下拉框边框悬浮颜色",
    "mainMenuVerticalBtnDisplayColorBtn": "主菜单垂直按钮颜色",
    "mainMenuVerticalBtnHoverColorBtn": "主菜单垂直按钮悬浮颜色",
    "mainMenuVerticalBtnBorderColorBtn": "主菜单垂直按钮边框颜色",
    "mainMenuVerticalBtnBorderHoverColorBtn": "主菜单垂直按钮边框悬浮颜色",
    "mainMenuHorizontalBtnDisplayColorBtn": "主菜单行按钮颜色",
    "mainMenuHorizontalBtnHoverColorBtn": "主菜单行按钮悬浮颜色",
    "mainMenuHorizontalBtnBorderColorBtn": "主菜单行按钮边框颜色",
    "mainMenuHorizontalBtnBorderHoverColorBtn": "主菜单行按钮边框悬浮颜色",
    "manageTopBtnDisplayColorBtn": "管理页顶部按钮颜色",
    "manageTopBtnHoverColorBtn": "管理页顶部按钮悬浮颜色",
    "manageTopBtnBorderColorBtn": "管理页顶部按钮边框颜色",
    "manageTopBtnBorderHoverColorBtn": "管理页顶部按钮边框悬浮颜色",
    "deleteBtnDisplayColorBtn": "删除按钮颜色",
    "deleteBtnHoverColorBtn": "删除按钮悬浮颜色",
    "deleteBtnBorderColorBtn": "删除按钮边框颜色",
    "deleteBtnBorderHoverColorBtn": "删除按钮边框悬浮颜色",
    "deleteBtnTextColorBtn": "删除按钮文字颜色",
    "deleteBtnTextHoverColorBtn": "删除按钮文字悬浮颜色",
    "saveBtnDisplayColorBtn": "保存按钮颜色",
    "saveBtnHoverColorBtn": "保存按钮悬浮颜色",
    "saveBtnBorderColorBtn": "保存按钮边框颜色",
    "saveBtnBorderHoverColorBtn": "保存按钮边框悬浮颜色",
    "saveBtnTextColorBtn": "保存按钮文字颜色",
    "saveBtnTextHoverColorBtn": "保存按钮文字悬浮颜色",
    "actionBtnDisplayColorBtn": "操作按钮颜色",
    "actionBtnHoverColorBtn": "操作按钮悬浮颜色",
    "actionBtnBorderColorBtn": "操作按钮边框颜色",
    "actionBtnBorderHoverColorBtn": "操作按钮边框悬浮颜色",
    "actionBtnTextColorBtn": "操作按钮文字颜色",
    "actionBtnTextHoverColorBtn": "操作按钮文字悬浮颜色",
    "okBtnDisplayColorBtn": "确认按钮颜色",
    "okBtnHoverColorBtn": "确认按钮悬浮颜色",
    "okBtnBorderColorBtn": "确认按钮边框颜色",
    "okBtnBorderHoverColorBtn": "确认按钮边框悬浮颜色",
    "okBtnTextColorBtn": "确认按钮文字颜色",
    "okBtnTextHoverColorBtn": "确认按钮文字悬浮颜色",
    "cancelBtnDisplayColorBtn": "取消按钮颜色",
    "cancelBtnHoverColorBtn": "取消按钮悬浮颜色",
    "cancelBtnBorderColorBtn": "取消按钮边框颜色",
    "cancelBtnBorderHoverColorBtn": "取消按钮边框悬浮颜色",
    "cancelBtnTextColorBtn": "取消按钮文字颜色",
    "cancelBtnTextHoverColorBtn": "取消按钮文字悬浮颜色",
    "launchGameBtnDisplayColorBtn": "启动游戏按钮颜色",
    "launchGameBtnHoverColorBtn": "启动游戏按钮悬浮颜色",
    "launchGameBtnBorderColorBtn": "启动游戏按钮边框颜色",
    "launchGameBtnBorderHoverColorBtn": "启动游戏按钮边框悬浮颜色",
    "launchGameBtnTextColorBtn": "启动游戏按钮文字颜色",
    "launchGameBtnTextHoverColorBtn": "启动游戏按钮文字悬浮颜色",
    "miscBtnTextColorBtn": "杂项按钮文字颜色",
    "miscBtnTextHoverColorBtn": "杂项按钮文字悬浮颜色",
    "miscBtnColorDisplayBtn": "杂项按钮显示颜色",
    "miscBtnColorHoverBtn": "杂项按钮悬浮颜色",
    "miscBtnColorBorderBtn": "杂项按钮边框颜色",
    "miscBtnBorderHoverColorBtn": "杂项按钮边框悬浮颜色",
    # Font button labels
    "customFontHeaderIBtn": "标签页字体",
    "customFontHeaderMBtn": "标签字体",
    "customFontLogBoxBtn": "日志框字体",
    "customFontLabelsBtn": "模组列表字体",
    "customFontTooltipBtn": "提示框字体",
    "customFontCbBtn": "复选框字体",
    "customFontButtonBtn": "按钮字体",
    "customFontMainMenuVerticalButtonsBtn": "主菜单左侧按钮字体",
    "customFontMainMenuTopButtonsBtn": "主菜单顶部按钮字体",
    "customFontManageTabButtonsBtn": "管理页按钮字体",
    # General labels / checkboxes
    "generalUseDownloadsAsSourceCheckBox": "将下载文件夹设为模组源目录。",
    "generalUseModsSourceAsSourceCheckBox": "将 mod_staging 文件夹设为模组源目录。",
    "generalUseBuiltInNexusBrowserCheckBox": "使用 CZT 自定义浏览器窗口打开模组链接。",
    "generalRegisterNxmHandlerCheckBox": "设置为「模组管理器下载」按钮的默认处理程序。",
    "generalUpdateOnlyEnabledModsCheckBox": "扫描时仅检查已启用模组的更新。",
    "generalDownloadModsAfterScanCheckBox": "自动下载标记为「有可用更新」的模组。",
    "generalDeleteAfterInstalledCheckBox": "模组安装完成后自动删除源压缩包。",
    "generalProtectEnabledModsFromDeletionCheckBox": "保护已启用模组不被删除。",
    "manageHomeCheckBox": "将「管理」设为默认标签页。",
    "installHomeCheckBox": "将「主菜单」设为默认标签页。",
    "enableCztBetaAlertsCheckBox": "启用 CZT 测试版更新提醒。",
    "scanUpdatesOnStartupCheckBox": "启动时扫描模组更新。",
    "updateScanCacheHoursLabel": "启动扫描频率（小时）：",
    "musicLabel": "曲目：",
    "menuMusicVolumeLabel": "音量：",
    "menuMusicCheckBox": "启用菜单背景音乐。",
    "pauseMenuMusicAfterLaunchCheckBox": "启动游戏后暂停菜单背景音乐。",
    "buttonHoverCheckBox": "启用按钮「悬浮」音效。",
    "buttonClickCheckBox": "启用按钮「点击」音效。",
    "languageLabel": "语言：",
    # Advanced labels / checkboxes
    "downloadParallelWorkersLabel": "最大同时下载数：",
    "backgroundThreadsLabel": "最大后台线程数：",
    "installLiveLogThresholdLabel": "实时进度日志阈值（MB）：",
    "installCacheSessionCheckBox": "缓存文件选择（仅本次会话）。",
    "installCachePersistentCheckBox": "缓存文件选择（持久化）。",
    "installCacheAutoClearCheckBox": "自动清理本地持久化缓存文件。",
    "installCacheMaxSizeLabel": "自动清理阈值（KB）：",
    "similarityPrimaryTokensLabel": "主匹配最小令牌重叠数：",
    "similarityPrimaryRatioLabel": "主匹配相似度阈值：",
    "generalEnableSecondaryInstallSafetyCheckBox": "启用二级安装安全校验。",
    "similaritySecondaryTokensLabel": "副匹配最小令牌重叠数：",
    "similaritySecondaryRatioLabel": "副匹配相似度阈值：",
    "saveButton": "保存",
}

SETTINGS_HELP_TEXT = (
    "以下设置控制 CZT 在安装过程中查找潜在替换文件时的严格程度。"
    "模组作者通常会在不同版本间轻微重命名文件，因此 CZT 会将新文件与您已有的文件进行比对，"
    "并在发现疑似匹配项时向您发出提示。\n"
    "完全匹配的文件名会自动替换。"
    "以下设置仅适用于文件名不同但仍相关的「近似匹配」场景。\n\n"
    "令牌重叠数：文件名中必须匹配的片段数量，达到该数量才会被视为候选替换文件。\n"
    "相似度阈值：控制匹配严格度——值越低显示更多候选项（范围更广但精度低），"
    "值越高显示更少候选项（精度更高，但设置过高可能错过有效更新）。\n\n"
    "二级安全校验为可选功能，可作为兜底检查，捕获主校验可能遗漏的边缘情况。"
)

TIP_REGISTER_NXM_HANDLER = (
    "启用后，点击模组页面上的「模组管理器下载」按钮时，文件将直接发送至 CZT 进行下载和安装。\n"
    "所有模组元数据会在安装时自动保存。\n"
    "- 支持所有 Nexus 账户类型（免费版和高级版）。\n"
    "除非您遇到 CZT 覆盖其他管理器下载的问题，否则请勿禁用此选项。"
)

TIP_OPEN_IN_APP_BROWSER = (
    "启用后，点击浏览、模组图片或链接图标时，将在 CZT 内置浏览器中打开 Nexus 页面。\n"
    "禁用后，所有链接将在您的默认外部浏览器中打开。"
)

TIP_INSTALL_LIVE_LOG_THRESHOLD = (
    "CZT 在日志框中显示实时安装进度的最小文件大小阈值。\n"
    "对于大文件，此设置可避免您误以为应用无响应。"
)

TIP_DOWNLOAD_PARALLEL_WORKERS = (
    "CZT 可同时运行的最大下载任务数。\n"
    "⚠️ 数值越高可加快批量下载速度，但可能导致程序不稳定。"
)

TIP_BACKGROUND_THREADS = (
    "后台线程数量限制。\n"
    "更新扫描/加载顺序/安装操作均受此设置影响。\n"
    "数值越高允许同时运行更多任务。\n"
    "⚠️ 数值越高可加快操作速度，但可能导致程序不稳定。"
)

TIP_UPDATE_SCAN_CACHE_HOURS = (
    "- 若您频繁重启应用且希望避免启动时全量扫描，可将此值设为更高（如 6）。\n"
    "- 若希望每次启动（或每次点击「检查所有模组更新」）时执行全量扫描，可将此值设为 0。\n"
    "- 此设置不影响「编辑模组条目」窗口中单个模组的更新检查频率。"
)

TIP_SAVE_SETTINGS = (
    "保存设置并应用更改。\n"
    "> 注意：部分设置需重启应用才能完全生效。"
)

# Reset button tooltips
TIP_RESET_LIVE_LOG_THRESHOLD = "将实时进度日志阈值重置为默认值。"
TIP_RESET_DOWNLOAD_WORKERS = "将最大同时下载数重置为默认值。"
TIP_RESET_BACKGROUND_THREADS = "将最大后台线程数重置为默认值。"
TIP_RESET_PRIMARY_TOKENS = "将主匹配令牌重叠数重置为默认值。"
TIP_RESET_PRIMARY_RATIO = "将主匹配相似度阈值重置为默认值。"
TIP_RESET_SECONDARY_TOKENS = "将副匹配令牌重叠数重置为默认值。"
TIP_RESET_SECONDARY_RATIO = "将副匹配相似度阈值重置为默认值。"

# Install cache tooltips
TIP_CACHE_SESSION = (
    "缓存已知压缩包的文件选择结果，直至 CZT 关闭。\n"
    "点击刷新可清除本次会话的缓存选择。"
)
TIP_CACHE_PERSISTENT = (
    "将压缩包的文件选择结果保存至文件，重启后仍保留。\n"
    "点击刷新可清除本地缓存文件。"
)
TIP_CACHE_AUTO_CLEAR = "启用后，当持久化缓存大小超过下方阈值时将自动清理。"
TIP_CACHE_MAX_SIZE = "触发自动清理的持久化缓存文件最大大小（KB）。"
TIP_CLEAR_SESSION_CACHE = "清除本次会话的文件选择缓存。"
TIP_CLEAR_PERSISTENT_CACHE = "清除持久化文件选择缓存。"
TIP_RESET_CACHE_SIZE_LIMIT = "将持久化缓存大小阈值重置为默认值。"

# Music dropdown fallback
DEFAULT_MUSIC_TRACK = "默认"

# Language dropdown
LBL_LANGUAGE = "语言："
TIP_LANGUAGE_DROPDOWN = (
    "选择 CZT 模组管理器的显示语言。\n"
    "可将额外语言包添加至根目录 > CZT Mod Manager/plugins/language_packs/ 目录。\n"
    "更改后需重启应用生效。"
)
MSG_LANGUAGE_RESTART = "语言已更改。请重启 CZT 模组管理器以完全生效。"

TIP_MENU_MUSIC_DROPDOWN = (
    "选择菜单背景音乐曲目。\n"
    "可将自定义曲目添加至根目录 > CZT Mod Manager/plugins/audio/menu_music 目录。\n"
    "支持格式：.mp3, .wav, .ogg"
)
TIP_BETA_ALERTS_RESET = "重置已关闭的测试版提醒，使最新测试版提示在启动时重新显示。"
TIP_INSTALL_CACHE_MAX_RESET = "将持久化缓存大小阈值重置为默认值。"
MSG_FONT_BLOCKED_TITLE = "字体被阻止"
MSG_FONT_BLOCKED_TEXT = "不允许使用字体 '{font_family}'。请选择其他字体。"
MSG_SETTINGS_SAVED_TITLE = "设置已保存"
MSG_SETTINGS_SAVED_CHANGED = "已更改以下设置："
MSG_SETTINGS_SAVED_NO_CHANGES = "未更改任何设置。"

# controls.py log/status strings
LOG_CONFIG_NOT_SAVED_NO_ROOT = "❌ [错误] 因未设置 czt_root_folder 导致配置未保存！\n    > 前往「用户设置」标签页并点击「创建根目录」"
DEFAULT_SET_PROFILE_PATH = "未设置，若使用手动路径模式请点击「设置安装目录」和「设置 EXE 路径」"
DEFAULT_STEAM_LIBRARY_PATH = "未设置，请点击「检测 Steam」"
DEFAULT_CURRENT_PROFILE = "未设置，请选择有效的配置文件。"
DEFAULT_EXE_NOT_FOUND = "未找到，\n    Steam 用户：点击「检测 Steam」，然后点击「启动游戏」\n    手动模式用户：点击「设置 EXE 路径」解决。"
LOG_SAVE_CONFIG_SUMMARY = (
    "[保存配置] 保存成功 ✓\n"
    "[配置速览]\n"
    "⇾ 当前配置文件：{current_profile}\n"
    "⇾ 路径模式：{profile_path_mode}\n"
    "⇾ 符号链接目标：{set_profile_path}\n"
    "⇾ 目标 EXE：{exe_path}"
)
LOG_AUTO_SAVE_NO_ROOT = "❌ [错误] 未设置 czt_root_folder。配置未保存！"
LOG_BROWSE_NO_ROOT = "\n[错误] 未设置根目录！点击「创建根目录」开始使用 CZT。\n"
LOG_PROFILE_MODS_FOLDER_NOT_FOUND = "[错误] 未找到配置文件模组文件夹：{profile_mods_path}"
LOG_DEST_FOLDER_NOT_FOUND = "[错误] 未找到目标文件夹。"
LOG_OPENED_INSTALL_AND_MODS = "已打开游戏安装目录和模组文件夹。"
LOG_SELECTED_PROFILE = "[配置文件] 已选择配置文件：{current_profile}"
LOG_PROFILE_FOLDER_WARN = "[配置文件][警告] 无法确保 '{current_profile}' 的配置文件文件夹存在：{error}"

# ============================================================
# Custom Profiles popup (F6)
# ============================================================
DLG_TITLE_CUSTOM_PROFILES = "自定义配置文件"
LBL_CUSTOM_PROFILES_TITLE = "自定义游戏配置文件"
LBL_CUSTOM_PROFILES_SUBTITLE = (
    "添加你自己的游戏。留空的字段将继承合理的引擎默认值。"
)
LBL_EDITING = "正在编辑："
LBL_PROFILE_NAME = "配置文件名称 *"
LBL_ENGINE = "引擎 *"
LBL_ENGINE_DESCRIPTION = "描述："
LBL_STEAM_APPID = "Steam App ID"
LBL_LAUNCH_EXE = "启动可执行文件"
LBL_GAME_PATH = "游戏模组路径"
LBL_NEXUS_LINK = "Nexus 游戏链接"
LBL_MOD_DIR_NAME = "模组文件夹名称"
LBL_ROUTING = "文件夹路由"
LBL_DEFAULT_MODS_DIR = "将模组直接放入配置文件根目录（不使用 'Mods' 子文件夹）"
OPT_NEW_PROFILE = "＋ 新建配置文件"
BTN_DELETE_PROFILE = "删除"
BTN_SAVE_PROFILE = "保存配置文件"
BTN_CLOSE = "关闭"

# Custom Profiles - input placeholders
PH_PROFILE_NAME = "例如：我的精彩游戏"
PH_STEAM_APPID = "Steam App ID（例如：1144200）"
PH_LAUNCH_EXE = "Game.exe"
PH_GAME_PATH = r"\My Game\Mods"
PH_NEXUS_LINK = "https://www.nexusmods.com/<game>/mods/"
PH_MOD_DIR_NAME = "Mods"
PH_ROUTING = "plugins=Plugins, config=Config"

# Custom Profiles - in-depth field tooltips
TIP_CP_PROFILE_SELECTOR = (
    "选择要编辑的配置文件。\n"
    "• '＋ 新建配置文件' 会打开一个空白表单以创建全新的游戏。\n"
    "• 选择现有配置文件会加载其值，以便编辑或删除。\n"
    "这里只显示你自己的自定义配置文件 --> 内置配置文件无法在此窗口\n"
    "编辑或删除。"
)
TIP_CP_PROFILE_NAME = (
    "游戏的显示名称，显示在配置文件下拉列表中（必填）。\n"
    "它也会成为 CZT 根目录下的真实文件夹名称，因此必须是\n"
    "有效的 Windows 文件夹名称。\n"
    "允许：字母、数字、空格、连字符、下划线。\n"
    "不允许：< > : \" / \\ | ? * ，以空格或句点结尾的名称，以及\n"
    "保留名称（CON、PRN、NUL、COM1…）。\n"
    "必须唯一 --> 不能与内置或其他自定义配置文件相同。"
)
TIP_CP_ENGINE = (
    "CZT 用于安装和链接此游戏模组的模组引擎（必填）。\n"
    "选择与你的游戏匹配的引擎（例如 Unreal Engine、Unity、Techland）。\n"
    "引擎会提供智能默认值（允许的文件类型、模组的链接方式），\n"
    "因此你很少需要修改下方的高级字段。\n"
    "此框下方的灰色文字概述所选引擎。"
)
TIP_CP_STEAM_APPID = (
    "游戏的 Steam App ID（可选，仅数字）。\n"
    "可在 Steam 商店 URL 中找到：store.steampowered.com/app/<APPID>/。\n"
    "CZT 用它通过你的 Steam 库自动定位游戏。\n"
    "非 Steam 游戏请留空 --> 你仍可在主菜单选项卡手动设置路径。\n"
    "此处的字母或符号在保存时会被拒绝。"
)
TIP_CP_LAUNCH_EXE = (
    "游戏的可执行文件，相对于游戏文件夹。\n"
    "示例：Game.exe 或 Binaries\\Win64\\Game.exe。\n"
    "用逗号分隔多个候选项 --> CZT 使用找到的第一个。\n"
    "由 '启动游戏' 按钮使用；如果你自己启动游戏，请留空。"
)
TIP_CP_GAME_PATH = (
    "用于帮助检测游戏模组文件夹的路径片段（Steam）。\n"
    "通常是安装路径的末尾，例如 \\My Game\\Mods。\n"
    "用逗号分隔多个候选项。\n"
    "这是检测提示，不是完整路径 --> 若需完全手动控制，请在保存后于\n"
    "主菜单选项卡设置游戏的安装路径。"
)
TIP_CP_NEXUS_LINK = (
    "此游戏的 Nexus Mods 页面。\n"
    "格式：https://www.nexusmods.com/<game>/mods/  其中 <game> 是该游戏在\n"
    "网站 URL 中显示的域名。\n"
    "为此配置文件启用应用内 Nexus 浏览器和 '在 Nexus 打开' 链接。"
)
TIP_CP_MOD_DIR_NAME = (
    "模组链接到的游戏端文件夹名称。\n"
    "常见值：Mods、Paks、source。留空时默认为 'Mods'。\n"
    "当勾选 '将模组直接放入配置文件根目录' 时忽略此项。\n"
    "如不确定，请保留默认值 --> 引擎通常会正确处理。"
)
TIP_CP_ROUTING = (
    "高级：将特定的顶级文件夹发送到不同的游戏端文件夹\n"
    "（可选）。\n"
    "- 格式：源=目标，用逗号分隔。示例：plugins=Plugins, config=Config。\n"
    "- 含义：模组内的 'plugins' 文件夹会链接到游戏的 'Plugins'\n"
    "文件夹，而不是普通的 Mods 文件夹。\n"
    "-除非你的游戏将插件等与普通模组分开，否则请留空。"
)
TIP_CP_DEFAULT_MODS_DIR = (
    "勾选后，模组会直接放入配置文件的根目录，而不是\n"
    "'Mods' 子文件夹。\n"
    "用于直接从游戏根目录加载模组的游戏。\n"
    "勾选后，上方的 '模组文件夹名称' 将被忽略。\n"
    "对于典型情况（模组位于专用的 Mods 文件夹），请不要勾选。"
)
TIP_CP_SAVE = (
    "验证并保存此配置文件。\n"
    "新配置文件会立即出现在配置文件下拉列表中；编辑会更新\n"
    "现有条目。\n"
    "保存到 CZT 根目录中的 custom_profiles.json。"
)
TIP_CP_DELETE = (
    "删除所选的自定义配置文件。\n"
    "这只会移除配置文件条目 --> 不会删除任何已安装的模组\n"
    "或磁盘上的文件。\n"
    "仅对你创建的自定义配置文件可用（非内置）。"
)
TIP_CP_CLOSE = (
    "关闭此窗口。\n"
    "表单中未保存的更改将被丢弃；已保存的配置文件会保留。"
)

# Custom Profiles - status / dialog messages
MSG_ENGINE_EXPERIMENTAL = (
    "⚠ 实验性引擎：未在真实游戏中测试。预计仅支持基本的文件"
    "部署（无特殊路由或加载顺序处理）。"
)
MSG_NO_ROOT_FOLDER = "请先设置你的 CZT 根目录（首次设置）。"
MSG_APPID_NUMERIC = "Steam App ID 必须为数字。"
DLG_TITLE_DELETE_PROFILE = "删除配置文件"
MSG_CONFIRM_DELETE_PROFILE = (
    "删除自定义配置文件 '{name}'？\n这不会删除任何已安装的模组。"
)

# Custom Profiles - validation / persistence messages
MSG_NAME_EMPTY = "配置文件名称不能为空。"
MSG_NAME_INVALID_CHARS = '名称不能包含以下任意字符：< > : " / \\ | ? *'
MSG_NAME_RESERVED = "'{name}' 是系统保留名称。"
MSG_NAME_TRAILING = "名称不能以空格或句点结尾。"
MSG_NAME_BUILTIN = "'{name}' 是内置配置文件名称；请另选一个。"
MSG_NAME_EXISTS = "已存在名为 '{name}' 的自定义配置文件。"
MSG_SELECT_ENGINE = "请为此配置文件选择一个引擎。"
MSG_UNKNOWN_ENGINE = "未知引擎：'{engine}'。"
MSG_SAVE_FAILED = "无法写入 custom_profiles.json（请检查文件夹权限）。"
MSG_PROFILE_SAVED = "配置文件 '{name}' 已保存。"
MSG_NOT_CUSTOM = "'{name}' 不是自定义配置文件。"
MSG_DELETE_UPDATE_FAILED = "无法更新 custom_profiles.json。"
MSG_PROFILE_DELETED = "配置文件 '{name}' 已删除。"

FORZATECH_DESC = (
    "用于 Forza Horizon 的松散文件覆盖引擎。模组是文件夹（而非 pak），"
    "带有覆盖原版内容的 'media' 树、附加的 'mediapc' 树，"
    "和/或诸如 version.dll 代理的根文件。CZT 按加载顺序将所有已启用的"
    "模组合并为一个覆盖层（顶部优先解决冲突），然后将其映射到"
    "游戏中，为每个顶级文件夹创建一个联接，并为每个根文件创建一个符号链接。"
    "在已存在真实原版文件夹处，按文件进行覆盖，并将其遮蔽的内容"
    "备份为 '.czt_orig'。"
)

TECHLAND_DESC = (
    "用于 Techland C-Engine（Dying Light 1/2、The Beast）的基于槽位的 .pak 引擎。"
    "加载顺序来自编号的 data##.pak 文件名，低槽位"
    "保留给游戏，高区间开放给模组。CZT 将"
    "每个模组的 .pak 符号链接到游戏的扁平资源文件夹，并将其重命名到"
    "空闲槽位。原生 .dll/.asi 插件链接在游戏 exe 旁边。没有"
    "Content 文件夹或独立音频 - 音频包含在 pak 内。"
)

UNREAL_DESC = (
    "用于 Unreal Engine 4/5 的 pak 引擎。处理旧版 .pak 以及 IoStore"
    " .utoc/.ucas 容器（以及签名 pak 游戏的 .sig 文件）。CZT 将"
    "pak 符号链接到游戏的模组文件夹（LogicMods、~mods 或 Mods），并按"
    "pakchunk 编号重命名以设置加载顺序。支持诸如 UE4SS 的 .dll/.asi 模组加载器"
    "链接到 exe，以及可选的 Wwise（.bnk/.wem）和 FMOD"
    "（.bank）音频。"
)

UNITY_DESC = (
    "用于 Unity 的模组加载器驱动引擎（BepInEx、MelonLoader、UnityModManager）"
    " - 加载器仍负责加载顺序，而非引擎。模组通常是 .dll 插件或"
    " .bundle/.unity3d 资源包。CZT 将 .dll 模组符号链接到加载器的"
    "模组文件夹，并将已知的顶级文件夹（例如 'plugins'）路由到其"
    "游戏根目录等效位置。可选的 FMOD/Wwise 音频；没有 pak 或 Content 文件夹"
    "的概念。"
)



