# Main Menu Tab - English strings

# General
STATUS_GAME_NOT_DETECTED = "GAME NOT DETECTED"

# Main tab button tooltips
TIP_BTN_GAME_BROWSE = "Open the current profiles mod folder, and symlink destination."
TIP_BTN_OPEN_CUSTOM_SETTINGS = "Startup options and Custom settings."
TIP_BTN_FIRST_TIME_SETUP = "Create Root, Install UnRAR, Set API Key."
TIP_BTN_SELECT_ALL = "[SELECT/DESELECT ALL]"
TIP_BTN_DELETE_SELECTED = (
    "Delete selected mod(s) from the install source folder.\n"
    "> This cannot be undone! (there is a warning prompt before deletion)"
)
TIP_BTN_INSTALL_SELECTED = (
    "Manually install selected mod(s) to the current profile.\n"
    "> Metadata is not saved during manual installs.\n"
    "   > If the mod you're installing is new, then you will have to open the manager tab after install,.. \n"
    "   > ...right click the file, and set the mods nexus ID/URL manually so CZT can retrieve and save the mods metadata.\n"
    "> You can safely install existing mods to update them.\n"
)
TIP_PATH_MODE_MANUAL = (
    "ENABLED = User can manually set paths for EXE and where mods should be linked to @ launch.\n"
    "[IMPORTANT] Read the log that appears after selecting this option for more information."
)
TIP_PATH_MODE_STEAM = (
    "ENABLED (DEFAULT) = CZT will utilize your STEAM library.vdf to automatically set all required paths.\n"
    "Click 'Detect Steam' to use auto pathing."
)
TIP_BTN_MANAGE_MODS = "Join the CZT Mod Manager Discord for updates and support."
TIP_BTN_CLEAN_MOD_LIST = (
    "4 Options:\n"
    "- Delete existing symlinks for profile.\n"
    "- Delete crash monitor logs.\n"
    "- Delete download history.\n"
    "- Remove stale entries in mod list file."
)
TIP_BTN_DONATIONS = "Thank you for using CZT!\nClick here to open the donations page (Paypal)"
TIP_BTN_UPDATE_CZT = (
    "Click this to open the CZT Mod Manager instructions.\n\n"
    "[HOTKEYS]\n"
    "- Press SHIFT + H to show available hotkeys.\n"
    "- Press F2 to open the Load Order menu."
)

# Main tab labels
LBL_PATH_MODE_MANUAL = "Manual"
LBL_PATH_MODE_STEAM = "Steam"
TAB_TITLE_MAIN_MENU = "Main Menu"

# Main tab button/section labels
LBL_PATH_MODES = "Path Modes"
LBL_BTN_DETECT_STEAM = "Detect Steam"
LBL_BTN_SAVE_CONFIG = "Save Config"
LBL_BTN_SET_INSTALL_DIRECTORY = "Set Install Path"
LBL_BTN_SET_EXE_PATH = "Set EXE Path"
LBL_BTN_LAUNCH_GAME = "Launch Game"
LBL_BTN_BROWSE = "Browse"
LBL_BTN_SETTINGS = "Settings"
LBL_BTN_SETUP = "Setup"
LBL_BTN_GUIDE = "Guide"
LBL_BTN_DISCORD = "Discord"
LBL_BTN_CLEAN = "Clean"
LBL_BTN_DONATIONS = "Donations"
LBL_BTN_PATCH_NOTES = "Patch Notes"
TIP_BTN_PATCH_NOTES = "View CZT Mod Manager patch notes and check for updates."

# Main tab storage stats labels
LBL_STORAGE_OVERVIEW = "[CZT Overview]"
LBL_STATS_DISK_USAGE_TOTAL = "CZT - Storage Used:"
LBL_STATS_MODS_ENABLED = "Mods Enabled: {count}"
LBL_STATS_MODS_DISABLED = "Mods Disabled: {count}"
LBL_STATS_MODS_ENABLED_VALUE_FMT = "size on disk: {size}"
LBL_STATS_MODS_DISABLED_VALUE_FMT = "size on disk: {size}"
LBL_STATS_UPDATES_AVAILABLE = "Updates Available: {count}"
LBL_STATS_APP_CPU_USAGE = "CZT - CPU Usage:"
LBL_STATS_APP_RAM_USAGE = "CZT - RAM Usage:"
LBL_STATS_NETWORK_SPEED = "Network Speed:"
LBL_STATS_DISK_RW_SPEED = "Read | Write Speed:"
LBL_STATS_DISK_TRANSFER_RATE = "Transfer Rate:"
LBL_STATS_UPDATES_VALUE_FMT = "scanned: {date}"
LBL_STATS_LAST_CHECKED_NEVER = "never"
LBL_STATS_NETWORK_VALUE_FMT = "↑ {sent} | ↓ {recv}"
LBL_STATS_DISK_RW_VALUE_FMT = "R {read} | W {write}"
LBL_STATS_DISK_TRANSFER_VALUE_FMT = "{total}"
LBL_STATS_UNAVAILABLE = "Unavailable"

