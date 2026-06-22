# Utilities Global - English strings

# ===== basic_global_utilities.py =====
LOG_WARN_NO_ROOT_SAVE = "⚠️  [警告] 无法保存配置，因为 czt_root_folder 目录不存在。"
LOG_UNRAR_NOT_FOUND = "[UNRAR] 未找到可用的 UnRAR 工具。请在设置中配置 'unrar_path' 或安装 WinRAR（需包含 UnRAR.exe）。"
DLG_TITLE_SELECT_DRIVE = "选择驱动器"
LBL_SELECT_DRIVE = "为模组管理器文件夹选择驱动器:"
BTN_OK = "确定"
BTN_CANCEL = "取消"

# ===== CheckForCZTUpdates.py =====
WELCOME_MESSAGE = (
    "🔄️自动安装模组:\n"
    "- 从Nexus网站下载模组（点击「模组管理器下载」按钮）。\n"
    "- 操作后会触发CZT，程序将自动处理安装并保存模组信息。\n"
    "- 若没有「模组管理器下载」按钮，请从GitHub下载CZT扩展插件\n"
    "- 该扩展插件可让「手动下载」按钮实现「模组管理器下载」按钮的功能。\n\n"
    "🛠️ 手动安装模组:\n"
    "- 将模组文件拖拽至本日志框，即可将其加入安装队列\n"
    "- 从列表中选中模组，点击右上角的 ➡️ 按钮继续安装流程。\n\n"
    "💡[提示]\n"
    "- 大部分UI元素都配有提示文本，将鼠标悬停在按钮或其他UI元素上即可查看。 \n"
    "- 按下 SHIFT + H 显示所有可用快捷键。\n"
    "- 按下 F2 打开加载顺序菜单。\n"
)
DLG_TITLE_BETA_AVAILABLE = "测试版可用"
DLG_TITLE_UPDATE_AVAILABLE = "更新可用"
LBL_BETA_AVAILABLE ="发现新版 CZT 测试版！"
LBL_UPDATE_AVAILABLE = "发现新版 CZT 模组管理器！"
LBL_VERSION_INFO = "当前版本：{local_version}\n最新版本：{latest_version}"
BTN_DOWNLOAD_INSTALL = "下载并安装（{tag}）"
BTN_DISMISS = "忽略"
DLG_TITLE_UPDATE_ERROR = "更新错误"
MSG_UPDATE_ERROR = "下载或运行安装程序失败:\n{error}"
MSG_NO_RELEASE_NOTES = "该更新渠道未找到更新日志。"
MSG_RELEASE_NOTES_ERROR = "获取更新日志失败: {error}"

# ===== load_order.py =====
DLG_TITLE_LOAD_ORDER = "加载顺序"
MSG_LOAD_ORDER_NO_PROFILE = "无法识别当前配置文件。"
MSG_LOAD_ORDER_NO_PROFILE_SET = "未设置当前配置文件。"
MSG_LOAD_ORDER_PROFILE_NOT_FOUND = "未找到配置文件：{profile_name}"
MSG_LOAD_ORDER_MODS_DIR_MISSING = " 对应的模组目录不存在: {profile_name}"
DLG_TITLE_SET_LOAD_ORDER = "设置加载顺序 - {profile_name}"
DLG_TITLE_SAVE = "保存"
MSG_LOAD_ORDER_SAVED = "加载顺序保存成功。"
DLG_TITLE_ERROR_SAVING = "保存失败"
MSG_LOAD_ORDER_SAVE_FAILED = "加载顺序保存失败:\n{error}"

# ===== popup_policies.py =====
POPUP_TITLE_CUSTOM_SETTINGS ="自定义设置"
POPUP_TITLE_MANAGE_LOADOUTS = "管理配置集"
POPUP_TITLE_FIRST_TIME_SETUP ="首次运行设置"
POPUP_TITLE_RESTORE_BACKUP =  "恢复备份"
POPUP_TITLE_FORCE_UPDATE_OPTIONS ="强制更新选项"
POPUP_TITLE_CLEAN_OPTIONS = "清理选项"

# ===== UserSetup_Actions.py =====
DLG_TITLE_NO_DRIVES = "无可用驱动器"
MSG_NO_DRIVES ="未检测到可用驱动器。"
DLG_TITLE_NO_ROOT_FOLDER ="无根目录"
MSG_NO_ROOT_FOLDER = "CZT 根目录未设置或不存在。"
DLG_TITLE_ROOT_CREATED = "根目录已创建"
MSG_ROOT_CREATED = "CZT 根目录已创建于：{czt_root_folder}"
DLG_TITLE_SELECT_UNRAR = "选择 UnRAR 可执行文件"
MSG_UNRAR_INSTALLER_PROMPT = (
    "即将启动 UnRAR 安装程序。\n"
    "请将安装目录设置为:\n"
    " > 所选根驱动器\\CZT Mod Manager\\czt_tools <"
)
LOG_UNRAR_INSTALLER_LAUNCHED = (
    "UnRAR 安装程序已启动，请完成安装流程。\n"
    " 解压过程完成后即代表安装结束!"
)

# ===== backups/mod_backup.py =====
DLG_TITLE_CREATE_BACKUP = "创建备份"
MSG_BACKUP_ROOT_NOT_SET = "根目录未配置。"
MSG_BACKUP_CHOOSE = "选择备份内容:"
BTN_BACKUP_MOD_FILES = "仅备份模组文件"
BTN_BACKUP_MODS_LIST = "仅备份 mods_list.json"
BTN_BACKUP_FILES_AND_LIST = "备份文件 + 列表"
MSG_BACKUP_SUCCESS = "备份创建成功。\n\n"
MSG_BACKUP_WARNINGS = "备份已完成，但存在警告。\n\n"
MSG_BACKUP_FAILED = "备份失败。\n\n"

# ===== backups/restore_backup.py =====
DLG_TITLE_RESTORE_BACKUP = "恢复备份"
MSG_RESTORE_ROOT_NOT_SET = "根目录未配置。"
MSG_RESTORE_BACKUPS_NOT_FOUND = "未找到备份文件夹：{backup_root}"
LBL_RESTORE_HEADER = "选择要恢复或删除的备份文件夹"
LBL_NO_BACKUPS = "未找到备份"
LBL_BACKUP_META = "包含: {kind_text}   |   创建时间: {stamp}"
MSG_RESTORE_SELECT_ONE = "请选择一个备份进行安装。"
MSG_RESTORE_ONLY_ONE = "安装操作仅支持同时选中一个备份"
MSG_RESTORE_SELECT_DELETE = "请选择一个或多个备份进行删除。"
MSG_DELETE_SINGLE = "确定删除备份'{name}'?"
MSG_DELETE_MULTIPLE = "确定删除 {count} 个备份文件夹？\n\n{preview}{extra}"
DLG_TITLE_DELETE_BACKUP = "删除备份"
MSG_DELETE_ERRORS = "部分备份文件夹删除失败:\n\n"
BTN_INSTALL_SELECTED = "安装选中项"
BTN_DELETE_SELECTED = "删除选中项"
MSG_RESTORE_CONFIRM = "确定为配置文件 '{backup_name}' 恢复备份 '{profile_name}'?"
MSG_RESTORE_CONFIRM_DETAIL = "此操作将替换当前启用/禁用的模组文件、已保存的配置集和/或 profile_mods_list.json。"
MSG_RESTORE_SUCCESS = "恢复操作完成.\n\n"
MSG_RESTORE_WARNINGS = "恢复操作完成，但存在警告.\n\n"
MSG_RESTORE_FAILED = "恢复失败.\n\n"

# ===== install_mods/process_install.py =====
DLG_TITLE_NOTHING_SELECTED = "未选中任何项"
MSG_NO_MODS_SELECTED_INSTALL = "未选择要安装的模组。"
DLG_TITLE_CONFIRM_INSTALL = "确认安装"
MSG_CONFIRM_INSTALL_LIST = "确定安装以下 {count} 个模组?\n\n{mod_list}"
MSG_CONFIRM_INSTALL_COUNT = "确定安装选中的 {count} 个模组?"
DLG_TITLE_ERROR = "错误"
MSG_NO_ROOT_FOLDER_INSTALL = "未设置根目录！请先点击设置并创建根目录，再尝试安装模组。"
MSG_SELECTED_MODS_NOT_FOUND = "选中的模组文件未找到。"
DLG_TITLE_CONFIRM_SOURCE_DELETE = "确认删除源文件"
MSG_CONFIRM_SOURCE_DELETE = "安装完成后，是否删除源文件夹中剩余的模组压缩包?\n\n{preview}{extra}"

# ===== install_mods/process_uninstall.py =====
MSG_NO_FILES_SELECTED_DELETE = "未选择要删除的文件。"
DLG_TITLE_CONFIRM_DELETE = "确认删除"
MSG_CONFIRM_DELETE_COUNT = "确定要删除 {count} 个文件?"

