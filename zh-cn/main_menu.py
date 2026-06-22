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

# Main tab storage stats labels
LBL_STORAGE_OVERVIEW = "[存储概览]"
LBL_STATS_DISK_USAGE_TOTAL = "磁盘使用量（总计）:"
LBL_STATS_DISK_USAGE_PROFILE = "磁盘使用量（当前配置文件）:"
LBL_STATS_MODS_ENABLED = "已启用模组:"
LBL_STATS_MODS_DISABLED = "已禁用模组:"
LBL_STATS_CORRUPTED = "损坏的模组:"
LBL_STATS_UPDATES_AVAILABLE = "可用更新:"

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
TIP_BROWSE_UNRAR = "若已安装，请选择 WinRAR.exe 或 UnRAR.exe 的路径。"
TIP_NEXUS_API = (
    "获取您的 Nexus Mods API Key\n"
    "将自动打开 Nexus 网站\n"
    "在打开的页面底部找到您的 Key"
)
MSG_API_KEY_SAVED_TITLE = "API Key已保存"
MSG_API_KEY_SAVED_TEXT = "Nexus API Key 已保存至配置文件."

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
    "storageOverviewBorderColorBtn": "存储概览边框颜色",
    "lineSeparatorColorBtn": "分隔线颜色",
    "selectedModBorderColorBtn": "选中模组边框颜色",
    "entryBorderColorBtn": "条目边框颜色",
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
    "okBtnDisplayColorBtn": "确认按钮颜色",
    "okBtnHoverColorBtn": "确认按钮悬浮颜色",
    "okBtnBorderColorBtn": "确认按钮边框颜色",
    "okBtnBorderHoverColorBtn": "确认按钮边框悬浮颜色",
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
    "以下设置控制 CZT 在安装过程中查找潜在替换文件时的严格程度。\n"
    "模组作者通常会在不同版本间轻微重命名文件，因此 CZT 会将新文件与您已有的文件进行比对，\n"
    "并在发现疑似匹配项时向您发出提示。\n"
    "完全匹配的文件名会自动替换。以下设置仅适用于文件名不同但仍相关的「近似匹配」场景。\n\n"
    "令牌重叠数：文件名中必须匹配的片段数量，达到该数量才会被视为候选替换文件。\n"
    "相似度阈值：控制匹配严格度——值越低显示更多候选项（范围更广但精度低），值越高显示更少候选项（精度更高，\n"
    "但设置过高可能错过有效更新）。\n\n"
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

# ===== Synced Missing Keys =====
LBL_BTN_PATCH_NOTES = "更新日志"
TIP_BTN_PATCH_NOTES = "查看 CZT 模组管理器更新日志并检查更新。"

LBL_STATS_MODS_ENABLED_VALUE_FMT = "磁盘占用：{size}"
LBL_STATS_MODS_DISABLED_VALUE_FMT = "磁盘占用：{size}"
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

LOG_CLEAN_EXE_TYPE_LINKS_REMOVED = "[{mod_type}] 已取消链接 {count} 个模组。"
LOG_CLEAN_TYPE_SYMLINKS_REMOVED = "[{mod_type}] 已取消链接 {count} 个模组。"
LOG_CLEAN_PER_FILE_REMOVE_FAILED_SUMMARY = "[清理] 移除失败：{count} 个模组符号链接。"
LOG_CLEAN_PER_FOLDER_LINKS_REMOVED = "[按文件夹] 已取消链接 {count} 个模组。"
LOG_CLEAN_PER_FOLDER_REMOVE_FAILED_SUMMARY = "[清理] 移除失败：{count} 个模组文件夹链接。"
LOG_CLEAN_ERRORS_OMITTED = "[清理] 另有 {count} 个错误未展示。"
LOG_CLEAN_CONTENT_LINKS_REMOVE_FAILED = "[清理] 无法移除内容模组链接：{error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED_SUMMARY = "[清理] 已移除配置文件 '{profile_name}' 的 {count} 个现有链接。"