TIP_STORAGE_OVERVIEW_CUSTOMIZE = "Click to customize CZT Overview widgets: reorder rows or swap what is displayed."
TIP_OVERVIEW_ITEM_UPDATES_AVAILABLE = "Shows how many mods have updates available.\n ↳ scanned: (date) is the most recent full/auto scan date."
TIP_OVERVIEW_ITEM_MODS_ENABLED = "Enabled mods (count) for the current profile:\n ↳ total size of the current profile's 'enabled' mods folder."
TIP_OVERVIEW_ITEM_MODS_DISABLED = "Disabled mods (count) for the current profile:\n ↳ total size of the current profile's 'disabled' mods folder."
TIP_OVERVIEW_ITEM_DISK_USAGE_TOTAL = "Size of the CZT root folder / Capacity of the drive that hosts your CZT root folder."
TIP_OVERVIEW_ITEM_APP_CPU_USAGE = "CZT CPU usage | system CPU usage | current CPU clock speed."
TIP_OVERVIEW_ITEM_APP_RAM_USAGE = "CZT RAM usage | total system RAM."
TIP_OVERVIEW_ITEM_NETWORK_SPEED = "Live system network upload and download speed."
TIP_OVERVIEW_ITEM_DISK_RW_SPEED = "Live read and write speed for selected drive (drive)."
TIP_OVERVIEW_ITEM_DISK_TRANSFER_RATE = "Live combined read + write transfer rate for selected drive (drive)."

DLG_TITLE_STORAGE_WIDGETS = "Customize CZT Overview"
DLG_STORAGE_WIDGETS_DESC = "Drag items to reorder. Checked rows are shown in CZT Overview."
LBL_STORAGE_WIDGETS_DRIVE_LABEL = "Select drive to use for R/W and Transfer Rate overview:"
LBL_STORAGE_WIDGETS_DRIVE_ALL = "All"
BTN_STORAGE_WIDGETS_RESTORE_DEFAULT = "Restore Default"
BTN_STORAGE_WIDGETS_CANCEL = "Cancel"
BTN_STORAGE_WIDGETS_APPLY = "Apply"
MSG_STORAGE_WIDGETS_NONE_SELECTED_TITLE = "No Widgets Selected"
MSG_STORAGE_WIDGETS_NONE_SELECTED_BODY = "Select at least one widget to display."
MSG_STORAGE_WIDGETS_TOO_MANY_TITLE = "Too Many Widgets"
MSG_STORAGE_WIDGETS_TOO_MANY_BODY = "This panel supports up to {max_visible} visible widgets at a time."

# Main tab setup popup titles
DLG_TITLE_CUSTOM_SETTINGS = "Custom Settings"
DLG_TITLE_FIRST_TIME_SETUP = "First Time Setup"

# Main tab log messages
LOG_ROOT_MISSING = (
    "\n❌ [ERROR] Root folder not set/folder does not exist! \n"
    "⚠️ [WARNING] Any settings you attempt to apply will not be saved until root is created!\n"
    "❓ [HINT] Click the 'SETUP' button above...\n"
    "  1: Click 'CREATE ROOT' and select your preferred drive to set up required folders.\n"
    "  2: Click 'INSTALL UNRAR' after creating root folders.\n"
    "    - Click install unrar again after it installs to set its path.\n"
    "  3: Restart CZT after installing UnRAR.exe\n"
)

# Clean utility messages
MSG_ROOT_NOT_SET_CLEAN = "Root folder not set. Cannot clean mod list."
MSG_NO_VALID_INSTALL_DIR = (
    "No valid install directory set!\n \n- Path Mode [STEAM]:\n   > Click 'Detect Steam'\n "
    "\n- Path Mode [Manual]:\n   > Click 'SET INSTALL' and 'SET EXE' to configure."
)
LOG_CLEAN_HISTORY_CLEARED = "[CLEAN] Cleared history in {history_path}."
LOG_CLEAN_HISTORY_CLEAR_FAILED = "[CLEAN] Failed to clear {history_name} at {history_path}: {error}"
LOG_CLEAN_CRASH_LOG_CLEARED = "[CLEAN] Cleared crash monitor logs: {log_path}"
LOG_CLEAN_CRASH_LOG_CLEAR_FAILED = "[CLEAN] Failed to clear crash monitor log {log_name} at {log_path}: {error}"
LOG_CLEAN_MOD_LIST_UPDATE_FAILED = "[CLEAN] Failed to update mod list: {error}"
LOG_CLEAN_STALE_ENTRIES_REMOVED = "[CLEAN] Removed {removed} stale mod entry(s) from mod_list.json for profile '{profile_name}'."
LOG_CLEAN_NO_OPTIONS_SELECTED = "[CLEAN] No options selected."
LOG_PER_FILE_SYMLINK_DISABLED = "[PER-FILE] Disabled symlink: {path}"
LOG_PER_FILE_SYMLINK_REMOVE_FAILED = "[PER-FILE] Could not remove symlink {path}: {error}"
LOG_PER_FOLDER_LINK_DISABLED = "[PER-FOLDER] Disabled symlink/junction: {path}"
LOG_PER_FOLDER_LINK_REMOVE_FAILED = "[PER-FOLDER] Could not remove symlink/junction {path}: {error}"
LOG_LINK_MODS_JUNCTION_DISABLED = "[LINK] Disabled Mods junction: {path}"
LOG_LINK_MODS_SYMLINK_DISABLED = "[LINK] Disabled Mods symlink: {path}"
LOG_LINK_MODS_SYMLINK_REMOVE_FAILED = "[LINK] Could not remove Mods symlink: {error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED = "[CLEAN] Removed existing symlinks for profile '{profile_name}'."
LOG_CLEAN_EXE_TYPE_LINKS_REMOVED = "[{mod_type}] Unlinked {count} mod(s)."
LOG_CLEAN_TYPE_SYMLINKS_REMOVED = "[{mod_type}] Unlinked {count} mod(s)."
LOG_CLEAN_PER_FILE_REMOVE_FAILED_SUMMARY = "[CLEAN] Failed to remove {count} mod symlink(s)."
LOG_CLEAN_PER_FOLDER_LINKS_REMOVED = "[PER-FOLDER] Unlinked {count} mod(s)."
LOG_CLEAN_PER_FOLDER_REMOVE_FAILED_SUMMARY = "[CLEAN] Failed to remove {count} mod folder link(s)."
LOG_CLEAN_ERRORS_OMITTED = "[CLEAN] ...and {count} more error(s)."
LOG_CLEAN_CONTENT_LINKS_REMOVE_FAILED = "[CLEAN] Could not remove content mod links: {error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED_SUMMARY = "[CLEAN] Removed {count} existing link(s) for profile '{profile_name}'."