# ===== install_mods/dying_light_auto_patch.py =====
DLG_TITLE_DL_DATA_SLOT = "替换消逝的光芒数据槽位"
LBL_DL_DATA_SLOT_CHOOSE = "安装前，请选择要替换的现有消逝的光芒数据文件、使用下一个空闲槽位全新安装，或取消安装。"
LBL_DL_SOURCE_MOD = "源模组: {source_display}"
LBL_DL_INSTALLING = "正在安装: {incoming_file}"
LBL_DL_PROFILE = "配置文件: {profile_name}"
BTN_INSTALL_AS_NEW = "全新安装"
BTN_INSTALL_AS_NEW_SLOT = "全新安装（{target} 槽位）"
BTN_CANCEL_INSTALL = "取消安装"
LBL_DL_STATE_ACTIVE = "已启用"
LBL_DL_STATE_DISABLED = "已禁用"

# ===== install_mods/archive_handler/archive_handler_core.py =====
DLG_TITLE_ARCHIVE_INSTALL_CHOICE = "压缩包安装选项"
MSG_ARCHIVE_MULTI_CANDIDATES = "在压缩包中检测到多个可安装项:\n{archive_title}\n\n此配置文件支持的扩展名: {exts_label}\n请选择一个项安装、全部安装，或跳过此压缩包。"
BTN_INSTALL_ALL = "全部安装"
BTN_SKIP_ARCHIVE = "跳过此压缩包"
DLG_TITLE_SELECTION_REQUIRED = "需选择安装项"
MSG_SELECT_CANDIDATE_FIRST = "请先选择一个安装项，或点击「全部安装」。"
DLG_TITLE_ARCHIVE_FOLDER_CHOICE = "压缩包文件夹选择"
MSG_ARCHIVE_MULTI_FOLDERS = "在压缩包中检测到多个文件夹安装项:\n{archive_title}\n\n请选择一个文件夹安装、全部安装，或跳过此压缩包。"
# ===== install_mods/replacement_handler/resolve_replacement.py =====
DLG_TITLE_SELECT_REPLACEMENT = "选择替换目标"
MSG_REPLACEMENT_DEFAULT = "检测到匹配/相似文件。请选择要替换的文件，或跳过替换。"
BTN_SKIP_REPLACEMENT = "跳过替换（安装新文件/替换完全匹配项）"

# ===== launch_game/launcher_core.py =====
MSG_NO_INSTALL_DIR = (
    "未设置有效的安装目录!\n \n- 游戏路径 [STEAM]:\n   > 点击 '检测 Steam'\n "
    "\n- 游戏路径 [手动]:\n   >  点击 '设置游戏安装目录' 和'设置游戏EXE路径' 完成配置."
)
MSG_EXE_NOT_FOUND = "未找到 {game_name} 的可执行文件!\n"
DLG_TITLE_CZT_LAUNCHER = "CZT 启动器"
MSG_LAUNCH_OPTIONS = (
    "{game_name} 启动选项: \n\n"
    " ➡️ 链接 | 带模组 = 链接已启用的模组。\n"
    " ➡️ 取消链接 | 安全模式 = 移除现有链接。\n"
    " ➡️  取消 = 终止启动流程!"
)
BTN_LINK_MODDED = "链接 | 带模组"
BTN_UNLINK_SAFE = "取消链接 | 安全模式"
MSG_ELEVATION_REQUIRED = "需要提升权限。正在尝试以管理员身份重新启动。\n\n错误: {error}"
MSG_PERMISSION_DENIED = "权限被拒绝.\n\n错误: {error}"
MSG_LAUNCH_TOGGLE_FAILED = "无法切换模组状态或启动游戏:\n{error}"

# ===== launch_game/launcher_utilities.py =====
MSG_ELEVATION_FAILED = "获取管理员权限失败: {error}"
MSG_SYMLINK_PERMISSIONS = (
    "需要 Windows 管理员权限才能创建符号链接\n\n"
    "请选择以下选项:\n"
    "- 以管理员身份运行本程序.\n"
    "- 在Windows设置中启用开发者模式以永久绕过此限制.\n"
    "    ↳ 无需管理员权限!\n"
)
BTN_RUN_AS_ADMIN = "以管理员身份运行"
BTN_OPEN_WIN_SETTINGS = "打开Windows设置"
MSG_DEV_MODE_OPEN_FAILED = "无法打开开发者模式设置页面。"

# ===== loadout_system/detect_missing.py =====
DLG_TITLE_MISSING_MODS = "缺失模组"
MSG_MISSING_NO_LOADOUTS = "未找到配置文件 '{profile_name}'的已保存配置集."
MSG_MISSING_LOADOUT_NOT_FOUND = "未找到配置集 '{target_loadout}'。"
DLG_TITLE_DETECT_MISSING = "检测缺失模组"
LBL_DETECT_MISSING_SELECT = "选择一个配置集，与已安装文件进行比对:"
MSG_MISSING_NO_FILES = "配置集  '{target_loadout}' 无关联文件."
MSG_MISSING_NONE_DETECTED = "未检测到配置集 '{target_loadout}' 的缺失文件."
MSG_MISSING_FOUND = "检测到配置集 '{target_loadout}' 有 {count} 个缺失的模组文件"
MSG_MISSING_DOWNLOAD_PROMPT = (
    "检测到 '{target_loadout}' 配置集有 {count} 个缺失的模组文件。\n\n"
    "是否立即下载并安装 {download_count} 个缺失项（含已保存的配置集元数据）w?"
)
MSG_MISSING_NO_METADATA = "{count} 个缺失项无Nexus元数据，将仅列出名称。"

# ===== loadout_system/ls_ui_dropdown.py =====
BTN_LOADOUTS = "配置集"
TIP_LOADOUTS = (
    "1.)先禁用所有模组，再启用你想加入新配置集的模组。\n"
    "2.)点击保存图标，将已启用的模组保存为配置集文件。\n"
    " - 已保存的配置集可随时从此下拉菜单切换。\n"
    " - 在「全部管理」中，每个配置集行都有重命名、复制文件、下载图标。\n"
    " - 点击「从文件导入」可从其他JSON文件添加配置集。\n"
    " - 也可点击「全部管理」删除/编辑配置集信息。"
)

# ===== loadout_system/ls_ui_widgets.py =====
TIP_LOADOUT_CHECKBOX = "勾选此项，可在「加载」或「合并」加载配置时包含本项。"
TIP_RENAME_LOADOUT = "重命名加载配置"
TIP_COPY_FILE = "复制文件路径到剪贴板"
TIP_DOWNLOAD_LOADOUT = "下载此加载配置"
TIP_DETECT_MISSING = (
    "不小心删除了模组？\n"
    "运行此功能可检测并下载此加载配置中缺失的模组"
)
TIP_REFRESH_NEXUS = (
    "验证并更新Nexus链接 + 文件ID。\n"
    "当模组在Nexus更新后，模组文件的下载ID会变化，但旧ID可能仍保留在加载配置文件中。\n"
    "   - 失效的URL/ID会导致下载失败。\n"
    "运行此功能将检查此类失效条目，并使用Nexus的最新信息更新。\n"
    "建议在以下场景运行：\n"
    "   - 你最近更新了现有模组（仅更新，未添加/移除）\n"
    "   - 向他人分享加载配置前。"
)

# ===== loadout_system/ls_ui_manage_dialog.py =====
LBL_MANAGE_LOADOUTS_TITLE = "加载配置文件："
LBL_MANAGE_LOADOUTS_DESC = "（在下方输入名称，点击「保存加载配置」创建新配置）"
LBL_MANAGE_LOADOUTS_TIP_1 = "提示1：选择一个已保存的加载配置，点击「保存加载配置」可覆盖它。"
LBL_MANAGE_LOADOUTS_TIP_2 = "提示2：将鼠标悬停在按钮上查看信息提示。"
LBL_CREATE_LOADOUT = "创建加载配置："
BTN_SAVE_LOADOUT = "保存加载配置"
BTN_LOAD_SELECTED = "加载所选"
BTN_MERGE_SELECTED = "合并所选"
BTN_IMPORT_LOADOUT = "导入加载配置"
BTN_DELETE_LOADOUT = "删除加载配置"

