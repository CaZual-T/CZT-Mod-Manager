# === Button Tooltips ===

# === Button Tooltips ===
TIP_SELECT_ALL          = "全选所有模组"
TIP_TOGGLE_ALL          = "启用/禁用所有模组"
TIP_QUICK_SAVE          = "将已启用的模组保存为配置集"
TIP_RESTORE_BACKUP      = "从备份列表恢复"
TIP_SCAN_UPDATES        = "检查所有模组的更新"
TIP_BROWSE_NEXUS        = "浏览该游戏的Nexus Mods模组库"
TIP_DOWNLOAD_SELECTED   = "下载选中的模组（Shift+D）"
TIP_DISABLE             = "禁用选中的模组"
TIP_RESTORE_DISABLED    = "恢复已禁用的模组"
TIP_DELETE              = "删除选中的模组"
TIP_CREATE_BACKUP       = "创建模组和/或mods_list.json的备份。"
TIP_HIDE_DISABLED       = "从列表/网格中隐藏已禁用的模组"
TIP_VIEW_LIST           = "列表视图"
TIP_VIEW_GRID           = "网格视图"

# === Main Tab Labels ===
TAB_TITLE_MANAGE_MODS   = "管理模组"
LBL_HIDE_DISABLED       = "隐藏已禁用项"

# === Loadouts Dropdown ===
BTN_LOADOUTS = "配置集"
TIP_LOADOUTS = (
    "1.) 先禁用所有模组，再启用你想要加入新配置集的模组。\n"
    "2.) 点击保存图标，将已启用的模组保存为配置集文件。\n"
    " - 已保存的配置集可随时从该下拉菜单切换。\n"
    " - 在“全部管理”中，每个配置集行都有重命名、复制文件和下载图标。\n"
    " - 可通过“从文件导入”功能，从其他JSON文件添加配置集。\n"
    " - 你也可以点击“全部管理”删除/编辑配置集信息。"
)
LBL_LOADOUTS_HEADER_SAVED = "已保存的配置集"
LBL_LOADOUTS_EMPTY = "无配置集"
LBL_LOADOUTS_HEADER_MANAGE = "管理"
BTN_LOADOUT_MANAGER = "配置集管理器"
LBL_LOADOUTS_HEADER_QUICK_ACTIONS = "快捷操作"
BTN_IMPORT_LOADOUT_FILE = "导入配置集文件"
BTN_IMPORT_DOWNLOAD_LOADOUT = "导入并下载配置集"

# === Search Bar ===
SEARCH_PLACEHOLDER = "搜索模组 : {profile}"

# === Sort / Filter ===
TIP_SORT_BY_MOD_NAME    = "按模组名称排序"
TIP_SORT_BY_CREATOR     = "按创作者排序"
BTN_SORT_FILTER         = "排序/筛选"

SORT_SECTION_DISPLAY_NAME   = "显示名称"
SORT_AZ_DISPLAY_NAME        = "显示名称 从A到Z"
SORT_ZA_DISPLAY_NAME        = "显示名称 从Z到A"

SORT_SECTION_CREATOR    = "创作者"
SORT_AZ_CREATOR         = "创作者 从A到Z"
SORT_ZA_CREATOR         = "创作者 从Z到A"

SORT_SECTION_CATEGORY   = "分类"
SORT_AZ_CATEGORY        = "分类 从A到Z"
SORT_ZA_CATEGORY        = "分类 从Z到A"

SORT_SECTION_STATUS         = "状态"
SORT_FAVORITES              = "收藏项（置顶）"
SORT_UPDATES_AVAILABLE      = "可更新项（置顶）"
SORT_MOD_HIDDEN             = "隐藏的模组（置顶）"
SORT_MOD_REMOVED            = "已移除的模组（置顶）"
SORT_ENABLED                = "已启用项（置顶）"
SORT_DISABLED               = "已禁用项（置顶）"

SORT_SECTION_FILE_SIZE  = "文件大小"
SORT_SMALLEST           = "按从小到大排序"
SORT_LARGEST            = "按从大到小排序"

SORT_SECTION_INSTALL_DATE   = "安装日期"
SORT_NEW_TO_OLD             = "按安装时间 从新到旧"
SORT_OLD_TO_NEW             = "按安装时间 从旧到新"

# === Delete Mods Dialog ===
DLG_DELETE_TITLE            = "删除 ({count}) 个模组？"
BTN_YES_DELETE              = "确认删除"
BTN_CANCEL                  = "取消"
MSG_NO_MODS_SELECTED_DELETE = "未选中任何待删除的模组文件。"
MSG_ENABLED_MODS_SKIPPED    = "由于“保护已启用的模组不被删除”功能已开启，已跳过启用状态的模组。"
MSG_MODS_DIR_NOT_FOUND      = "未找到模组目录，请设置有效的根文件夹。"

# === Per-Mod Delete ===
DLG_DELETE_MOD_TITLE        = "删除模组"
MSG_CONFIRM_DELETE_MOD      = "确定删除该模组？\n{filename}"

# === Disable Mods ===
MSG_NO_MODS_SELECTED_DISABLE    = "未选中任何待禁用的模组文件。"
DLG_DISABLE_TITLE               = "禁用模组"
MSG_CONFIRM_DISABLE             = "确定要禁用选中的模组吗？"
MSG_DISABLED_WITH_ERRORS        = "已禁用 {moved} 个模组，但出现 {errors} 个错误。"
MSG_DISABLED_OK                 = "已禁用 {moved} 个模组文件。"