# Clean options popup
DLG_TITLE_CLEAN_OPTIONS = "Cleaning Options"
CLEAN_OPTIONS_PROMPT = "Select one or multiple options:"
CLEAN_OPTION_STALE_ENTRIES = "Remove stale entries from mods_list.json."
CLEAN_OPTION_BROWSER_HISTORY = "Delete local CZT browser download history."
CLEAN_OPTION_CRASH_LOGS = "Delete crash monitor logs."
CLEAN_OPTION_SYMLINKS = "Delete existing symlinks for the current profile."
CLEAN_OPTIONS_APPLY = "Apply"
CLEAN_OPTIONS_CANCEL = "Cancel"

# First-time setup popup
LBL_FTS_CREATE_ROOT = "Create Root"
LBL_FTS_INSTALL_UNRAR = "Install UnRAR"
LBL_FTS_NEXUS_API_KEY = "Nexus API Key"
LBL_FTS_SAVE_KEY = "Save Key"
LBL_FTS_SET_PATH = "Set Path"
LBL_FTS_OPEN_ROOT = "Open Root"

TIP_CREATE_ROOT = (
    "Click 'Create Root', Then select your preferred drive.\n"
    "CZT will AUTO create root folders and set source path."
)
TIP_INSTALL_UNRAR = (
    "Download and install UnRAR to enable mod extraction.\n"
    "UnRAR.exe can live anywhere on your PC - the czt_tools folder is just the default.\n"
    "After installing, click again to auto-detect it, or use 'Set Path' to browse or paste the path."
)
TIP_BROWSE_UNRAR = (
    "Set the path to UnRAR.exe (or WinRAR.exe) located anywhere on your PC.\n"
    "Browse to the file, or paste its full path into the box and press Enter to save."
)
TIP_NEXUS_API = (
    "Get your Nexus Mods API key\n"
    "The nexus website will open\n"
    "Scroll to the bottom of opened page for your key"
)
MSG_API_KEY_SAVED_TITLE = "API Key Saved"
MSG_API_KEY_SAVED_TEXT = "Nexus API Key saved to config."
MSG_UNRAR_PATH_INVALID_TITLE = "Invalid UnRAR Path"
MSG_UNRAR_PATH_INVALID_TEXT = (
    "That path doesn't point to a valid UnRAR.exe or WinRAR.exe.\n"
    "Browse to the file, or paste its full path and press Enter."
)

# Custom settings popup

SETTINGS_RESET_BUTTON_TEXT = "Reset"
SETTINGS_FONT_BUTTON_VALUE_TEXT = "{label}: {value}"