TIP_OPEN_LOADOUTS_FOLDER = "打开加载配置文件夹"
TIP_SAVE_LOADOUT = (
    "- 输入新名称并点击「保存加载配置」可创建新加载配置 \n"
    "- 选择现有加载配置后点击「保存加载配置」可覆盖原有配置"
)
TIP_LOAD_LOADOUT = (
    "加载（启用）一个或多个加载配置。\n"
    "  仅启用当前已安装的模组。\n"
    "  使用下载按钮可实际下载模组列表文件。 \n"
    "  你也可以先加载配置，再按F9检测缺失的模组文件。"
)
TIP_MERGE_LOADOUT = "将所选加载配置合并为一个新配置。"
TIP_IMPORT_LOADOUT = "从JSON文件导入加载配置。"
TIP_DELETE_LOADOUT = "删除所选加载配置。"
DLG_TITLE_OVERWRITE_LOADOUT = "覆盖加载配置"
MSG_OVERWRITE_LOADOUT = "覆盖现有加载配置「{name}」？"
DLG_TITLE_COPY_LOADOUT = "复制加载配置文件"
DLG_TITLE_DOWNLOAD_LOADOUT = "下载加载配置"
DLG_TITLE_REFRESH_NEXUS = "刷新Nexus元数据"
MSG_NEXUS_API_REQUIRED = "需要Nexus API密钥。"
MSG_REFRESH_NEXUS_CONFIRM = "验证「{loadout_name}」的Nexus链接和固定文件ID，并使用刷新后的元数据覆盖此加载配置文件？"
MSG_REFRESH_NO_ENTRIES = "此加载配置无元数据条目，请先保存或导入元数据。"
MSG_REFRESH_WRITE_ERROR = "验证完成，但写入文件失败：\n{error}"
MSG_REFRESH_COMPLETE = (
    "「{loadout_name}」的刷新已完成。\n\n"
    "扫描总数：{scanned_count}\n"
    "有效条目：{valid_count}\n"
    "无效条目：{invalid_count}\n"
    "修复失效ID数量：{repaired_count}\n"
    "更新条目总数：{changed}\n"
)
DLG_TITLE_LOADOUTS = "加载配置"
MSG_MULTI_SELECT_ONLY_DELETE = "多选时仅支持删除操作。\n\n请求的操作：{action_label}"
MSG_OVERWRITE_PIN_MODE = "使用当前启用的模组覆盖现有加载配置「{name}」？\n\n请选择此加载配置中模组文件ID的处理方式：\n\n"
BTN_UPDATE_ALL = "更新全部"
BTN_UPDATE_NEW = "仅更新新增项"
BTN_DONT_UPDATE = "不更新"
MSG_SELECT_ONE_OVERWRITE = "请仅选择一个加载配置进行覆盖，或输入新名称。"
MSG_ENTER_LOADOUT_NAME = "请输入加载配置名称，或选择一个要覆盖的配置。"
DLG_TITLE_SAVE_LOADOUT = "保存加载配置"
MSG_PIN_FILE_IDS_PROMPT = (
    "部分模组在Nexus上有多个主文件或可选文件。\n"
    "是否要将特定的文件版本保存到此加载配置中？\n\n"
    "此操作可让未来下载/分享加载配置时更稳定。\n\n"
    "注意：CZT会为你展示所有可用版本，方便选择，无需手动查找。\n"
)
MSG_OVERWRITE_SAVED = "覆盖保存完成。\n\n使用模式：{mode_label}\n更新文件ID数量：{processed}"
MSG_OVERWRITE_SAVED_NO_CHANGE = "覆盖保存完成。\n\n使用模式：{mode_label}\n0个条目更新，新数据与现有数据一致。"
MSG_SELECT_LOADOUTS_DELETE = "选择一个或多个已保存的加载配置进行删除。"
DLG_TITLE_DELETE_LOADOUTS = "删除加载配置"
MSG_CHECK_LOADOUTS_LOAD = "勾选一个或多个已保存的加载配置进行加载。"
DLG_TITLE_LOAD_LOADOUT = "加载配置"
MSG_LOADED_LOADOUTS = "成功加载 {count} 个加载配置{plural}。"
DLG_TITLE_MERGE_LOADOUTS = "合并加载配置"
MSG_SELECT_TWO_MERGE = "至少选择两个已保存的加载配置进行合并。"
LBL_MERGED_LOADOUT_NAME = "合并后的加载配置名称："
MSG_ENTER_MERGED_NAME = "请输入有效的合并后配置名称。"
DLG_TITLE_RENAME_LOADOUT = "重命名加载配置"
LBL_NEW_FILE_NAME = "新文件名："

# ===== loadout_system/download_list.py =====
DLG_TITLE_DOWNLOAD_MOD_LIST = "下载模组列表"
MSG_RUN_INSTALL_NOW = "{summary_text}\n\n是否立即安装？"
MSG_INSTALL_NOT_AVAILABLE = "安装逻辑不可用"

# ===== loadout_system/importing.py =====
DLG_TITLE_IMPORT_LOADOUTS = "导入加载配置"
MSG_IMPORT_ROOT_NOT_SET = "根目录未配置。"

# ===== nexus/updates.py =====
MSG_API_KEY_REQUIRED = (
    "检查更新需要你的Nexus API密钥。\n"
    "API密钥用于与Nexus网站通信。\n"
    "  密钥将保存在本地配置文件中。"
)
MSG_NO_TRACKED_MODS = "此配置文件未找到已追踪的模组。"
MSG_ALL_UP_TO_DATE = "所有模组均为最新版本！"
LBL_UPDATES_AVAILABLE = "有可用更新："
UPDATE_LINE_FMT = "→ {mod_name}（当前版本：{local_version} | 最新版本：{latest_version}）"

# ===== nexus/nexus_sync.py =====
MSG_MOD_DIR_NOT_SET = (
    "模组目录未设置或不存在。"
    "请先在「用户设置」标签页中设置模组目录，再保存Nexus链接。"
)
MSG_NEXUS_INFO_UPDATED = "已更新 {count} 个模组的Nexus信息。"

# ===== nexus/downloads.py =====
LBL_SELECT_FILE_DOWNLOAD = "选择要下载的文件"
LBL_SELECT_A_FILE = "选择要下载的文件……"
BTN_DOWNLOAD = "下载"
BTN_CANCEL = "取消"
ERR_DOWNLOAD_CANCELLED = "下载已取消"
ERR_NO_FILE_SELECTED = "未选择文件"
ERR_MISSING_API_KEY = "缺失Nexus API密钥"
ERR_NO_FILES_AVAILABLE = "无可用文件"
ERR_MISSING_MOD_ID_URL = "缺失Nexus模组ID或URL"
ERR_CANNOT_RESOLVE_SLUG = "无法解析此配置文件对应的Nexus游戏标识（slug）"
ERR_INVALID_MOD_ID_URL = "无效的Nexus模组ID或URL"
ERR_NO_DOWNLOADABLE_FILE = "无可用下载文件ID"
ERR_MISSING_ROOT_FOLDER = "缺失czt_root_folder目录"
ERR_NO_SELECTED_MODS = "未选择模组"
ERR_NO_TRACKED_MODS_PROFILE = "当前配置文件无已追踪的模组"
ERR_NO_VALID_NEXUS_URL = "未选择包含有效nexus_url的模组"
LBL_INSTALLED_MOD = "已安装模组：{name}"
LBL_INSTALLED_FILE = "已安装文件：{name}"
LBL_FILE_UNKNOWN = "未知"
LBL_FILE_VERSION = "版本 {version}"

# ===== nexus/browse_mods/browser_actions.py =====
MSG_OPEN_MOD_PAGE_FIRST = (
    "请先打开具体的Nexus模组页面，再点击「添加当前模组」。\n\n"
    "预期URL格式：\n"
    "https://www.nexusmods.com/<游戏名>/mods/<ID>"
)
STATUS_DOWNLOADING_MOD = "正在下载模组 {mod_id}……"
STATUS_DOWNLOAD_FAILED = "下载失败"
STATUS_DOWNLOAD_INSTALLING = "下载完成，正在安装……"
STATUS_DOWNLOADED = "已下载：{name}"
MSG_DOWNLOAD_COMPLETE_SAVED = "下载完成。\n\n保存路径：{path}"
STATUS_INSTALL_FAILED = "安装失败"
STATUS_INSTALLED = "已安装：{name}"

# ===== nexus/browse_mods/browser_widgets.py =====
LBL_SELECT_A_MOD = "选择一个模组"
LBL_NOT_INSTALLED = "未安装"
BTN_ADD_TO_FAVORITES = "加入收藏"
LBL_ZERO_DOWNLOADS = "0次下载"
LBL_ZERO_ENDORSEMENTS = "0次认可"
LBL_UPDATED_NONE = "更新时间：--"
LBL_NO_MOD_SELECTED = "未选择模组"
LBL_PAK_FILES = "PAK文件"
LBL_NO_FILES_AVAILABLE = "无可用文件"
LBL_NO_CHANGELOG = "无更新日志"
LBL_UNKNOWN_MOD = "未知模组"
LBL_BY_AUTHOR = "作者：{author}"
LBL_DOWNLOADS_COUNT = "{count}次下载"
LBL_ENDORSEMENTS_COUNT = "{count}次认可"
LBL_UPDATED_DATE = "更新时间：{date}"
LBL_NO_DESCRIPTION = "无可用描述。"