# === Restore Disabled Mods Dialog ===
MSG_NO_DISABLED_FOLDER          = "未找到已禁用模组的文件夹。"
MSG_NO_MODS_TO_RESTORE          = "已禁用文件夹中无待恢复的模组。"
DLG_RESTORE_TITLE               = "恢复已禁用模组"
LBL_RESTORE_CONFIRM             = "确定恢复这些模组吗？"
BTN_SELECT_ALL                  = "全选"
BTN_DESELECT_ALL                = "取消全选"
BTN_RESTORE_SELECTED            = "恢复选中项"
MSG_RESTORED_WITH_ERRORS        = "已恢复 {restored} 个模组，但出现 {errors} 个错误。"
MSG_RESTORED_OK                 = "已恢复 {restored} 个模组文件。"

# === Toggle/Log Messages ===
LOG_TYPE_DISABLED       = "[{mod_type}] 已禁用 {count} 个模组"
LOG_TYPE_ENABLED        = "[{mod_type}] 已启用 {count} 个模组"
LOG_MOD_LIST_ITEM       = "  - {mod_name}"
LOG_DISABLE_TOTAL       = "[禁用] 已成功禁用 {count} 个模组。"
LOG_DISABLE_FAILED_ITEM = "[{mod_type}] 禁用模组 {mod_name} 失败：{error}"
LOG_ENABLE_FAILED_ITEM  = "[{mod_type}] 启用模组 {mod_name} 失败：{error}"

# === Mod Links ===
MSG_NO_MOD_LINKS        = "未找到可打开的模组链接。"
MSG_CONFIRM_OPEN_LINKS  = "确定打开 {count} 个选中模组的链接吗？"
MSG_OPEN_LINKS_INFO     = "此操作将打开 {count} 个浏览器标签页。"

# === Mod Info Popup ===
TIP_REFRESH_NEXUS       = "刷新Nexus信息并重新下载图片"
TIP_DOWNLOAD_NEXUS      = "从Nexus下载最新文件"
TIP_DOWNLOAD_MOD        = "下载模组"
TIP_DELETE_MOD          = "删除模组"
LBL_NEXUS_DESCRIPTION   = "描述"
LBL_NEXUS_METADATA      = "模组统计"
LBL_NEXUS_DOWNLOADS     = "下载次数"
LBL_NEXUS_UNIQUE_DOWNLOADS = "独立下载"
LBL_NEXUS_ENDORSEMENTS  = "认可数"
LBL_NEXUS_UPLOAD_DATE   = "上传日期"
LBL_NEXUS_UPDATED_DATE  = "最后更新"
LBL_NEXUS_CATEGORY      = "分类"
LBL_NEXUS_TAGS          = "标签"
TIP_NEXUS_DOWNLOADS     = "总下载次数"
TIP_NEXUS_UNIQUE_DOWNLOADS = "独立下载次数"
TIP_NEXUS_ENDORSEMENTS  = "认可数量"
TIP_NEXUS_UPLOAD_DATE   = "模组首次上传日期"
TIP_NEXUS_UPDATED_DATE  = "模组最近更新日期"
BTN_CHECK_FOR_UPDATE    = "检查更新"
DLG_TITLE_EDIT_MOD_ENTRY = "编辑模组条目"
LBL_EDIT_NAME           = "名称："
LBL_EDIT_CREATOR        = "作者："
LBL_EDIT_CATEGORY       = "分类："
LBL_EDIT_FILE           = "文件："
LBL_EDIT_SIZE           = "大小："
LBL_EDIT_VERSION        = "版本："
LBL_EDIT_LOCAL_VERSION  = "本地版本："
LBL_EDIT_LATEST_VERSION = "最新版本："
LBL_EDIT_INSTALL_DATE   = "安装日期："
LBL_EDIT_STATUS         = "状态："
LBL_EDIT_DISPLAY_NAME   = "显示名称"
LBL_EDIT_NEXUS_ID_URL   = "Nexus 模组 ID 或 URL"
BTN_SAVE                = "保存"
FMT_LOCAL_LATEST        = "本地：{local_version} | 最新：{latest_version}"
LBL_STATUS_ENABLED      = "已启用"
LBL_STATUS_DISABLED     = "已禁用"
LBL_NO_IMAGE            = "无图片"
LBL_ROW_CATEGORY        = "分类"
LBL_ROW_SIZE            = "大小"
LBL_ROW_FILE            = "文件"
LBL_ROW_LOCAL           = "本地"
LBL_ROW_LATEST          = "最新"
LBL_ROW_INSTALL         = "安装"
LBL_ROW_MOD_ID          = "模组 ID"
TAG_VALID_UP_TO_DATE    = "有效且最新"
TAG_UPDATE_REMOVED      = "已移除"
TAG_UPDATE_HIDDEN       = "已隐藏"
TAG_UPDATE_AVAILABLE    = "有可用更新"
TAG_REMOVED_DELETED     = "已移除/已删除"

# === Force Update Options Dialog ===
DLG_FORCE_UPDATE_TITLE      = "强制更新选项"
LBL_FORCE_UPDATE_PROMPT     = "你想要强制更新哪些属性？"
CB_DISPLAY_NAME             = "显示名称"
CB_THUMBNAIL                = "缩略图/图片"
CB_INSTALL_DATE             = "安装日期"
CB_LOCAL_VERSION            = "本地版本（适用于data2.pak、data3.pak等格式的模组）"
BTN_APPLY                   = "应用"