# UI text overrides - maps widget objectName to display text
SETTINGS_UI_TEXT = {
    # Group headers
    "General_Settings": "General Settings",
    "groupBox": "Advanced Settings",
    "startupGroup_2": "Color Options",
    "startupGroup_3": "Font Options",
    # Color button labels
    "groupBoxBorderColorBtn": "Log Box Border Color",
    "logBoxBackgroundColorBtn": "Log Box Background Color",
    "storageOverviewBorderColorBtn": "CZT Overview Border",
    "lineSeparatorColorBtn": "Line Separator Color",
    "selectedModBorderColorBtn": "Selected Mod Border Color",
    "entryBorderColorBtn": "Entry Border Color",
    "entrySelectedBorderColorBtn": "Selected Entry Border",
    "entryBorderHoverColorBtn": "Entry Border Hover",
    "entryBackgroundColorBtn": "Entry Background Color",
    "descriptionBackgroundColorBtn": "Description Background",
    "descriptionBorderColorBtn": "Description Border",
    "installListBorderColorBtn": "Install List Border",
    "scrollbarHandleBgBtn": "Scrollbar Handle BG",
    "scrollbarHandleHoverBgBtn": "Scrollbar Handle Hover BG",
    "scrollbarBorderBtn": "Scrollbar Handle Border",
    "tabBgColorBtn": "Tab Background Color",
    "tabHoverBgBtn": "Tab Hover Background",
    "tabSelectedBgBtn": "Selected Tab Background",
    "tabTextColorBtn": "Tab Text Color",
    "tabHoverTextBtn": "Tab Hover Text Color",
    "tabSelectedTextColorBtn": "Selected Tab Text Color",
    "customTabBorderColorBtn": "Window Border Color",
    "modListBorderColorBtn": "Mod List Border Color",
    "progressBarColorBtn": "Progress Bar Color",
    "customColorLogBoxTextBtn": "Log Box Text Color",
    "dropdownDisplayColorBtn": "Dropdown Display Color",
    "dropdownHoverColorBtn": "Dropdown Hover Color",
    "dropdownBorderColorBtn": "Dropdown Border Color",
    "dropdownBorderHoverColorBtn": "Dropdown Border Hover",
    "mainMenuVerticalBtnDisplayColorBtn": "Main Menu Vertical Btn Color",
    "mainMenuVerticalBtnHoverColorBtn": "Main Menu Vertical Btn Hover",
    "mainMenuVerticalBtnBorderColorBtn": "Main Menu Vertical Btn Border",
    "mainMenuVerticalBtnBorderHoverColorBtn": "Main Menu Vertical Btn Border Hover",
    "mainMenuHorizontalBtnDisplayColorBtn": "Main Menu Row Btn Color",
    "mainMenuHorizontalBtnHoverColorBtn": "Main Menu Row Btn Hover",
    "mainMenuHorizontalBtnBorderColorBtn": "Main Menu Row Btn Border",
    "mainMenuHorizontalBtnBorderHoverColorBtn": "Main Menu Row Btn Border Hover",
    "manageTopBtnDisplayColorBtn": "Manage Top Btn Color",
    "manageTopBtnHoverColorBtn": "Manage Top Btn Hover",
    "manageTopBtnBorderColorBtn": "Manage Top Btn Border",
    "manageTopBtnBorderHoverColorBtn": "Manage Top Btn Border Hover",
    "deleteBtnDisplayColorBtn": "Delete Btn Color",
    "deleteBtnHoverColorBtn": "Delete Btn Hover",
    "deleteBtnBorderColorBtn": "Delete Btn Border",
    "deleteBtnBorderHoverColorBtn": "Delete Btn Border Hover",
    "deleteBtnTextColorBtn": "Delete Btn Text Color",
    "deleteBtnTextHoverColorBtn": "Delete Btn Text Hover",
    "saveBtnDisplayColorBtn": "Save Btn Color",
    "saveBtnHoverColorBtn": "Save Btn Hover",
    "saveBtnBorderColorBtn": "Save Btn Border",
    "saveBtnBorderHoverColorBtn": "Save Btn Border Hover",
    "saveBtnTextColorBtn": "Save Btn Text Color",
    "saveBtnTextHoverColorBtn": "Save Btn Text Hover",
    "actionBtnDisplayColorBtn": "Action Btn Color",
    "actionBtnHoverColorBtn": "Action Btn Hover",
    "actionBtnBorderColorBtn": "Action Btn Border",
    "actionBtnBorderHoverColorBtn": "Action Btn Border Hover",
    "actionBtnTextColorBtn": "Action Btn Text Color",
    "actionBtnTextHoverColorBtn": "Action Btn Text Hover",
    "okBtnDisplayColorBtn": "OK Btn Color",
    "okBtnHoverColorBtn": "OK Btn Hover",
    "okBtnBorderColorBtn": "OK Btn Border",
    "okBtnBorderHoverColorBtn": "OK Btn Border Hover",
    "okBtnTextColorBtn": "OK Btn Text Color",
    "okBtnTextHoverColorBtn": "OK Btn Text Hover",
    "cancelBtnDisplayColorBtn": "Cancel Btn Color",
    "cancelBtnHoverColorBtn": "Cancel Btn Hover",
    "cancelBtnBorderColorBtn": "Cancel Btn Border",
    "cancelBtnBorderHoverColorBtn": "Cancel Btn Border Hover",
    "cancelBtnTextColorBtn": "Cancel Btn Text Color",
    "cancelBtnTextHoverColorBtn": "Cancel Btn Text Hover",
    "launchGameBtnDisplayColorBtn": "Launch Game Btn Color",
    "launchGameBtnHoverColorBtn": "Launch Game Btn Hover",
    "launchGameBtnBorderColorBtn": "Launch Game Btn Border",
    "launchGameBtnBorderHoverColorBtn": "Launch Game Btn Border Hover",
    "launchGameBtnTextColorBtn": "Launch Game Btn Text Color",
    "launchGameBtnTextHoverColorBtn": "Launch Game Btn Text Hover",
    "miscBtnTextColorBtn": "Misc Button Text Color",
    "miscBtnTextHoverColorBtn": "Misc Button Text Hover Color",
    "miscBtnColorDisplayBtn": "Misc Button Display Color",
    "miscBtnColorHoverBtn": "Misc Button Hover Color",
    "miscBtnColorBorderBtn": "Misc Button Border Color",
    "miscBtnBorderHoverColorBtn": "Misc Button Border Hover",
    # Font button labels
    "customFontHeaderIBtn": "Tab Font",
    "customFontHeaderMBtn": "Label Font",
    "customFontLogBoxBtn": "Log Box Font",
    "customFontLabelsBtn": "Mod List Font",
    "customFontTooltipBtn": "Tooltip Font",
    "customFontCbBtn": "Checkbox Font",
    "customFontButtonBtn": "Button Font",
    "customFontMainMenuVerticalButtonsBtn": "Main Menu Left Btns Font",
    "customFontMainMenuTopButtonsBtn": "Main Menu Top Btns Font",
    "customFontManageTabButtonsBtn": "Manage Tab Btns Font",
    # General labels / checkboxes
    "generalUseDownloadsAsSourceCheckBox": "Use downloads folder as source.",
    "generalUseModsSourceAsSourceCheckBox": "Use mod_staging folder as source.",
    "generalUseBuiltInNexusBrowserCheckBox": "Open mod links using CZT's custom browser window.",
    "generalRegisterNxmHandlerCheckBox": "Set as handler for 'Mod Manager Download' button.",
    "generalUpdateOnlyEnabledModsCheckBox": "Only check enabled mods for updates during scans.",
    "generalDownloadModsAfterScanCheckBox": "Auto download mods flagged as 'update available'.",
    "generalDeleteAfterInstalledCheckBox": "Auto delete archives from source after mod installation.",
    "generalProtectEnabledModsFromDeletionCheckBox": "Protect enabled mods from deletion.",
    "manageHomeCheckBox": "Set 'Manage' as home tab.",
    "installHomeCheckBox": "Set 'Main Menu' as home tab.",
    "enableCztBetaAlertsCheckBox": "Enable alerts for CZT beta releases.",
    "scanUpdatesOnStartupCheckBox": "Scan mods for updates on startup.",
    "updateScanCacheHoursLabel": "Startup scan frequency (hrs):",
    "musicLabel": "Track:",
    "menuMusicVolumeLabel": "Volume:",
    "menuMusicCheckBox": "Enable menu music.",
    "pauseMenuMusicAfterLaunchCheckBox": "Pause menu music after launching a game.",
    "buttonHoverCheckBox": "Enable button 'hover' sound.",
    "buttonClickCheckBox": "Enable button 'click' sound.",
    "languageLabel": "Language:",
    # Advanced labels / checkboxes
    "downloadParallelWorkersLabel": "Max downloads allowed at once:",
    "backgroundThreadsLabel": "Max background threads:",
    "installLiveLogThresholdLabel": "Live progress log threshold (MB):",
    "installCacheSessionCheckBox": "Cache file selection (per session only).",
    "installCachePersistentCheckBox": "Cache file selection (persistent).",
    "installCacheAutoClearCheckBox": "Auto clear persistent local cache file.",
    "installCacheMaxSizeLabel": "Auto clear threshold (KB):",
    "similarityPrimaryTokensLabel": "Primary minimum token overlap:",
    "similarityPrimaryRatioLabel": "Primary match ratio:",
    "generalEnableSecondaryInstallSafetyCheckBox": "Enable secondary install safety.",
    "similaritySecondaryTokensLabel": "Secondary minimum token overlap:",
    "similaritySecondaryRatioLabel": "Secondary match ratio:",
    "saveButton": "Save",
}