# ===== nexus/browse_mods/browser_window.py =====
DLG_TITLE_BROWSE_NEXUS = "浏览Nexus模组 - {profile}"
TIP_BACK = "后退"
TIP_FORWARD = "前进"
TIP_REFRESH = "刷新"
TIP_GO = "跳转"
TIP_ENDORSEMENT_STATUS = "认可状态"
MSG_WEBENGINE_UNAVAILABLE = (
    "此安装版本未包含Qt WebEngine。\n"
    "请安装PySide6-WebEngine以启用内置Nexus浏览功能。"
)
STATUS_BROWSER_UNAVAILABLE = "内置浏览器不可用"
STATUS_LOADING_PAGE = "正在加载页面……"
STATUS_NO_NEXUS_LINK = "此配置文件未配置Nexus游戏链接"
STATUS_LOADING_MODS = "正在加载Nexus模组……"
STATUS_PAGE_LOADED = "页面加载完成"
STATUS_PAGE_FAILED = "页面加载失败"

# ===== nexus/browse_mods/endorsements.py =====
TIP_ENDORSE_ONLY_MOD_PAGES = "仅在模组详情页可查看/操作认可状态"
TIP_ENDORSED = "已认可"
TIP_NOT_ENDORSED = "未认可"
ERR_INVALID_ENDORSEMENT = "无效的认可操作"
ERR_UNKNOWN_ENDORSEMENT = "未知的认可错误"
STATUS_OPEN_MOD_TO_ENDORSE = "请打开具体的模组页面进行认可操作"
STATUS_ENDORSE_UNAVAILABLE = "认可状态不可用"
STATUS_UPDATING_ENDORSEMENT = "正在更新认可状态……"
STATUS_ENDORSED = "已认可"
STATUS_ENDORSEMENT_REMOVED = "已取消认可"
STATUS_ENDORSEMENT_FAILED = "认可操作失败"
MSG_ENDORSEMENT_FAILED = "无法更新认可状态。\n\n{error}"

# ===== nexus/browse_mods/install_state.py =====
LBL_MOD_INSTALLED = "模组已安装"
LBL_MOD_NOT_INSTALLED = "模组未安装"

# ===== nexus/protocol_handler/nxm/nxm_actions.py =====
MSG_NXM_GAME_MISMATCH = (
    "此模组适用于「{game}」。 \n"
    "当前配置文件为「{profile}」。\n\n"
    "请切换到「{game}」配置文件后重试。"
)

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py =====
MSG_CZTMM_GAME_MISMATCH = (
    "你尝试安装的模组适用于「{game}」。 \n"
    "当前配置文件为「{profile}」。\n\n"
    "请切换到「{game}」配置文件后重试。"
)

# ===== refresh_manager/refresh_manager.py =====
PLACEHOLDER_SEARCH_MODS = "搜索模组 : {profile}"


# =====================================================================
#  日志消息  (czt_log / czt_log_synced)
# =====================================================================

# ===== install_mods/process_install.py (logs) =====
LOG_INSTALL_CANCELLED = "[安装已取消] 用户在替换确认阶段取消了安装。"
LOG_INSTALL_FAILED = "\n[错误] 安装失败：{error}\n"
LOG_INSTALL_QUEUED = "[安装] 已有安装任务在运行，此安装请求已加入队列。"
LOG_INSTALL_SELECTED_FILES = "\n[安装] 所选文件：\n{file_list}"
LOG_PROCESSING_MOD = "[处理中] 模组：{install_label}"
LOG_INSTALL_MOD_FAILED = "[错误] 安装「{install_label}」时失败：{error}"
LOG_DELETE_SOURCE_FAILED = "[安装后删除] 无法移除源文件「{src_path}」：{error}"
LOG_INSTALL_COMPLETED = " \n[安装流程完成] 所有选中的模组已处理完毕。\n"
LOG_SUMMARY = "[摘要]"
LOG_SUMMARY_SUCCESS = "\n    > 成功："
LOG_SUMMARY_FAILED = "\n    > 失败："
LOG_SUMMARY_SKIPPED = "\n    > 已跳过：（未找到匹配导出器的压缩包安装项）"
LOG_SUMMARY_SOURCE_DELETED = "\n    > 源文件已删除："
LOG_SUMMARY_SOURCE_DELETE_SKIPPED = "\n    > 源文件删除已跳过：用户拒绝确认。"

# ===== install_mods/process_uninstall.py (logs) =====
LOG_DELETED_MODS = "[删除] 已删除 {count} 个模组：\n -> {item_list}"

# ===== install_mods/dying_light_auto_patch.py (logs) =====
LOG_DL_SLOT_SKIPPED = "[消逝的光芒数据槽位] 跳过「{base_name}」，原因：未选择替换目标且其当前槽位不可用。"
LOG_DL_SLOT_KEEP = "[消逝的光芒数据槽位] 保留待安装文件名称「{base_name}」。"
LOG_DL_SLOT_INSTALL_NEW = "[消逝的光芒数据槽位] 选择全新安装，为「{base_name}」分配下一个空闲槽位「{selected_file_name}」。"
LOG_DL_SLOT_REPLACE = "[消逝的光芒数据槽位] 为「{base_name}」选择替换目标「{selected_file_name}」。"

# ===== install_mods/archive_handler/archive_handler_core.py (logs) =====
LOG_OPTION_SKIP_NO_EXPORTERS = "[安装][选项][已跳过] {archive_name} 中无匹配导出器名称的{choice_kind}安装项。"
LOG_OPTION_AUTO_SELECT = "[安装][选项] 在{archive_name}中自动选中 {count} 个匹配导出器的{choice_kind}安装项。"
LOG_OPTION_SKIP_NO_MATCH = "[安装][选项][已跳过] {archive_name} 中未找到匹配导出器的{choice_kind}安装项。"
LOG_CACHE_SKIP = "[安装][选项][缓存] 使用缓存的文件选项：跳过压缩包 {archive_name}"
LOG_CACHE_INSTALL_ALL = "[安装][选项][缓存] 使用缓存的文件选项：安装{archive_name}中的全部内容"
LOG_CACHE_SELECTED = "[安装][选项][缓存] 使用缓存的文件选择：{chosen_rel}"
LOG_MULTI_FOLDER_CANDIDATES = "[安装][选项] 在压缩包中找到多个文件夹安装项：{archive_name}"
LOG_SKIPPED_FOLDER_CHOICE = "[安装][已跳过] 用户跳过了文件夹压缩包选择：{archive_name}"
LOG_ADDITIONAL_FOLDER_CANDIDATES = "[安装][选项] 所选选项中找到额外的文件夹安装项：{archive_name}"
LOG_SKIPPED_NESTED_FOLDER = "[安装][已跳过] 用户跳过了嵌套文件夹选择：{archive_name}"
LOG_MULTI_FILE_CANDIDATES = "[安装][选项] 在压缩包中找到多个文件安装项：{archive_name}"
LOG_SKIPPED_FILE_CHOICE = "[安装][已跳过] 用户跳过了压缩包安装选择：{archive_name}"
LOG_ADDITIONAL_FILE_CANDIDATES = "[安装][选项] 所选选项中找到额外的文件安装项：{archive_name}"
LOG_SKIPPED_NESTED_FILE = "[安装][已跳过] 用户跳过了嵌套文件选择：{archive_name}"
LOG_UNSUPPORTED_ARCHIVE = "[错误] 不支持的压缩包类型或缺失依赖库：{archive_type}"
LOG_RAR_NOT_AVAILABLE = "[错误] 缺失rarfile库，无法解压.rar文件：{archive_name}。"
LOG_7Z_NOT_AVAILABLE = "[错误] 缺失py7zr库，无法解压.7z文件：{archive_name}"
LOG_PROCESS_ITEM_FAILED = "[错误] 处理{item}失败：{error}"
LOG_EXTRACT_FAILED = "[错误] 解压{archive_type}压缩包{archive_name}失败：{error}"

# ===== install_mods/replacement_handler/resolve_replacement.py (logs) =====
LOG_REPLACEMENT_CONFIRM = "[安装安全校验] 「{mod_name}」需要确认替换操作"
LOG_REPLACEMENT_REMOVE_FAILED = "[警告] 无法移除所选替换文件「{old_path}」：{error}"
LOG_REPLACEMENT_DIALOG_FAILED = "[警告] 替换确认对话框失败：{error_type}：{error}"

# ===== install_mods/install_registry.py (logs) =====
LOG_REPLACE_EXISTING = "[更新安装] 替换现有模组文件：{old_file} -> {new_file}"
LOG_REPLACE_REMOVE_FAILED = "[警告] 无法移除被替换的模组文件「{old_file}」：{error}"
LOG_REPLACE_DISABLED_REMOVE_FAILED = "[警告] 无法移除被替换的禁用模组文件「{old_file}」：{error}"
LOG_JSON_UPDATING = "[JSON写入] 更新模组列表中的现有条目：\n   ↓「{mod_name}」"
LOG_REPLACE_OPTIONS_FOUND = "[替换] 「{mod_name}」：找到 {count} 个现有文件选项。"
LOG_INSTALLED = "[已安装] 「{mod_name}」"
LOG_INSTALLED_KEPT_EXISTING = "[已安装] 「{mod_name}」：保留现有文件并安装新文件。"
LOG_JSON_WRITE_COMPLETE = (
    "[JSON写入完成] profile_mods_list.json 已成功更新。\n"
    "[摘要] 更新数量：{updated_count}，新增数量：{new_count}，总数：{total_count}。"
)
LOG_JSON_WRITE_ERROR = "[错误] 无法更新模组列表：{error}"