SETTINGS_HELP_TEXT = (
    "The settings below control how strict CZT is when looking for possible replacement files during install. "
    "Mod creators often rename files slightly between versions, so CZT compares incoming files against files "
    "you already have and prompts you when it finds a likely match.\n"
    "Exact filename matches are replaced automatically. The settings below are only used for near matches where "
    "the names are different but still look related.\n\n"
    "Token overlap is how many parts of a filename must match before it is treated as a candidate.\n"
    "Ratio controls strictness: lower values show more candidates (broader but less precise), while higher values "
    "show fewer (more precise, but can miss valid updates if set too high).\n\n"
    "Secondary safety is optional and acts as a wider fallback check to catch edge cases the primary check might miss."
)

TIP_REGISTER_NXM_HANDLER = (
    "When enabled, clicking the 'Mod Manager Download' button on a mod page results in the file being\n"
    "sent directly to CZT for download and install. All mod metadata will be saved at the time of install.\n"
    "- Works for all Nexus account types (free and premium).\n"
    "DO NOT DISABLE UNLESS YOU RUN INTO ISSUES WITH CZT OVERRIDING OTHER MANAGERS AT THE TIME OF DOWNLOAD."
)

TIP_OPEN_IN_APP_BROWSER = (
    "When enabled, clicking the browse, mod images, or the link icon will open nexus within CZT's built-in browser.\n"
    "When disabled, all links open in your default external browser."
)

TIP_INSTALL_LIVE_LOG_THRESHOLD = (
    "Minimum install size before CZT shows live install progress within the log box.\n"
    "Just a useful visual for large files that make the app 'feel' like nothing is happening."
)

TIP_DOWNLOAD_PARALLEL_WORKERS = (
    "Max amount of downloads CZT can run in parallel.\n"
    "⚠️ Higher values can speed up batch downloads, but may cause instability."
)

TIP_BACKGROUND_THREADS = (
    "Background thread limit.\n"
    "Update Scan/Loadout/Install operations are affected by this setting.\n"
    "Higher values allow more tasks to run simultaneously.\n"
    "⚠️ Higher values can speed up actions, but may cause instability."
)

TIP_UPDATE_SCAN_CACHE_HOURS = (
    "- If you restart the app a lot and want to prevent a full scan on startup, set this to a higher value like 6.\n"
    "- If you want to do a full scan on every startup (or every time you click check all mods for updates) set this to 0.\n"
    "- DOES NOT AFFECT HOW FREQUENTLY YOU CAN USE THE INDIVIDUAL UPDATE CHECK IN THE \"EDIT MOD ENTRY\" WINDOW."
)

TIP_SAVE_SETTINGS = (
    "Save settings and apply changes.\n"
    "> Note: Certain settings may require a restart to take full effect."
)

# Reset button tooltips
TIP_RESET_LIVE_LOG_THRESHOLD = "Reset live progress threshold to default."
TIP_RESET_DOWNLOAD_WORKERS = "Reset max concurrent downloads to default."
TIP_RESET_BACKGROUND_THREADS = "Reset max background threads to default."
TIP_RESET_PRIMARY_TOKENS = "Reset primary token overlap to default."
TIP_RESET_PRIMARY_RATIO = "Reset primary ratio to default."
TIP_RESET_SECONDARY_TOKENS = "Reset secondary token overlap to default."
TIP_RESET_SECONDARY_RATIO = "Reset secondary ratio to default."

# Install cache tooltips
TIP_CACHE_SESSION = (
    "Store archive file selection from familiar archives until CZT closes.\n"
    "Use refresh to clear the sessions cached choices."
)
TIP_CACHE_PERSISTENT = (
    "Store archive file selection to file so they persist after restart.\n"
    "Use refresh to clear the local cache file."
)
TIP_CACHE_AUTO_CLEAR = "When enabled, persistent cache is auto-cleared once it exceeds the limit below."
TIP_CACHE_MAX_SIZE = "Maximum persistent cache file size in KB before auto-clear runs."
TIP_CLEAR_SESSION_CACHE = "Clear session file-selection cache."
TIP_CLEAR_PERSISTENT_CACHE = "Clear persistent file-selection cache."
TIP_RESET_CACHE_SIZE_LIMIT = "Reset persistent cache size limit to default."

# Music dropdown fallback
DEFAULT_MUSIC_TRACK = "Default"

# Language dropdown
LBL_LANGUAGE = "Language:"
TIP_LANGUAGE_DROPDOWN = (
    "Select the display language for CZT Mod Manager.\n"
    "Additional language packs can be added to your root folder > CZT Mod Manager/plugins/language_packs/.\n"
    "Changes take effect after restarting the application."
)
MSG_LANGUAGE_RESTART = "Language changed. Please restart CZT Mod Manager for the change to take full effect."

TIP_MENU_MUSIC_DROPDOWN = (
    "Select the background music track for the menu.\n"
    "You can add custom tracks by placing them in your root folder > CZT Mod Manager/plugins/audio/menu_music.\n"
    "Supported formats: .mp3, .wav, .ogg"
)
TIP_BETA_ALERTS_RESET = "Reset dismissed beta alerts so the newest beta prompt can show again at startup."
TIP_INSTALL_CACHE_MAX_RESET = "Reset persistent cache size limit to default."
MSG_FONT_BLOCKED_TITLE = "Font Blocked"
MSG_FONT_BLOCKED_TEXT = "The font '{font_family}' is not allowed. Please select a different font."
MSG_SETTINGS_SAVED_TITLE = "Settings Saved"
MSG_SETTINGS_SAVED_CHANGED = "The following settings were changed:"
MSG_SETTINGS_SAVED_NO_CHANGES = "No settings were changed."

# controls.py log/status strings
LOG_CONFIG_NOT_SAVED_NO_ROOT = "❌ [ERROR] Config not saved due to czt_root_folder not being set!\n    > Go to USER SETTINGS tab and click 'CREATE ROOT'"
DEFAULT_SET_PROFILE_PATH = "Not set, If youre using Manual Pathing please press [Set Install] and [Set EXE]"
DEFAULT_STEAM_LIBRARY_PATH = "Not set, Press [Detect Steam]"
DEFAULT_CURRENT_PROFILE = "Not set, Please select a valid profile."
DEFAULT_EXE_NOT_FOUND = "Not found, \n    Steam Users: Press [Detect Steam], Then press [Launch Game]\n     Manual Users: Press [Set EXE] to resolve."
LOG_SAVE_CONFIG_SUMMARY = (
    "[SAVE CONFIG] Saved ✓\n"
    "[QUICK CFG SUMMARY]\n"
    "⇾ Current Profile: {current_profile}\n"
    "⇾ Path Mode: {profile_path_mode}\n"
    "⇾ SymLink Target: {set_profile_path}\n"
    "⇾ Target EXE: {exe_path}"
)
LOG_AUTO_SAVE_NO_ROOT = "❌ [ERROR] No czt_root_folder set. Config not saved!"
LOG_BROWSE_NO_ROOT = "\n[ERROR] No root folder set! Click 'CREATE ROOT' to begin using CZT.\n"
LOG_PROFILE_MODS_FOLDER_NOT_FOUND = "[ERROR] Profile mods folder not found: {profile_mods_path}"
LOG_DEST_FOLDER_NOT_FOUND = "[ERROR] Destination folder not found."
LOG_OPENED_INSTALL_AND_MODS = "Game install location and Mods folder opened."
LOG_SELECTED_PROFILE = "[PROFILE] Selected profile: {current_profile}"
LOG_PROFILE_FOLDER_WARN = "[PROFILE][WARN] Could not ensure profile folders for '{current_profile}': {error}"