# ===== install_mods/install_utilities.py (logs) =====
LOG_STAGING_ERROR = "[暂存错误] 无法暂存{file_name}：{error}"
LOG_STAGED = "[已暂存] 已将 {count} 个模组暂存至：\n -> {staged_list}\n[源目录] -> {mods_source}"
LOG_REPLACEMENT_TIMEOUT = "[警告] 等待替换确认对话框超时。"

# ===== install_mods/archive_handler/progress.py (logs) =====
LOG_PROGRESS = "[{stage_key}] {label} [{percent}%]"
LOG_EXTRACTING = "[解压中] {label} [0%]"
LOG_INSTALLING_PROGRESS = "[安装中] {label} [0%]"

# ===== nexus/updates.py (logs) =====
LOG_UPDATE_SCAN_START = "[更新扫描] 当前配置文件：{profile_name} | 正在检查可用更新……\n"
LOG_UPDATE_SCAN_MOD = "→ 模组：{file_name} | 本地版本：{local_version} | 最新版本：{latest_version} | "
LOG_UPDATE_SCAN_COMPLETED = " \n[更新扫描完成] {scan_label} | 找到更新数量：{updated_count}"
LOG_UPDATE_SCAN_COMPLETED_ALT = "\n[更新扫描完成] {scan_label} | 找到更新数量：{updated_count}"

# ===== nexus/nexus_sync.py (logs) =====
LOG_NEXUS_MODS_DIR_MISSING = "[NEXUS] 模组目录缺失，使用备用目录：{fallback_dir}"
LOG_NEXUS_MODS_DIR_ERROR = "[NEXUS][错误] 模组目录无效。提供的路径：{mods_dir} | 备用路径：{fallback_dir} | 配置文件：{profile_name}"
LOG_NEXUS_SAVING = "[NEXUS][保存] 将收集到的模组数据保存至 {tracked_file}"
LOG_NEXUS_INFO_UPDATED_LOG = "[NEXUS] 已更新 {updated_count} 个模组的信息。"

# ===== nexus/downloads.py (logs) =====
LOG_NEXUS_REDIRECT_STANDARD = "[NEXUS - 标准模式] 重定向到模组文件页面以下载：{target_url}"
LOG_NEXUS_OPEN_FAILED = "[NEXUS] 无法打开模组文件页面：{error}"
LOG_DOWNLOADING = "[下载中] {out_path}"
LOG_DOWNLOAD_FAILED = "[下载] 「{display_label}」下载失败：{error}"
LOG_DOWNLOAD_COMPLETED = "[下载] 完成：成功下载 {downloaded} 个文件。"

# ===== nexus/browse_mods/browser_window.py (logs) =====
LOG_BROWSER_CLOSED = "[NEXUS浏览器] 已关闭"
LOG_BROWSER_NO_GAME = "[NEXUS浏览器] 无可用游戏变量"

# ===== nexus/protocol_handler/nxm/nxm_actions.py (logs) =====
LOG_NXM_RECEIVED = "[NXM] 收到URL：{nxm_url}"
LOG_NXM_PARSE_FAILED = "[NXM][错误] 无法解析NXM URL：{nxm_url}"
LOG_NXM_GAME_MISMATCH_LOG = "[NXM] 游戏不匹配：NXM={game_slug}，当前配置文件={profile_game_slug}"
LOG_NXM_DOWNLOAD_EVENT = (
    "[NXM] 收到Nexus下载事件：游戏：{game_slug}，模组ID：{mod_id}，文件ID：{file_id}\n"
    "[NXM] 下载完成后，CZT将自动安装该文件。\n"
    "[NXM] 请等待……"
)
LOG_NXM_DOWNLOAD_FAILED = "[NXM] 下载失败或已取消"
LOG_NXM_DOWNLOAD_COMPLETE = "[NXM] 下载完成：{result}"

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py (logs) =====
LOG_CZTMM_RECEIVED = "[CZTMM] 收到URL：{cztmm_url}"
LOG_CZTMM_PARSE_FAILED = "[CZTMM][错误] 无法解析URL：{cztmm_url}"
LOG_CZTMM_GAME_MISMATCH_LOG = "[CZTMM] 游戏不匹配：CZTMM={game_slug}，当前配置文件={profile_game_slug}"
LOG_CZTMM_DOWNLOAD_EVENT = (
    "[CZTMM] 收到Nexus下载事件：游戏：{game_slug}，模组ID：{mod_id}，文件ID：{file_id}\n"
    "[CZTMM] 下载完成后，CZT将自动安装该文件。\n"
    "[CZTMM] 请等待……"
)
LOG_CZTMM_DOWNLOAD_EVENT_STANDARD = (
    "[CZTMM] 收到Nexus下载事件：游戏：{game_slug}，模组ID：{mod_id}，文件ID：{file_id}\n"
    "[CZTMM] [检测到标准NEXUS账户] \n"
    "[CZTMM] 别忘了在浏览器中点击「慢速下载」！\n"
    "[CZTMM] 下载完成后，CZT将自动安装该文件。\n"
    "[CZTMM] 请等待……\n"
)

# ===== nexus/account_type_status.py (logs) =====
LOG_NEXUS_ACCOUNT_TIER_FAILED = "[CZTMM] 无法解析Nexus账户等级，默认使用标准账户：{error}"

# ===== nexus/manual_download_install.py (logs) =====
LOG_NO_DOWNLOAD_DETECTED = "[CZTMM] 未检测到近期完成的下载，自动安装已跳过。"
LOG_INSTALLING_DOWNLOAD = "[CZTMM] 正在安装已下载的文件：{chosen_path}"

# ===== nexus/browse_mods/browser_ext.py (logs) =====
LOG_BROWSER_JS_WITH_SOURCE = "[NEXUS浏览器][JS] {text}（{source}：{line_number}）"
LOG_BROWSER_JS = "[NEXUS浏览器][JS] {text}"

# ===== nexus/browse_mods/marquee_label.py =====
BANNER_TEXT_FREE = (
    "检测到标准Nexus账户 — "
    "此功能为高级账户设计 — "
    "Nexus限制免费账户从第三方应用直接下载 — "
    "Vortex也受此限制约束。"
)
BANNER_TEXT_PREMIUM = (
    "无需登录即可浏览或下载模组，API密钥已在设置菜单中配置 "
    "— 使用此浏览器时，请导航到目标模组，然后点击「下载并安装当前模组」按钮 "
    "— 模组信息将在下载时保存到本地模组列表文件"
)
LOG_ACCOUNT_TIER_FALLBACK = "[NEXUS浏览器] 无法解析账户等级，默认使用免费账户：{error}"

# ===== nexus/protocol_handler/nxm/nxm_runtime.py (logs) =====
LOG_NXM_STARTUP_REG_FAILED = "[NXM] 应用启动注册设置失败：{error}"
LOG_NXM_SENT_URL = "[NXM] 已将URL发送至运行中的实例：{protocol_url_arg}"
LOG_NXM_SEND_FAILED = "[NXM] 无法将URL发送至运行中的实例：{error}"
LOG_NXM_IPC_FAILED = "[NXM][错误] 无法启动NXM IPC服务器"

# ===== nexus/protocol_handler/nxm/nxm_register.py (logs) =====
LOG_NXM_REGISTERED = "[NXM] 已注册nxm://协议处理器：{command}"
LOG_NXM_REGISTER_FAILED = "[NXM][错误] 注册nxm://处理器失败：{error}"
LOG_NXM_UNREGISTERED = "[NXM] 已注销nxm://协议处理器"
LOG_NXM_UNREGISTER_FAILED = "[NXM][错误] 注销nxm://处理器失败：{error}"

# ===== nexus/protocol_handler/cztmm/cztmm_register.py (logs) =====
LOG_CZTMM_REGISTERED = "[CZTMM] 已注册cztmm://协议处理器：{command}"
LOG_CZTMM_REGISTER_FAILED = "[CZTMM][错误] 注册cztmm://处理器失败：{error}"
LOG_CZTMM_UNREGISTERED = "[CZTMM] 已注销cztmm://协议处理器"
LOG_CZTMM_UNREGISTER_FAILED = "[CZTMM][错误] 注销cztmm://处理器失败：{error}"

# ===== loadout_system/ls_ui_manage_dialog.py (logs) =====
LOG_LOADOUT_ROOT_NOT_SET = "[加载配置] 根目录未设置，无法管理加载配置。"