# ============================================================
# Custom Profiles popup (F6)
# ============================================================
DLG_TITLE_CUSTOM_PROFILES = "Custom Profiles"
LBL_CUSTOM_PROFILES_TITLE = "Custom Game Profiles"
LBL_CUSTOM_PROFILES_SUBTITLE = (
    "Add your own games. Fields left blank inherit sensible engine defaults."
)
LBL_EDITING = "Editing:"
LBL_PROFILE_NAME = "Profile Name *"
LBL_ENGINE = "Engine *"
LBL_ENGINE_DESCRIPTION = "Description:"
LBL_STEAM_APPID = "Steam App ID"
LBL_LAUNCH_EXE = "Launch Executable"
LBL_GAME_PATH = "Game Mod Path"
LBL_NEXUS_LINK = "Nexus Game Link"
LBL_MOD_DIR_NAME = "Mod Folder Name"
LBL_ROUTING = "Folder Routing"
LBL_DEFAULT_MODS_DIR = "Stage mods directly in the profile root folder (no 'Mods' subfolder)"
OPT_NEW_PROFILE = "＋ New Profile"
BTN_DELETE_PROFILE = "Delete"
BTN_SAVE_PROFILE = "Save Profile"
BTN_CLOSE = "Close"

# Custom Profiles - input placeholders
PH_PROFILE_NAME = "ex: My Awesome Game"
PH_STEAM_APPID = "Steam App ID (ex: 1144200)"
PH_LAUNCH_EXE = "Game.exe"
PH_GAME_PATH = r"\My Game\Mods"
PH_NEXUS_LINK = "https://www.nexusmods.com/<game>/mods/"
PH_MOD_DIR_NAME = "Mods"
PH_ROUTING = "plugins=Plugins, config=Config"

# Custom Profiles - in-depth field tooltips
TIP_CP_PROFILE_SELECTOR = (
    "Choose which profile to edit.\n"
    "• '＋ New Profile' opens a blank form to create a brand-new game.\n"
    "• Selecting an existing profile loads its values so you can edit or delete it.\n"
    "Only YOUR custom profiles appear here --> built-in profiles cannot be edited\n"
    "or deleted from this window."
)
TIP_CP_PROFILE_NAME = (
    "The display name for your game, shown in the profile dropdown (required).\n"
    "This also becomes a real folder name under your CZT root, so it must be a\n"
    "valid Windows folder name.\n"
    "Allowed: letters, numbers, spaces, dashes, underscores.\n"
    "Not allowed: < > : \" / \\ | ? * , names ending in a space or period, and\n"
    "reserved names (CON, PRN, NUL, COM1…).\n"
    "Must be unique --> it cannot match a built-in or another custom profile."
)
TIP_CP_ENGINE = (
    "The mod engine CZT uses to install and link this game's mods (required).\n"
    "Pick the engine that matches your game (e.g. Unreal Engine, Unity, Techland).\n"
    "The engine supplies smart defaults (allowed file types, how mods are linked),\n"
    "so you rarely need to touch the advanced fields below.\n"
    "The grey text under this box summarizes the selected engine."
)
TIP_CP_STEAM_APPID = (
    "The game's Steam App ID (optional, numbers only).\n"
    "Find it in the Steam store URL: store.steampowered.com/app/<APPID>/.\n"
    "CZT uses this to auto-locate the game through your Steam library.\n"
    "Leave blank for non-Steam games --> you can still set paths manually on the\n"
    "Main Menu tab. Letters or symbols here will be rejected on save."
)
TIP_CP_LAUNCH_EXE = (
    "The game's executable, relative to the game folder.\n"
    "Example: Game.exe  or  Binaries\\Win64\\Game.exe.\n"
    "Separate multiple candidates with commas --> CZT uses the first one it finds.\n"
    "Used by the 'Launch Game' button; leave blank if you launch the game yourself."
)
TIP_CP_GAME_PATH = (
    "A path fragment used to help detect the game's mod folder (Steam).\n"
    "Usually the tail of the install path, e.g. \\My Game\\Mods.\n"
    "Separate multiple candidates with commas.\n"
    "This is a detection hint, not a full path --> for full manual control, set the\n"
    "game's installation path on the Main Menu tab after saving."
)
TIP_CP_NEXUS_LINK = (
    "The Nexus Mods page for this game.\n"
    "Format: https://www.nexusmods.com/<game>/mods/  where <game> is the domain\n"
    "shown in the site's URL for that game.\n"
    "Enables the in-app Nexus browser and 'open on Nexus' links for this profile."
)
TIP_CP_MOD_DIR_NAME = (
    "The name of the game-side folder mods are linked into.\n"
    "Common values: Mods, Paks, source. Defaults to 'Mods' if left blank.\n"
    "Ignored when 'Stage mods directly in the profile root folder' is checked.\n"
    "If unsure, leave the default --> the selected engine usually handles this correctly."
)
TIP_CP_ROUTING = (
    "Advanced: send specific top-level folders to a different game-side folder (optional).\n"
    "- Format: source=Target, comma-separated. Example: plugins=Plugins, config=Config.\n"
    "- Meaning: a 'plugins' folder inside a mod is linked to the game's 'Plugins'\n"
    "folder instead of the normal Mods folder.\n"
    "-Leave blank unless your game separates plugins etc from regular mods."
)
TIP_CP_DEFAULT_MODS_DIR = (
    "When checked, mods are staged directly in the profile's root folder instead\n"
    "of a 'Mods' subfolder.\n"
    "Use this for games that load mods straight from the game root.\n"
    "When checked, 'Mod Folder Name' above is ignored.\n"
    "Leave unchecked for the typical case (mods live in a dedicated Mods folder)."
)
TIP_CP_SAVE = (
    "Validate and save this profile.\n"
    "New profiles appear immediately in the profile dropdown; editing updates the\n"
    "existing entry.\n"
    "Saved to custom_profiles.json in your CZT root folder."
)
TIP_CP_DELETE = (
    "Delete the selected custom profile.\n"
    "This only removes the profile entry --> it does NOT delete any installed mods\n"
    "or files on disk.\n"
    "Only available for custom profiles you created (not built-ins)."
)
TIP_CP_CLOSE = (
    "Close this window.\n"
    "Unsaved changes in the form are discarded; already-saved profiles are kept."
)