# ===== loadout_system/download_list.py (logs) =====
LOG_LOADOUT_SAVE_FAILED_DL = "[加载配置] 无法保存从「下载模组列表」导入的加载配置。"
LOG_LOADOUT_IMPORTED_DL = "[加载配置] 已从「下载模组列表」为配置文件「{profile_name}」导入 {added_count} 个加载配置。"
LOG_DOWNLOAD_CANCELED = "[加载配置下载] 在重新下载确认提示时取消了「下载模组列表」操作。"
LOG_DOWNLOAD_SUMMARY = "[摘要] 已下载：{downloaded} | 跳过已存在项：{skipped} | 失败：{failed}"
LOG_DOWNLOAD_INSTALL_QUEUED = "[安装] 已有应用内下载安装任务在运行，此安装请求已加入队列。"
LOG_DOWNLOAD_INSTALL_FAILED = "[安装] 下载安装工作线程失败：{error}\n{traceback}"
LOG_LOADOUT_AUTO_SELECT_FAILED = "[加载配置] 无法自动选中导入的加载配置「{loadout_name}」：{error}"

# ===== loadout_system/importing.py (logs) =====
LOG_LOADOUT_IMPORTED = (
    "[加载配置] 已从「{imported_path}」导入 {added_count} 个加载配置。 \n"
    "添加到主模组列表的条目数：{profile_metadata_added}。 \n"
    "更新主模组列表的条目数：{profile_metadata_updated}。"
)

# ===== loadout_system/build_loadout.py (logs) =====
LOG_LOADOUT_MERGE_FAILED = "[加载配置] 为配置文件「{profile_name}」保存合并后的加载配置失败：{error}"

# ===== loadout_system/apply_loadout.py (logs) =====
LOG_LOADOUT_ROOT_NOT_SET_APPLY = "[加载配置] 根目录未设置，无法应用加载配置。"
LOG_LOADOUT_NO_MODS = "[加载配置] 加载配置「{loadout_name}」未找到模组。"
LOG_LOADOUT_ROOT_NOT_SET_APPLY_MULTI = "[加载配置] 根目录未设置，无法应用加载配置。"
LOG_LOADOUT_NO_MODS_MULTI = "[加载配置] 所选加载配置未找到模组。"

# ===== loadout_system/storage.py (logs) =====
LOG_LOADOUT_REMOVE_FAILED = "[加载配置] 无法移除现有加载配置文件：{error}"
LOG_LOADOUT_SAVE_FAILED = "[加载配置] 保存加载配置失败：{error}"

# ===== loadout_system/select_file_variant.py (logs) =====
LOG_FILE_PIN_SKIPPED = "[加载配置] 「{display_name}」（{cache_key}）的文件固定操作已跳过：{error}"

# ===== loadout_system/ls_utilities.py (logs) =====
LOG_FILE_CANDIDATES_FAILED = "[加载配置] 为{loadout_name}：{mod_id}加载文件候选项失败：{error}"
LOG_FILE_PIN_SELECTION_SKIPPED = "[加载配置] {loadout_name}：{mod_id}的文件固定选择已跳过：{error}"

# ===== Get_SteamLibraries.py (logs) =====
LOG_STEAM_SCAN_DRIVE = "[STEAMLIB][扫描] 正在扫描驱动器 {drive_root} 中的libraryfolders.vdf（新版）"
LOG_STEAM_SCAN_LEGACY = "[STEAMLIB][扫描] 正在扫描驱动器 {drive_root} 中的libraryfolder.vdf（旧版）"
LOG_STEAM_SEARCHING = "[STEAMLIB][扫描] 搜索中... {pattern}"
LOG_STEAM_LOCATED = "[STEAMLIB] [已找到] libraryfolders.vdf @ {vdf}（新版）"
LOG_STEAM_LOCATED_LEGACY = "\n[STEAMLIB] [已找到] libraryfolder.vdf @ {vdf}（旧版）"
LOG_VDF_PARSING = "[VDF] 正在解析VDF文件……"
LOG_STEAM_ADDED = "[STEAMLIB][已添加] ↓ {lib_common}"
LOG_STEAM_PARSE_WARN = "[警告] 无法解析Steam库：{error}"
LOG_STEAM_SKIP_SCAN = "[STEAMLIB] 跳过Steam库扫描：「{current_profile}」的路径模式为「{pathing_mode}」。"
LOG_STEAM_RUN_UTIL = "[运行工具] ▶ SteamLibrarySearchUtility ◀"
LOG_STEAM_SCANNING = "[STEAMLIB] 正在扫描Steam库……"
LOG_STEAM_SCAN_SUCCESS = "[STEAMLIB] [扫描成功]\n    ↓ 所有Steam库路径已更新。"
LOG_STEAM_WARN_NO_ROOT = "⚠️ [警告] 无法保存配置，因为 czt_root_folder 目录不存在。"
LOG_EXE_DETECTED = "[可执行文件已检测] 路径：{path}"
LOG_EXE_NOT_FOUND = "[可执行文件检测] 未找到有效可执行文件。"

# ===== Synced Missing Keys =====
BTN_YES = "是"
BTN_NO = "否"
BTN_SHOW_DETAILS = "显示详情..."
BTN_HIDE_DETAILS = "隐藏详情..."
BTN_IGNORE = "忽略"
BTN_CLOSE = "关闭"
BTN_CHECK_FOR_UPDATES = "检查更新"

MSG_HOTKEY_CONTROLS = (
    "\n\n"
    "[快捷键]\n"
    "    > F2           : 打开加载顺序菜单。\n"
    "    > F3           : 打开插件菜单。\n"
    "    > F5           : 将主窗口重新居中。\n"
    "    > F7           : 链接模组（不启动游戏）。\n"
    "    > F8           : 取消链接模组 / 安全模式（不启动游戏）。\n"
    "    > F9           : 从已保存配置集中检测缺失模组。\n"
    "    > CTRL+O       : 打开 CZT 根目录。\n"
    "    > Shift+H      : 显示快捷键选项。\n"
    "    > Shift+C      : 显示当前配置。\n"
    "    > Shift+R      : 显示资源文件路径。\n"
    "    > Ctrl+Shift+L : 启动游戏。\n"
    "    > Ctrl+Shift+S : 启动调试控制台。\n        \n"
)
DLG_TITLE_PATCH_NOTES = "更新日志"
LBL_PATCH_NOTES = "CZT 模组管理器 - 更新日志"

DLG_TITLE_LOAD_ORDER_BLOCKED = "加载顺序已禁用"
MSG_LOAD_ORDER_BLOCKED_PROFILE = "该配置文件已禁用加载顺序菜单：{profile_name}"
LBL_LOAD_ORDER_TITLE = "选择一个模组，然后使用下方控件生成加载顺序文件。"
LBL_LOAD_ORDER_SUBTITLE = "> 点击“保存顺序”应用更改，然后启动游戏即可！\n> 加载顺序会持续生效，直到再次修改。"
BTN_LOAD_ORDER_MOVE_UP = "上移"
BTN_LOAD_ORDER_MOVE_DOWN = "下移"
BTN_LOAD_ORDER_SAVE_ORDER = "保存顺序"
LBL_LOAD_ORDER_LEGEND_CONTROLS = "控件："
LBL_LOAD_ORDER_LEGEND_MOVE_UP = "上移"
LBL_LOAD_ORDER_LEGEND_MOVE_DOWN = "下移"
LBL_LOAD_ORDER_LEGEND_DRAG = "拖拽：上移或下移"
LBL_LOAD_ORDER_LEGEND_SAVE = "保存：设置加载顺序"

DLG_TITLE_PLUGIN_MANAGER = "插件管理器"
BTN_PLUGIN_MENU = "插件菜单"
LBL_PLUGIN_MANAGER_INSTALLED = "已安装插件"
BTN_PLUGIN_MANAGER_RESCAN = "重新扫描"
MSG_PLUGIN_MANAGER_NOT_INITIALISED = "插件管理器尚未初始化。"
MSG_PLUGIN_MANAGER_EMPTY = (
    "未找到插件。\n\n"
    "请将插件文件夹放入：\n  {plugins_root}\n\n"
    "每个插件文件夹必须包含 plugin.json 清单文件。"
)
CB_PLUGIN_ENABLE_PROFILE_FMT = "配置文件（{profile}）"
LBL_PLUGIN_PROFILE_NONE = "无"
BTN_PLUGIN_OPEN_FOLDER = "打开文件夹"
MSG_PLUGIN_MANAGER_SAVE_FAILED = "保存配置失败：\n{error}"
MSG_PLUGIN_ROOT_NOT_SET = "CZT 根目录未设置，无法加载插件。"
LBL_PLUGIN_STANDALONE_EXE = "独立 EXE："
LBL_PLUGIN_SCRIPTS = "脚本："
LBL_PLUGIN_NONE_STANDALONE = "未找到独立 EXE 插件。"
LBL_PLUGIN_NONE_SCRIPTS = "未找到脚本插件。"
CB_PLUGIN_ENABLE_PROFILE = "为此配置文件启用"
CB_PLUGIN_ENABLE_GLOBAL = "全局启用"
CB_PLUGIN_RUN_STARTUP = "启动时运行"
BTN_PLUGIN_RUN = "加载"
BTN_PLUGIN_UNLOAD = "卸载"
BTN_PLUGIN_SAVE_STARTUP_OPTIONS = "保存启动选项"
BTN_PLUGIN_CLOSE = "关闭"
DLG_TITLE_PLUGIN_RUN_AS_ADMIN = "以管理员身份运行？（可选）"
MSG_PLUGIN_RUN_AS_ADMIN = "是否以管理员身份运行 {plugin_name}？"
DLG_TITLE_PLUGIN = "插件"
MSG_PLUGIN_LAUNCHED = "已启动：{plugin_name}"
DLG_TITLE_PLUGIN_ERROR = "插件错误"
MSG_PLUGIN_LAUNCH_FAILED = "启动插件失败：\n{error}"
MSG_PLUGIN_UNLOAD_FAILED = "卸载插件失败：\n{error}"
MSG_PLUGIN_UNLOADED = "已卸载：{plugin_name}\n\n注意：这只会从内存中移除模块。\n若插件未自行清理，运行中的线程、信号或 UI 元素可能仍会保留。"
MSG_PLUGIN_NOTHING_TO_UNLOAD = "没有可卸载内容：{plugin_name}"
DLG_TITLE_PLUGIN_STARTUP_REQUIREMENTS = "启动要求未满足"
MSG_PLUGIN_STARTUP_REQUIREMENTS = "设置为启动时运行的插件必须“全局启用”或“为配置文件启用”。\n以下插件在修复前不会随启动加载：\n- {plugins}"
DLG_TITLE_SAVED = "已保存"
MSG_PLUGIN_OPTIONS_SAVED = "插件选项已保存。"
DLG_TITLE_SAVE_ERROR = "保存错误"
MSG_PLUGIN_OPTIONS_SAVE_FAILED = "保存插件选项失败：\n{error}"

LOG_AUDIO_MENU_MUSIC_PAUSED = "[音频] 菜单音乐已暂停。重启 CZT 可重置，或重新保存音频设置可恢复。"
LOG_LAUNCH_LOAD_ORDER_READ_FAILED = "[启动] 读取加载顺序失败：{error}"
LOG_CONFIG_RELOAD_FAILED = "[错误] 无法从磁盘重新加载配置：{error}"
LOG_LAUNCH_SEARCHING_EXE = "[首次启动]\n- 正在以下位置搜索 EXE：{steam_libraries}"
LOG_LAUNCH_EXE_NOT_FOUND = "[错误] 未找到 {game_name} 的 EXE！"
LOG_NO_ROOT_SET = "[错误] 未设置根目录！点击“创建根目录”开始使用 CZT。"
LOG_LAUNCH_CREATED_MODS_FOLDER = "[启动] 已创建缺失模组文件夹：{path}"
LOG_LAUNCH_CREATED_MODS_FOLDER_PARENT = "[启动] 已创建缺失模组父目录：{path}"
LOG_MODS_FOLDER_PREP_FAILED = "[错误] 无法准备模组文件夹路径 {path}：{error}"
LOG_LAUNCH_CANCELLED = "[启动] 用户已取消 {game_name} 启动！"
LOG_TOTAL_LINKED = "[总计] 已链接 {count} 个模组"
LOG_PER_FILE_REMOVE_FAILED = "[按文件] 无法移除符号链接 {path}：{error}"
LOG_TYPE_SYMLINKS_REMOVED = "[{mod_type}] 已移除 {count} 个符号链接"
LOG_PER_FOLDER_REMOVE_FAILED = "[按文件夹] 无法移除符号链接/连接点 {path}：{error}"
LOG_PER_FOLDER_REMOVED_COUNT = "[按文件夹] 已移除 {count} 个符号链接/连接点"
LOG_LINK_DISABLED_MODS_JUNCTION = "[链接] 已禁用 Mods 连接点：{path}"
LOG_LINK_DISABLED_MODS_SYMLINK = "[链接] 已禁用 Mods 符号链接：{path}"
LOG_LINK_REMOVE_MODS_SYMLINK_FAILED = "[链接] 无法移除 Mods 符号链接：{error}"
LOG_LAUNCH_STEAM_START = "[启动] Steam 正在启动应用 ID：{steam_appid} > {game_name} > {mode}"
LOG_STEAM_LAUNCH_FAILED_FALLBACK = "[错误] 无法通过 Steam 启动：{error}\n正在回退到 EXE 启动。"
LOG_LAUNCH_STARTED_GAME = "[启动] 已启动游戏：{exe_path} {mode}"
LOG_HOTKEY_LINK_DONE = "[LINK] {game_name}：模组已成功链接到 {path}（Hotkey - 不启动）"
LOG_HOTKEY_UNLINK_DONE = "[UNLINK] {game_name}：所有模组已成功取消链接。"
LOG_ELEVATION_REQUIRED_RELAUNCH = "[错误] 需要提权：{error}\n正在尝试以管理员身份重启..."
LOG_PERMISSION_DENIED_SIMPLE = "[错误] 权限被拒绝：{error}"
LOG_LAUNCH_TOGGLE_FAILED_SIMPLE = "[错误] 无法切换模组状态或启动游戏：{error}"
LOG_TYPE_LINKING_TO = "[{mod_type}] 正在将 {count} 个模组链接到 {destination}"
LOG_MOD_LIST_ITEM = "  - {mod_name}"
LOG_LINK_MODS_DIR_MISSING = "[链接] 模组目录不存在或已禁用：{path}"
LOG_LINK_EXE_FAILED = "[链接] 无法将 {file_name} 链接到 EXE 目录：{error}"
LOG_LINK_MODS_FOLDER_NOT_EMPTY = "[链接] 无法替换现有 mods 文件夹，因为其非空：{path}"
LOG_LINK_PREP_MODS_FOLDER_FAILED = "[链接] 无法为连接点准备 Mods 文件夹：{error}"
LOG_LINK_ENABLED_MODS_SUMMARY = "[链接] 已启用模组：\n - 源：{source}\n - 已链接到 -> {destination}"
LOG_PER_FILE_CLEAN_FAILED = "[按文件] 清理失败 {path}：{error}"
LOG_PER_FILE_LINK_FAILED = "[按文件] 链接失败 {file_name}：{error}"
LOG_CONTENT_GAME_DIR_NOT_FOUND = "[内容模组] 未找到游戏 Content 目录：{path}"
LOG_CONTENT_BACKUP_FAILED = "{tag} 备份 {path} 失败，已跳过：{error}"
LOG_CONTENT_LINK_FAILED = "{tag} 链接 {file_name} 失败：{error}"
LOG_CONTENT_SKIP_JUNCTION_REAL_DIR = "{tag} 跳过连接点，真实目录已存在：{sub_name}"
LOG_CONTENT_JUNCTION_FAILED = "{tag} 创建 {sub_name} 连接点失败：{error}"
LOG_PER_FOLDER_CLEAN_FAILED = "[按文件夹] 清理失败 {path}：{error}"
LOG_PER_FOLDER_LINKED_COUNT = "[按文件夹] 已链接 {count} 个文件夹 -> {destination}"
LOG_IS_JUNCTION_FAILED = "[错误] is_junction 执行失败：{error}"
LOG_RMDIR_FAILED = "[错误] 删除目录失败 {link}：{error}"
LOG_REMOVE_FILE_LINK_FAILED = "[错误] 移除文件链接失败：{link} - {error}"
LOG_REMOVE_JUNCTION_EXCEPTION = "[错误] remove_junction 发生异常 {link}：{error}"
LOG_LAUNCH_REFRESHING_SYMLINKS = "[链接] 正在刷新符号链接..."
LOG_ASI_DLL_REMOVE_FAILED = "[ASI_DLL] 无法移除 asi/dll 符号链接 {path}：{error}"
LOG_CONTENT_GAME_DIR_NOT_FOUND_SKIP_UNLINK = "[内容模组] 未找到 game_content_dir，跳过取消链接：{path}"
LOG_CONTENT_UNLINK_FAILED = "{tag} 取消链接失败 {path}：{error}"
LOG_CONTENT_RESTORE_FAILED = "{tag} 恢复失败 {path}：{error}"
LOG_CONTENT_UNLINKED_COUNT = "{tag} 已取消链接 {count} 个模组"
LOG_CONTENT_ORPHAN_REMOVED = "[内容模组] 已移除 {count} 个孤立链接（安全清扫）"
LOG_CONTENT_PRESERVE_DIR_CREATED = "[内容模组] 已重新创建必需文件夹：{path}"
LOG_CONTENT_PRESERVE_DIR_FAILED = "[内容模组] 无法确保必需文件夹 {path}：{error}"
LOG_LINK_DISABLED_FOLDER_JUNCTION = "[链接] 已禁用文件夹连接点：{path}"
LOG_LINK_DISABLED_FOLDER_SYMLINK = "[链接] 已禁用文件夹符号链接：{path}"
LOG_LINK_REMOVE_FOLDER_FAILED = "[链接] 移除文件夹链接出错 {path}：{error}"
LOG_LINK_DISABLED_FILE_SYMLINK = "[链接] 已禁用文件符号链接：{path}"
LOG_LINK_REMOVED_FILE = "[链接] 已移除文件：{path}"
LOG_LINK_REMOVE_FILE_FAILED = "[链接] 移除文件链接出错 {path}：{error}"
LOG_ELEVATION_FAILED_SIMPLE = "[错误] 提权失败：{error}"
LOG_DEV_MODE_SETTINGS_OPEN_FAILED = "[错误] 打开开发者模式设置失败：{error}"