# Custom Profiles - status / dialog messages
MSG_ENGINE_EXPERIMENTAL = (
    "⚠ Experimental engine: untested against a real game. Expect basic file "
    "deployment only (no special routing or load-order handling)."
)
MSG_NO_ROOT_FOLDER = "Set your CZT root folder first (First Time Setup)."
MSG_APPID_NUMERIC = "Steam App ID must be numeric."
DLG_TITLE_DELETE_PROFILE = "Delete Profile"
MSG_CONFIRM_DELETE_PROFILE = (
    "Delete custom profile '{name}'?\nThis does not delete any installed mods."
)

# Custom Profiles - validation / persistence messages
MSG_NAME_EMPTY = "Profile name cannot be empty."
MSG_NAME_INVALID_CHARS = 'Name cannot contain any of: < > : " / \\ | ? *'
MSG_NAME_RESERVED = "'{name}' is a reserved system name."
MSG_NAME_TRAILING = "Name cannot end with a space or period."
MSG_NAME_BUILTIN = "'{name}' is a built-in profile name; choose another."
MSG_NAME_EXISTS = "A custom profile named '{name}' already exists."
MSG_SELECT_ENGINE = "Select an engine for this profile."
MSG_UNKNOWN_ENGINE = "Unknown engine: '{engine}'."
MSG_SAVE_FAILED = "Could not write custom_profiles.json (check folder permissions)."
MSG_PROFILE_SAVED = "Profile '{name}' saved."
MSG_NOT_CUSTOM = "'{name}' is not a custom profile."
MSG_DELETE_UPDATE_FAILED = "Could not update custom_profiles.json."
MSG_PROFILE_DELETED = "Profile '{name}' deleted."

FORZATECH_DESC = (
    "Loose-file overlay engine for Forza Horizon. Mods are folders (not paks) "
    "with a 'media' tree that overrides vanilla content, an additive 'mediapc' "
    "tree, and/or root files like a version.dll proxy. CZT merges all enabled "
    "mods into one overlay in load order (top wins conflicts), then maps it into "
    "the game as a junction per top-level folder plus a symlink per root file. "
    "Where a real vanilla folder already exists it overlays per-file and backs "
    "up anything it shadows as '.czt_orig'."
)

TECHLAND_DESC = (
    "Slot-based .pak engine for Techland's C-Engine (Dying Light 1/2, The "
    "Beast). Load order comes from numbered data##.pak filenames, with low "
    "slots reserved for the game and an upper range open to mods. CZT symlinks "
    "each mod's .pak into the game's flat resource folder and renames it into a "
    "free slot. Native .dll/.asi plugins are linked beside the game exe. No "
    "Content folder or separate audio - audio ships inside the paks."
)

UNREAL_DESC = (
    "Pak engine for Unreal Engine 4/5. Handles legacy .pak plus IoStore "
    ".utoc/.ucas containers (and .sig files for signed-pak games). CZT symlinks "
    "paks into the game's mod folder (LogicMods, ~mods, or Mods) and renames "
    "them by pakchunk number to set load order. Supports .dll/.asi modloaders "
    "like UE4SS linked to the exe, plus optional Wwise (.bnk/.wem) and FMOD "
    "(.bank) audio."
)

UNITY_DESC = (
    "Modloader-driven engine for Unity (BepInEx, MelonLoader, UnityModManager) "
    "- loaders still handle load order, not the engine. Mods are typically .dll plugins or "
    ".bundle/.unity3d asset packs. CZT symlinks .dll mods into the loader's "
    "mods folder and routes known top-level folders (e.g. 'plugins') to their "
    "game-root equivalents. Optional FMOD/Wwise audio; no pak or Content-folder "
    "concept."
)