LOG_FORZATECH_HOISTED_PAYLOAD = "[ForzaTech] 已将 '{mod}' 的 '{prefix}' 载荷提取到游戏根目录。"
LOG_FORZATECH_RENAMED_LOADER = "[ForzaTech] 已将 '{mod}' 中的 version.dll 重命名为 {rel} 以进行代理加载。"
LOG_FORZATECH_MERGE_LINK_FAILED = "[ForzaTech] 合并链接失败 {rel}：{error}"
LOG_FORZATECH_CONFLICTS_MODS = "[ForzaTech] 存在文件冲突的模组：\n{mod_list}"
LOG_FORZATECH_CONFLICTS_RESOLVED = "[ForzaTech] 已按加载顺序解决 {count} 个文件冲突。"
LOG_FORZATECH_LOADER_NOT_FOUND = "[ForzaTech] 未找到内置加载器：{path}；已跳过。"
LOG_FORZATECH_LOADER_INJECTED = "[ForzaTech] 已安装 CZTMM 'version.dll' 代理加载器。"
LOG_FORZATECH_LOADER_INJECT_FAILED = "[ForzaTech] 注入内置加载器失败：{error}"
LOG_FORZATECH_STAGING_MISSING = "[ForzaTech] 暂存目录缺失；无内容可部署。"
LOG_FORZATECH_GAME_ROOT_NOT_FOUND = "[ForzaTech] 未找到游戏根目录：{path}"
LOG_FORZATECH_AUTOSCOPE_KEPT_ZIP = "[ForzaTech] 已将内容压缩包 '{name}' 归类到 mediapc/{reldir}/{name}。"
LOG_FORZATECH_AUTOSCOPE_ZIP_UNSCOPED = "[ForzaTech] 无法确定内容压缩包 '{name}' 的分类"
LOG_FORZATECH_AUTOSCOPE_FAILED = "[ForzaTech] 自动归类失败 '{mod}'：{error}"
LOG_FORZATECH_AUTOSCOPE_NO_MEDIA = "[ForzaTech][autoscope] 未发现已安装 media/；仅使用启发式规则。"
LOG_FORZATECH_AUTOSCOPE_INDEXING = "[ForzaTech][autoscope] 正在索引原版 media/ 树（首次运行）..."
LOG_FORZATECH_AUTOSCOPE_INDEXED = "[ForzaTech][autoscope] 已索引 {files} 个原版文件名，覆盖 {categories} 个分类。"
LOG_FORZATECH_AUTOSCOPE_UNNESTED = "[ForzaTech][autoscope] 已对已归类模组 '{mod}' 取消嵌套。"
LOG_FORZATECH_AUTOSCOPE_MEDIA_TO_MEDIAPC = "[ForzaTech][autoscope] 已将 '{mod}' 顶层 'media' 规范为 'mediapc'。"
LOG_FORZATECH_AUTOSCOPE_LOADER_SKIPPED = "[ForzaTech][autoscope] '{mod}' 含 .dll/.asi 加载器；已跳过自动归类。"
LOG_FORZATECH_AUTOSCOPE_UNSCOPED = "[ForzaTech][autoscope] 无法确定 '{mod}' 中 {count} 个文件的分类；保持未归类。"
LOG_FORZATECH_AUTOSCOPE_RESCOPED = "[ForzaTech][autoscope] 已重新归类 '{mod}'：{count} 个文件 -> mediapc/。"
LOG_FORZATECH_AUTOSCOPE_UNRESOLVED = "[ForzaTech][autoscope] '{mod}' 中 {count} 个文件未归类（未知分类）。"
LOG_FORZATECH_AUTOSCOPE_MOVE_FAILED = "[ForzaTech][autoscope] 移动失败 '{path}'：{error}"
LOG_FORZATECH_AUTOSCOPE_REZIPPED_CAR = "[ForzaTech][autoscope] 已将散文件车辆包重新应缓存 -> mediapc/Cars/{name}.zip"
LOG_FORZATECH_AUTOSCOPE_REZIP_FAILED = "[ForzaTech][autoscope] 车辆包重新应缓存失败 '{name}'：{error}"
LOG_FORZATECH_NO_ENABLED_MODS = "[ForzaTech] 无已启用模组可部署。"
LOG_FORZATECH_REUSING_OVERLAY = "[ForzaTech] 暂存模组未变化 --> 复用现有 overlay。"
LOG_FORZATECH_BUILT_OVERLAY = "[ForzaTech] 已构建合并 overlay：来自 {mods} 个模组的 {count} 个文件。"
LOG_FORZATECH_DEPLOYED = "[ForzaTech] 已将 {count} 个 overlay 对象部署到游戏中。"
LOG_FORZATECH_JUNCTION_FAILED = "[ForzaTech] 连接点失败 {name}：{error}"
LOG_FORZATECH_JUNCTION_REFRESH_FAILED = "[ForzaTech] 刷新连接点失败 {name}：{error}"
LOG_FORZATECH_OVERLAY_LINK_FAILED = "[ForzaTech] Overlay 链接失败 {path}：{error}"
LOG_FORZATECH_REMOVE_FAILED = "[ForzaTech] 无法移除 {path}：{error}"
LOG_FORZATECH_OVERLAY_CLEANUP_FAILED = "[ForzaTech] Overlay 清理失败 {path}：{error}"
LOG_FORZATECH_SWEPT_ORPHANS = "[ForzaTech] 已移除 {count} 个清单遗漏的失效 overlay 链接。"
LOG_FORZATECH_REMOVED = "[ForzaTech] 已从游戏中移除 {count} 个 overlay 对象。"

LOG_INSTALL_CONTENT_ADDED_MOD = "[{mod_type}] 已添加模组：{mod_label}"
LOG_INSTALL_CONTENT_ADDED_FOLDER_MOD = "[{mod_type}] 已添加文件夹模组：{mod_name}"
LOG_COPY_CONTENT_MOD_FOLDER_FAILED = "[错误] copy_content_mod_folder 执行失败：{error}"
LOG_INSTALL_FILE_FAILED = "[错误] 安装 {install_name} 时发生错误：{error}"

DLG_TITLE_DOWNLOADING_MODS = "正在下载模组"
DLG_TITLE_DOWNLOADING_UPDATES = "正在下载模组更新"
LBL_DOWNLOAD_ROW_DEFAULT = "下载 #{num}"
LBL_DOWNLOADS_COMPLETE = "{done} / {total} 下载已完成"
LBL_DOWNLOADS_REMAINING = "队列中剩余 {count} 项"

DLG_TITLE_RESOLVE_INSTALL = "处理安装选项"
DLG_TITLE_SELECT_FILES_PIN = "选择要固定的文件"
DLG_TITLE_SELECT_FILES_DOWNLOAD = "选择要下载的文件"
LBL_RESOLVE_HEADER = "有 {count} 个模组需要处理。\n请在下方选择后点击“应用”。"
LBL_HDR_MOD_ARCHIVE = "模组压缩包："
LBL_HDR_INSTALLED_MOD = "已安装模组："
LBL_HDR_CHOOSE_DOWNLOAD = "选择要下载的文件："
LBL_HDR_SELECT_LOADOUT_FILE = "选择用于配置集的文件："
LBL_HDR_ARCHIVE_OPTIONS = "压缩包选项：（选择要安装的文件）"
LBL_HDR_REPLACE_OR_NEW = "替换现有文件，或作为新文件安装："
LBL_UNKNOWN_MOD_INLINE = "（未知）"
LBL_FILE_NUM = "文件 {file_id}"
OPT_SKIP_DOWNLOAD = "（跳过下载）"
OPT_INSTALL_NEW = "（安装为新文件）"
OPT_INSTALL_ALL = "全部安装"
OPT_SKIP = "跳过"
MSG_BROKEN_LINK = "（链接失效 - 请手动下载）"
MSG_BROKEN_LINK_URL = "（链接失效 - 查看 {url}）"
BTN_APPLY = "应用"
BTN_INSTALL = "安装"
BTN_SKIP_ALL = "全部跳过"
BTN_USE_THIS_FILE = "使用此文件"
BTN_SELECT_FILE = "选择文件"
LBL_PIN_SELECT_HEADER = "选择要固定的文件"
LBL_CTX_MOD_NAME = "模组名称：{name}"
LBL_CTX_LOADOUT = "配置集：{name}"
LBL_CTX_INSTALLED_FILE = "已安装文件：{name}"
LBL_CTX_MOD_FILE = "模组文件：{name}"
LBL_MOD_FALLBACK = "模组 {mod_id}"
LBL_TARGET_UNKNOWN = "未知"

