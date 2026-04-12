# Utilities Global - English strings

# ===== basic_global_utilities.py =====
LOG_WARN_NO_ROOT_SAVE = "⚠️ [WARNING] Cannot save config because czt_root_folder does not exist."
LOG_UNRAR_NOT_FOUND = "[UNRAR] No working UnRAR tool found. Set 'unrar_path' in settings or install WinRAR (UnRAR.exe)."
DLG_TITLE_SELECT_DRIVE = "Select Drive"
LBL_SELECT_DRIVE = "Choose a drive for Mod Manager folders:"
BTN_OK = "Ok"
BTN_CANCEL = "Cancel"

# ===== CheckForCZTUpdates.py =====
WELCOME_MESSAGE = (
    "🔄️ Auto Mod Install:\n"
    "- Download mods from the nexus site. (use the 'Mod Manager Download' button)\n"
    "- This will trigger CZT and the app will automatically handle install + saving mod info.\n"
    "- If the 'Mod Manger Download' button doesnt exist, download the CZT extension from github.\n"
    "- The CZT extension enables the manual download button to act like the 'Mod Manager Download' button.\n\n"
    "🛠️ Manual Mod Install:\n"
    "- Drag and drop mod files into this log box to stage them for installation.\n"
    "- Select mods from the list and then click ➡️ (top right) to proceed.\n\n"
    "💡 [HINT]\n"
    "- Most UI elements have tooltips, hover over buttons and other UI elements to see them. \n"
    "- Press SHIFT + H to show available hotkeys.\n"
    "- Press F2 to open the Load Order menu.\n"
)
DLG_TITLE_BETA_AVAILABLE = "Beta Available"
DLG_TITLE_UPDATE_AVAILABLE = "Update Available"
LBL_BETA_AVAILABLE = "A new CZT beta is available!"
LBL_UPDATE_AVAILABLE = "A new version of CZT Mod Manager is available!"
LBL_VERSION_INFO = "Current: {local_version}\nLatest: {latest_version}"
BTN_DOWNLOAD_INSTALL = "Download and Install ({tag})"
BTN_DISMISS = "Dismiss"
DLG_TITLE_UPDATE_ERROR = "Update Error"
MSG_UPDATE_ERROR = "Failed to download or run installer:\n{error}"
MSG_NO_RELEASE_NOTES = "No release notes were found for this update channel."
MSG_RELEASE_NOTES_ERROR = "Could not fetch release notes: {error}"

# ===== load_order.py =====
DLG_TITLE_LOAD_ORDER = "Load Order"
MSG_LOAD_ORDER_NO_PROFILE = "Could not determine current profile."
MSG_LOAD_ORDER_NO_PROFILE_SET = "No current profile set."
MSG_LOAD_ORDER_PROFILE_NOT_FOUND = "Profile config not found: {profile_name}"
MSG_LOAD_ORDER_MODS_DIR_MISSING = "Mods directory does not exist for profile: {profile_name}"
DLG_TITLE_SET_LOAD_ORDER = "Set Load Order - {profile_name}"
DLG_TITLE_SAVE = "Save"
MSG_LOAD_ORDER_SAVED = "Load order saved successfully."
DLG_TITLE_ERROR_SAVING = "Error Saving"
MSG_LOAD_ORDER_SAVE_FAILED = "Failed to save load order:\n{error}"

# ===== popup_policies.py =====
POPUP_TITLE_CUSTOM_SETTINGS = "Custom Settings"
POPUP_TITLE_MANAGE_LOADOUTS = "Manage Loadouts"
POPUP_TITLE_FIRST_TIME_SETUP = "First Time Setup"
POPUP_TITLE_RESTORE_BACKUP = "Restore Backup"
POPUP_TITLE_FORCE_UPDATE_OPTIONS = "Force Update Options"
POPUP_TITLE_CLEAN_OPTIONS = "Clean Options"

# ===== UserSetup_Actions.py =====
DLG_TITLE_NO_DRIVES = "No Drives"
MSG_NO_DRIVES = "No available drives found."
DLG_TITLE_NO_ROOT_FOLDER = "No Root Folder"
MSG_NO_ROOT_FOLDER = "CZT root folder is not set or does not exist."
DLG_TITLE_ROOT_CREATED = "Root Created"
MSG_ROOT_CREATED = "CZT root folders created at: {czt_root_folder}"
DLG_TITLE_SELECT_UNRAR = "Select UnRAR Executable"
MSG_UNRAR_INSTALLER_PROMPT = (
    "UnRAR installer will launch next.\n"
    "Set destination folder to:\n"
    " > Drive_Selected_For_Root\\CZT Mod Manager\\czt_tools <"
)
LOG_UNRAR_INSTALLER_LAUNCHED = (
    "UnRAR installer launched. Please complete installation.\n"
    " Install is complete after the extraction process!"
)

# ===== backups/mod_backup.py =====
DLG_TITLE_CREATE_BACKUP = "Create Backup"
MSG_BACKUP_ROOT_NOT_SET = "Root folder is not configured."
MSG_BACKUP_CHOOSE = "Choose what to back up:"
BTN_BACKUP_MOD_FILES = "Mod Files Only"
BTN_BACKUP_MODS_LIST = "mods_list.json Only"
BTN_BACKUP_FILES_AND_LIST = "Backup Files + List"
MSG_BACKUP_SUCCESS = "Backup created successfully.\n\n"
MSG_BACKUP_WARNINGS = "Backup completed with warnings.\n\n"
MSG_BACKUP_FAILED = "Backup failed.\n\n"

# ===== backups/restore_backup.py =====
DLG_TITLE_RESTORE_BACKUP = "Restore Backup"
MSG_RESTORE_ROOT_NOT_SET = "Root folder is not configured."
MSG_RESTORE_BACKUPS_NOT_FOUND = "Backups folder not found: {backup_root}"
LBL_RESTORE_HEADER = "Select backup folders to restore or delete"
LBL_NO_BACKUPS = "No backups found"
LBL_BACKUP_META = "Contains: {kind_text}   |   Created: {stamp}"
MSG_RESTORE_SELECT_ONE = "Select one backup to install."
MSG_RESTORE_ONLY_ONE = "Install supports exactly one selected backup at a time."
MSG_RESTORE_SELECT_DELETE = "Select one or more backups to delete."
MSG_DELETE_SINGLE = "Delete backup '{name}'?"
MSG_DELETE_MULTIPLE = "Delete {count} backup folders?\n\n{preview}{extra}"
DLG_TITLE_DELETE_BACKUP = "Delete Backup"
MSG_DELETE_ERRORS = "Some backup folders could not be deleted:\n\n"
BTN_INSTALL_SELECTED = "Install Selected"
BTN_DELETE_SELECTED = "Delete Selected"
MSG_RESTORE_CONFIRM = "Restore backup '{backup_name}' for profile '{profile_name}'?"
MSG_RESTORE_CONFIRM_DETAIL = "This will replace current enabled/disabled mod files, saved loadouts, and/or profile_mods_list.json."
MSG_RESTORE_SUCCESS = "Restore completed successfully.\n\n"
MSG_RESTORE_WARNINGS = "Restore completed with warnings.\n\n"
MSG_RESTORE_FAILED = "Restore failed.\n\n"

# ===== install_mods/process_install.py =====
DLG_TITLE_NOTHING_SELECTED = "Nothing selected"
MSG_NO_MODS_SELECTED_INSTALL = "No mods selected for install."
DLG_TITLE_CONFIRM_INSTALL = "Confirm Install"
MSG_CONFIRM_INSTALL_LIST = "Install the following {count} mod(s)?\n\n{mod_list}"
MSG_CONFIRM_INSTALL_COUNT = "Install {count} selected mod(s)?"
DLG_TITLE_ERROR = "Error"
MSG_NO_ROOT_FOLDER_INSTALL = "No root folder set! Please click setup and create a root folder before attempting to install mods."
MSG_SELECTED_MODS_NOT_FOUND = "Selected mod files were not found."
DLG_TITLE_CONFIRM_SOURCE_DELETE = "Confirm Source Deletion"
MSG_CONFIRM_SOURCE_DELETE = "Delete left over mod archive(s) from source folder after install?\n\n{preview}{extra}"

# ===== install_mods/process_uninstall.py =====
MSG_NO_FILES_SELECTED_DELETE = "No files selected to delete."
DLG_TITLE_CONFIRM_DELETE = "Confirm Delete"
MSG_CONFIRM_DELETE_COUNT = "Are you sure you want to delete {count} file(s)?"

# ===== install_mods/dying_light_auto_patch.py =====
DLG_TITLE_DL_DATA_SLOT = "Replace Dying Light Data Slot"
LBL_DL_DATA_SLOT_CHOOSE = "Choose an existing Dying Light data file to replace before install, install as new using the next free slot, or cancel the install."
LBL_DL_SOURCE_MOD = "Source Mod: {source_display}"
LBL_DL_INSTALLING = "Installing: {incoming_file}"
LBL_DL_PROFILE = "Profile: {profile_name}"
BTN_INSTALL_AS_NEW = "Install as New"
BTN_INSTALL_AS_NEW_SLOT = "Install as New ({target})"
BTN_CANCEL_INSTALL = "Cancel Install"
LBL_DL_STATE_ACTIVE = "Active"
LBL_DL_STATE_DISABLED = "Disabled"

# ===== install_mods/archive_handler/archive_handler_core.py =====
DLG_TITLE_ARCHIVE_INSTALL_CHOICE = "Archive Install Choice"
MSG_ARCHIVE_MULTI_CANDIDATES = "Multiple install candidates were found in archive:\n{archive_title}\n\nAllowed extensions for this profile: {exts_label}\nSelect one candidate to install, install all, or skip this archive."
BTN_INSTALL_ALL = "Install All"
BTN_SKIP_ARCHIVE = "Skip This Archive"
DLG_TITLE_SELECTION_REQUIRED = "Selection Required"
MSG_SELECT_CANDIDATE_FIRST = "Select a candidate first, or use Install All."
DLG_TITLE_ARCHIVE_FOLDER_CHOICE = "Archive Folder Choice"
MSG_ARCHIVE_MULTI_FOLDERS = "Multiple folder install candidates were found in archive:\n{archive_title}\n\nSelect one folder candidate to install, install all, or skip this archive."

# ===== install_mods/replacement_handler/resolve_replacement.py =====
DLG_TITLE_SELECT_REPLACEMENT = "Select Replacement Target"
MSG_REPLACEMENT_DEFAULT = "Matching / similar files found. Choose which file to replace, or skip replacement."
BTN_SKIP_REPLACEMENT = "Skip Replacement (Install New File/Replace Exact Match)"

# ===== launch_game/launcher_core.py =====
MSG_NO_INSTALL_DIR = (
    "No valid install directory set!\n \n- Path Mode [STEAM]:\n   > Click 'Detect Steam'\n "
    "\n- Path Mode [Manual]:\n   > Click 'SET INSTALL' and 'SET EXE' to configure."
)
MSG_EXE_NOT_FOUND = "Could not find EXE for {game_name}!\n"
DLG_TITLE_CZT_LAUNCHER = "CZT Launcher"
MSG_LAUNCH_OPTIONS = (
    "{game_name} Launch Options: \n\n"
    " ➡️ Link | Modded = Link enabled mods.\n"
    " ➡️ Unlink | Safe = Remove existing links.\n"
    " ➡️ Cancel = Abort missile launch!"
)
BTN_LINK_MODDED = "Link | Modded"
BTN_UNLINK_SAFE = "Unlink | Safe"
MSG_ELEVATION_REQUIRED = "Elevation required. Attempting to relaunch as admin.\n\nError: {error}"
MSG_PERMISSION_DENIED = "Permission denied.\n\nError: {error}"
MSG_LAUNCH_TOGGLE_FAILED = "Could not toggle mods or launch game:\n{error}"

# ===== launch_game/launcher_utilities.py =====
MSG_ELEVATION_FAILED = "Failed to elevate to admin: {error}"
MSG_SYMLINK_PERMISSIONS = (
    "Windows requires Admin permissions to create symlinks.\n\n"
    "Choose an option:\n"
    "- Run the application as an Administrator.\n"
    "- Enable Developer Mode in Windows settings to bypass permanently.\n"
    "    ↳ No admin perms required!\n"
)
BTN_RUN_AS_ADMIN = "Run as Administrator"
BTN_OPEN_WIN_SETTINGS = "Open Windows Settings"
MSG_DEV_MODE_OPEN_FAILED = "Could not open Developer Mode settings."

# ===== loadout_system/detect_missing.py =====
DLG_TITLE_MISSING_MODS = "Missing Mods"
MSG_MISSING_NO_LOADOUTS = "No saved loadouts found for profile '{profile_name}'."
MSG_MISSING_LOADOUT_NOT_FOUND = "Loadout '{target_loadout}' was not found."
DLG_TITLE_DETECT_MISSING = "Detect Missing Mods"
LBL_DETECT_MISSING_SELECT = "Select a loadout to compare installed files against:"
MSG_MISSING_NO_FILES = "Loadout '{target_loadout}' has no files."
MSG_MISSING_NONE_DETECTED = "No missing files detected for loadout '{target_loadout}'."
MSG_MISSING_FOUND = "Found {count} missing mod file(s) for loadout '{target_loadout}'."
MSG_MISSING_DOWNLOAD_PROMPT = (
    "Found {count} missing mod file(s) for '{target_loadout}'.\n\n"
    "Download and install {download_count} missing item(s) with saved loadout metadata now?"
)
MSG_MISSING_NO_METADATA = "{count} missing item(s) have no Nexus metadata and will be listed instead."

# ===== loadout_system/ls_ui_dropdown.py =====
BTN_LOADOUTS = "Loadouts"
TIP_LOADOUTS = (
    "1.) Start by disabling all of your mods, then enable the mods you want for the new loadout.\n"
    "2.) Click the save icon to save enabled mods as a loadout file.\n"
    " - Saved loadouts can be switched from this dropdown at any time.\n"
    " - In Manage All, each loadout row has rename, copy-file, and download icons.\n"
    " - Use 'Import from file' to add loadouts from another JSON file.\n"
    " - You can also delete/edit loadout info by clicking 'Manage All'."
)

# ===== loadout_system/ls_ui_widgets.py =====
TIP_LOADOUT_CHECKBOX = "Check to include this loadout when using 'Load' or 'Merge' Loadout."
TIP_RENAME_LOADOUT = "Rename loadout"
TIP_COPY_FILE = "Copy file to clipboard"
TIP_DOWNLOAD_LOADOUT = "Download this loadout"
TIP_DETECT_MISSING = (
    "Accidently deleted a mod?\n"
    "Run this to detect and download missing mods from this loadout"
)
TIP_REFRESH_NEXUS = (
    "Validate and update nexus links + file IDs.\n"
    "When a mod is updated on nexus, the mod files download ID changes, but the old ID may still be in the loadout file.\n"
    "   - Stale URLs/IDs can lead to download failure.\n"
    "Running this will check for such stale entries and update them with the latest info from Nexus.\n"
    "Run this if,\n"
    "   - You've recently updated existing mods (not added/removed, only updated)\n"
    "   - Before sharing the loadout with others."
)

# ===== loadout_system/ls_ui_manage_dialog.py =====
LBL_MANAGE_LOADOUTS_TITLE = "Loadout Files:"
LBL_MANAGE_LOADOUTS_DESC = "(type a name below, then click 'Save Loadout' to create a new loadout)"
LBL_MANAGE_LOADOUTS_TIP_1 = "Tip 1: Select a saved loadout and click 'Save Loadout' to overwrite it."
LBL_MANAGE_LOADOUTS_TIP_2 = "Tip 2: Hover over buttons for informational tooltips."
LBL_CREATE_LOADOUT = "Create Loadout:"
BTN_SAVE_LOADOUT = "Save Loadout"
BTN_LOAD_SELECTED = "Load Selected"
BTN_MERGE_SELECTED = "Merge Selected"
BTN_IMPORT_LOADOUT = "Import Loadout"
BTN_DELETE_LOADOUT = "Delete Loadout"

TIP_OPEN_LOADOUTS_FOLDER = "Open loadouts folder"
TIP_SAVE_LOADOUT = (
    "- Enter a new name and click 'Save Loadout' to create a new loadout \n"
    "- Select an existing loadout and then click 'Save Loadout' to overwrite"
)
TIP_LOAD_LOADOUT = (
    "Load (enable) one or more loadouts.\n"
    " Only enabled mods that are currently installed.\n"
    " Use download button to actually download mod list files. \n"
    " You can also load a loadout, then press F9 to detect missing mod files."
)
TIP_MERGE_LOADOUT = "Merge selected loadouts into one new loadout."
TIP_IMPORT_LOADOUT = "Import loadouts from JSON file."
TIP_DELETE_LOADOUT = "Delete selected loadout."
DLG_TITLE_OVERWRITE_LOADOUT = "Overwrite Loadout"
MSG_OVERWRITE_LOADOUT = "Overwrite existing loadout '{name}'?"
DLG_TITLE_COPY_LOADOUT = "Copy Loadout File"
DLG_TITLE_DOWNLOAD_LOADOUT = "Download Loadout"
DLG_TITLE_REFRESH_NEXUS = "Refresh Nexus Metadata"
MSG_NEXUS_API_REQUIRED = "Nexus API key is required."
MSG_REFRESH_NEXUS_CONFIRM = "Validate Nexus links and pinned file IDs for '{loadout_name}' and overwrite this loadout file with refreshed metadata?"
MSG_REFRESH_NO_ENTRIES = "This loadout has no metadata entries. Save or import metadata first."
MSG_REFRESH_WRITE_ERROR = "Validation finished, but failed to write file:\n{error}"
MSG_REFRESH_COMPLETE = (
    "Refresh completed for '{loadout_name}'.\n\n"
    "Scanned: {scanned_count}\n"
    "Valid: {valid_count}\n"
    "Invalid: {invalid_count}\n"
    "Dead IDs Repaired: {repaired_count}\n"
    "Updated Entries (total): {changed}\n"
)
DLG_TITLE_LOADOUTS = "Loadouts"
MSG_MULTI_SELECT_ONLY_DELETE = "Only delete actions are available when multiple items are selected.\n\nRequested action: {action_label}"
MSG_OVERWRITE_PIN_MODE = "Overwrite existing loadout '{name}' with currently enabled mods?\n\nChoose how to handle file ID selection for mods in this loadout:\n\n"
BTN_UPDATE_ALL = "Update All"
BTN_UPDATE_NEW = "Update New"
BTN_DONT_UPDATE = "Dont Update"
MSG_SELECT_ONE_OVERWRITE = "Select only one loadout to overwrite, or enter a new name."
MSG_ENTER_LOADOUT_NAME = "Enter a loadout name, or select one loadout to overwrite."
DLG_TITLE_SAVE_LOADOUT = "Save Loadout"
MSG_PIN_FILE_IDS_PROMPT = (
    "Some mods have multiple main or optional files available on Nexus.\n"
    "Would you like to save the specific file version to this loadout?\n\n"
    "Doing this now will make downloading/sharing the loadout more consistent in the future.\n\n"
    "Note: CZT will display each available variant to you for easy selection. No need to go searching manually.\n"
)
MSG_OVERWRITE_SAVED = "Overwrite saved.\n\nMode Used: {mode_label}\nFile IDs updated: {processed}"
MSG_OVERWRITE_SAVED_NO_CHANGE = "Overwrite saved.\n\nMode Used: {mode_label}\n0 entries updated. New data matched existing."
MSG_SELECT_LOADOUTS_DELETE = "Select one or more saved loadouts to delete."
DLG_TITLE_DELETE_LOADOUTS = "Delete Loadouts"
MSG_CHECK_LOADOUTS_LOAD = "Check one or more saved loadouts to load."
DLG_TITLE_LOAD_LOADOUT = "Load Loadout"
MSG_LOADED_LOADOUTS = "Loaded {count} loadout{plural} successfully."
DLG_TITLE_MERGE_LOADOUTS = "Merge Loadouts"
MSG_SELECT_TWO_MERGE = "Select at least two saved loadouts to merge."
LBL_MERGED_LOADOUT_NAME = "Merged loadout name:"
MSG_ENTER_MERGED_NAME = "Enter a valid merged loadout name."
DLG_TITLE_RENAME_LOADOUT = "Rename Loadout"
LBL_NEW_FILE_NAME = "New file name:"

# ===== loadout_system/download_list.py =====
DLG_TITLE_DOWNLOAD_MOD_LIST = "Download Mod List"
MSG_RUN_INSTALL_NOW = "{summary_text}\n\nRun install now?"
MSG_INSTALL_NOT_AVAILABLE = "Install logic not available"

# ===== loadout_system/importing.py =====
DLG_TITLE_IMPORT_LOADOUTS = "Import Loadouts"
MSG_IMPORT_ROOT_NOT_SET = "Root folder is not configured."

# ===== nexus/updates.py =====
MSG_API_KEY_REQUIRED = (
    "Your Nexus API key is required to check for updates.\n"
    "API Key is used to communicate with Nexus site.\n"
    " Key is saved locally within your config file."
)
MSG_NO_TRACKED_MODS = "No tracked mods found for this profile."
MSG_ALL_UP_TO_DATE = "All mods are up to date!"
LBL_UPDATES_AVAILABLE = "Updates available:"
UPDATE_LINE_FMT = "→ {mod_name} (Current: {local_version} | New: {latest_version})"

# ===== nexus/nexus_sync.py =====
MSG_MOD_DIR_NOT_SET = (
    "Mod directory is not set or does not exist. "
    "Please set up your mod directory in the User Settings tab before saving Nexus links."
)
MSG_NEXUS_INFO_UPDATED = "Nexus info updated for {count} mod(s)."

# ===== nexus/downloads.py =====
LBL_SELECT_FILE_DOWNLOAD = "Select file to download"
LBL_SELECT_A_FILE = "Select a file to download..."
BTN_DOWNLOAD = "Download"
BTN_CANCEL = "Cancel"
ERR_DOWNLOAD_CANCELLED = "Download cancelled"
ERR_NO_FILE_SELECTED = "No file selected"
ERR_MISSING_API_KEY = "Missing Nexus API key"
ERR_NO_FILES_AVAILABLE = "No files available"
ERR_MISSING_MOD_ID_URL = "Missing Nexus Mod ID or URL"
ERR_CANNOT_RESOLVE_SLUG = "Cannot resolve Nexus game slug for this profile"
ERR_INVALID_MOD_ID_URL = "Invalid Nexus Mod ID or URL"
ERR_NO_DOWNLOADABLE_FILE = "No downloadable file id"
ERR_MISSING_ROOT_FOLDER = "Missing czt_root_folder"
ERR_NO_SELECTED_MODS = "No selected mods"
ERR_NO_TRACKED_MODS_PROFILE = "No tracked mods for current profile"
ERR_NO_VALID_NEXUS_URL = "No selected mods with valid nexus_url"
LBL_INSTALLED_MOD = "Installed Mod: {name}"
LBL_INSTALLED_FILE = "Installed File: {name}"
LBL_FILE_UNKNOWN = "Unknown"
LBL_FILE_VERSION = "Version {version}"

# ===== nexus/browse_mods/browser_actions.py =====
MSG_OPEN_MOD_PAGE_FIRST = (
    "Open a specific Nexus mod page first, then click Add Current Mod.\n\n"
    "Expected URL format:\n"
    "https://www.nexusmods.com/<game>/mods/<id>"
)
STATUS_DOWNLOADING_MOD = "Downloading mod {mod_id}..."
STATUS_DOWNLOAD_FAILED = "Download failed"
STATUS_DOWNLOAD_INSTALLING = "Download complete. Installing..."
STATUS_DOWNLOADED = "Downloaded: {name}"
MSG_DOWNLOAD_COMPLETE_SAVED = "Download complete.\n\nSaved to: {path}"
STATUS_INSTALL_FAILED = "Install failed"
STATUS_INSTALLED = "Installed: {name}"

# ===== nexus/browse_mods/browser_widgets.py =====
LBL_SELECT_A_MOD = "Select a mod"
LBL_NOT_INSTALLED = "Not Installed"
BTN_ADD_TO_FAVORITES = "Add to Favorites"
LBL_ZERO_DOWNLOADS = "0 downloads"
LBL_ZERO_ENDORSEMENTS = "0 endorsements"
LBL_UPDATED_NONE = "Updated: --"
LBL_NO_MOD_SELECTED = "No mod selected"
LBL_PAK_FILES = "Pak Files"
LBL_NO_FILES_AVAILABLE = "No files available"
LBL_NO_CHANGELOG = "No changelog available"
LBL_UNKNOWN_MOD = "Unknown Mod"
LBL_BY_AUTHOR = "By {author}"
LBL_DOWNLOADS_COUNT = "{count} downloads"
LBL_ENDORSEMENTS_COUNT = "{count} endorsements"
LBL_UPDATED_DATE = "Updated {date}"
LBL_NO_DESCRIPTION = "No description available."

# ===== nexus/browse_mods/browser_window.py =====
DLG_TITLE_BROWSE_NEXUS = "Browse Nexus Mods - {profile}"
TIP_BACK = "Back"
TIP_FORWARD = "Forward"
TIP_REFRESH = "Refresh"
TIP_GO = "Go"
TIP_ENDORSEMENT_STATUS = "Endorsement status"
MSG_WEBENGINE_UNAVAILABLE = (
    "Qt WebEngine is not available in this install.\n"
    "Install PySide6-WebEngine to enable in-app Nexus browsing."
)
STATUS_BROWSER_UNAVAILABLE = "Embedded browser unavailable"
STATUS_LOADING_PAGE = "Loading page..."
STATUS_NO_NEXUS_LINK = "No Nexus game link configured for this profile"
STATUS_LOADING_MODS = "Loading Nexus mods..."
STATUS_PAGE_LOADED = "Page loaded"
STATUS_PAGE_FAILED = "Failed to load page"

# ===== nexus/browse_mods/endorsements.py =====
TIP_ENDORSE_ONLY_MOD_PAGES = "Endorsement status is only available on mod pages"
TIP_ENDORSED = "Endorsed"
TIP_NOT_ENDORSED = "Not endorsed"
ERR_INVALID_ENDORSEMENT = "Invalid endorsement action"
ERR_UNKNOWN_ENDORSEMENT = "Unknown endorsement error"
STATUS_OPEN_MOD_TO_ENDORSE = "Open a specific mod page to endorse"
STATUS_ENDORSE_UNAVAILABLE = "Endorsement status unavailable"
STATUS_UPDATING_ENDORSEMENT = "Updating endorsement..."
STATUS_ENDORSED = "Endorsed"
STATUS_ENDORSEMENT_REMOVED = "Endorsement removed"
STATUS_ENDORSEMENT_FAILED = "Endorsement failed"
MSG_ENDORSEMENT_FAILED = "Could not update endorsement.\n\n{error}"

# ===== nexus/browse_mods/install_state.py =====
LBL_MOD_INSTALLED = "Mod installed"
LBL_MOD_NOT_INSTALLED = "Mod not installed"

# ===== nexus/protocol_handler/nxm/nxm_actions.py =====
MSG_NXM_GAME_MISMATCH = (
    "This mod is for \"{game}\". \n"
    "Current profile is \"{profile}\".\n\n"
    "Switch to the \"{game}\" profile then try again."
)

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py =====
MSG_CZTMM_GAME_MISMATCH = (
    "The mod you attempted to install is for \"{game}\". \n"
    "Your current profile is \"{profile}\".\n\n"
    "Switch to the \"{game}\" profile then try again."
)

# ===== refresh_manager/refresh_manager.py =====
PLACEHOLDER_SEARCH_MODS = "Search mods : {profile}"


# =====================================================================
#  LOG MESSAGES  (czt_log / czt_log_synced)
# =====================================================================

# ===== install_mods/process_install.py (logs) =====
LOG_INSTALL_CANCELLED = "[INSTALL CANCELLED] Install cancelled by user during replacement confirmation."
LOG_INSTALL_FAILED = "\n[ERROR] Install failed: {error}\n"
LOG_INSTALL_QUEUED = "[INSTALL] Another install is running. Queuing this install request."
LOG_INSTALL_SELECTED_FILES = "\n[INSTALL] Selected Files:\n{file_list}"
LOG_PROCESSING_MOD = "[PROCESSING] Mod: {install_label}"
LOG_INSTALL_MOD_FAILED = "[ERROR] Failed while installing '{install_label}': {error}"
LOG_DELETE_SOURCE_FAILED = "[DELETE AFTER INSTALLED] Failed to remove source item '{src_path}': {error}"
LOG_INSTALL_COMPLETED = " \n[INSTALL PROCESS COMPLETED] All selected mods have been processed.\n"
LOG_SUMMARY = "[SUMMARY]"
LOG_SUMMARY_SUCCESS = "\n    > SUCCESS: "
LOG_SUMMARY_FAILED = "\n    > FAILED: "
LOG_SUMMARY_SKIPPED = "\n    > SKIPPED: (Exporter-matched archive candidate not found) "
LOG_SUMMARY_SOURCE_DELETED = "\n    > SOURCE FILE DELETED: "
LOG_SUMMARY_SOURCE_DELETE_SKIPPED = "\n    > SOURCE FILE DELETE SKIPPED: User declined confirmation."

# ===== install_mods/process_uninstall.py (logs) =====
LOG_DELETED_MODS = "[DELETE] Deleted {count} mod(s):\n -> {item_list}"

# ===== install_mods/dying_light_auto_patch.py (logs) =====
LOG_DL_SLOT_SKIPPED = "[DL DATA SLOT] Skipped '{base_name}' because no replacement target was selected and its current slot is not available."
LOG_DL_SLOT_KEEP = "[DL DATA SLOT] Keeping incoming file name '{base_name}' for install."
LOG_DL_SLOT_INSTALL_NEW = "[DL DATA SLOT] Install as new selected next available slot '{selected_file_name}' for incoming '{base_name}'."
LOG_DL_SLOT_REPLACE = "[DL DATA SLOT] Selected replacement target '{selected_file_name}' for incoming '{base_name}'."

# ===== install_mods/archive_handler/archive_handler_core.py (logs) =====
LOG_OPTION_SKIP_NO_EXPORTERS = "[INSTALL][OPTION][SKIPPED] No exporter basenames available for {choice_kind} candidates in {archive_name}."
LOG_OPTION_AUTO_SELECT = "[INSTALL][OPTION] Auto-selected {count} exporter-matched {choice_kind} candidate(s) in {archive_name}."
LOG_OPTION_SKIP_NO_MATCH = "[INSTALL][OPTION][SKIPPED] No exporter-matched {choice_kind} candidates found in {archive_name}."
LOG_CACHE_SKIP = "[INSTALL][OPTION][CACHE] Used cached file option: skip archive {archive_name}"
LOG_CACHE_INSTALL_ALL = "[INSTALL][OPTION][CACHE] Used cached file option: install all from archive {archive_name}"
LOG_CACHE_SELECTED = "[INSTALL][OPTION][CACHE] Used cached file selection: {chosen_rel}"
LOG_MULTI_FOLDER_CANDIDATES = "[INSTALL][OPTION] Multiple folder candidates found in archive: {archive_name}"
LOG_SKIPPED_FOLDER_CHOICE = "[INSTALL][SKIPPED] User skipped folder archive choice: {archive_name}"
LOG_ADDITIONAL_FOLDER_CANDIDATES = "[INSTALL][OPTION] Additional folder candidates found in selected option: {archive_name}"
LOG_SKIPPED_NESTED_FOLDER = "[INSTALL][SKIPPED] User skipped nested folder choice: {archive_name}"
LOG_MULTI_FILE_CANDIDATES = "[INSTALL][OPTION] Multiple install candidates found in archive: {archive_name}"
LOG_SKIPPED_FILE_CHOICE = "[INSTALL][SKIPPED] User skipped archive install choice: {archive_name}"
LOG_ADDITIONAL_FILE_CANDIDATES = "[INSTALL][OPTION] Additional file candidates found in selected option: {archive_name}"
LOG_SKIPPED_NESTED_FILE = "[INSTALL][SKIPPED] User skipped nested file choice: {archive_name}"
LOG_UNSUPPORTED_ARCHIVE = "[ERROR] Unsupported archive type or missing library: {archive_type}"
LOG_RAR_NOT_AVAILABLE = "[ERROR] rarfile library not available for .rar extraction: {archive_name}."
LOG_7Z_NOT_AVAILABLE = "[ERROR] py7zr library not available for .7z extraction: {archive_name}"
LOG_PROCESS_ITEM_FAILED = "[ERROR] Failed to process {item}: {error}"
LOG_EXTRACT_FAILED = "[ERROR] Failed to extract {archive_type} {archive_name}: {error}"

# ===== install_mods/replacement_handler/resolve_replacement.py (logs) =====
LOG_REPLACEMENT_CONFIRM = "[INSTALL SAFETY] Replacement confirmation required for '{mod_name}'"
LOG_REPLACEMENT_REMOVE_FAILED = "[WARN] Could not remove selected replacement file '{old_path}': {error}"
LOG_REPLACEMENT_DIALOG_FAILED = "[WARN] Replacement confirmation dialog failed: {error_type}: {error}"

# ===== install_mods/install_registry.py (logs) =====
LOG_REPLACE_EXISTING = "[UPDATE INSTALL] Replaced existing mod file: {old_file} -> {new_file}"
LOG_REPLACE_REMOVE_FAILED = "[WARN] Could not remove replaced mod file '{old_file}': {error}"
LOG_REPLACE_DISABLED_REMOVE_FAILED = "[WARN] Could not remove replaced disabled mod file '{old_file}': {error}"
LOG_JSON_UPDATING = "[JSON WRITE] Updating existing entry in mod list:\n   \u21b3'{mod_name}'"
LOG_REPLACE_OPTIONS_FOUND = "[REPLACE] '{mod_name}': {count} existing file option(s) found."
LOG_INSTALLED = "[INSTALLED] '{mod_name}'"
LOG_INSTALLED_KEPT_EXISTING = "[INSTALLED] '{mod_name}': Kept existing file(s) and installed new file."
LOG_JSON_WRITE_COMPLETE = (
    "[JSON WRITE COMPLETE] profile_mods_list.json has been updated successfully.\n"
    "[SUMMARY] Updated: {updated_count}, New: {new_count}, Total: {total_count}."
)
LOG_JSON_WRITE_ERROR = "[ERROR] Could not update mods list: {error}"

# ===== install_mods/install_utilities.py (logs) =====
LOG_STAGING_ERROR = "[STAGING ERROR] Could not stage {file_name}: {error}"
LOG_STAGED = "[STAGED] Staged {count} mod(s) in:\n -> {staged_list}\n[SOURCE] -> {mods_source}"
LOG_REPLACEMENT_TIMEOUT = "[WARN] Timed out waiting for replacement confirmation dialog."

# ===== install_mods/archive_handler/progress.py (logs) =====
LOG_PROGRESS = "[{stage_key}] {label} [{percent}%]"
LOG_EXTRACTING = "[EXTRACTING] {label} [0%]"
LOG_INSTALLING_PROGRESS = "[INSTALLING] {label} [0%]"

# ===== nexus/updates.py (logs) =====
LOG_UPDATE_SCAN_START = "[UPDATE SCAN] Current Profile: {profile_name} | Checking for available updates...\n"
LOG_UPDATE_SCAN_MOD = "\u2192 Mod: {file_name} | Local: {local_version} | Latest: {latest_version} | "
LOG_UPDATE_SCAN_COMPLETED = " \n[UPDATE SCAN COMPLETED] {scan_label} | updates found: {updated_count}"
LOG_UPDATE_SCAN_COMPLETED_ALT = "\n[UPDATE SCAN COMPLETED] {scan_label} | updates found: {updated_count}"

# ===== nexus/nexus_sync.py (logs) =====
LOG_NEXUS_MODS_DIR_MISSING = "[NEXUS] mods_dir missing, using fallback: {fallback_dir}"
LOG_NEXUS_MODS_DIR_ERROR = "[NEXUS][ERROR] mods_dir invalid. Provided: {mods_dir} | Fallback: {fallback_dir} | Profile: {profile_name}"
LOG_NEXUS_SAVING = "[NEXUS][SAVE] Saving collected mod data to {tracked_file}"
LOG_NEXUS_INFO_UPDATED_LOG = "[NEXUS] info updated for {updated_count} mod(s)."

# ===== nexus/downloads.py (logs) =====
LOG_NEXUS_REDIRECT_STANDARD = "[NEXUS - STANDARD] Redirecting to mod files page for download: {target_url}"
LOG_NEXUS_OPEN_FAILED = "[NEXUS] Failed to open mod files page: {error}"
LOG_DOWNLOADING = "[DOWNLOADING] {out_path}"
LOG_DOWNLOAD_FAILED = "[DOWNLOAD] Failed for '{display_label}': {error}"
LOG_DOWNLOAD_COMPLETED = "[DOWNLOAD] Completed: {downloaded} file(s) downloaded."

# ===== nexus/browse_mods/browser_window.py (logs) =====
LOG_BROWSER_CLOSED = "[NEXUS_BROWSER] Closed"
LOG_BROWSER_NO_GAME = "[NEXUS_BROWSER] No game_var available"

# ===== nexus/protocol_handler/nxm/nxm_actions.py (logs) =====
LOG_NXM_RECEIVED = "[NXM] Received URL: {nxm_url}"
LOG_NXM_PARSE_FAILED = "[NXM][ERROR] Could not parse NXM URL: {nxm_url}"
LOG_NXM_GAME_MISMATCH_LOG = "[NXM] Game mismatch: NXM={game_slug}, active profile={profile_game_slug}"
LOG_NXM_DOWNLOAD_EVENT = (
    "[NXM] Nexus download event received: Game: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[NXM] CZT will auto install your file once the download is complete.\n"
    "[NXM] Please wait..."
)
LOG_NXM_DOWNLOAD_FAILED = "[NXM] Download failed or was cancelled"
LOG_NXM_DOWNLOAD_COMPLETE = "[NXM] Download complete: {result}"

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py (logs) =====
LOG_CZTMM_RECEIVED = "[CZTMM] Received URL: {cztmm_url}"
LOG_CZTMM_PARSE_FAILED = "[CZTMM][ERROR] Could not parse URL: {cztmm_url}"
LOG_CZTMM_GAME_MISMATCH_LOG = "[CZTMM] Game mismatch: CZTMM={game_slug}, current profile={profile_game_slug}"
LOG_CZTMM_DOWNLOAD_EVENT = (
    "[CZTMM] Nexus download event received: Game: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[CZTMM] CZT will auto install your file once the download is complete.\n"
    "[CZTMM] Please wait..."
)
LOG_CZTMM_DOWNLOAD_EVENT_STANDARD = (
    "[CZTMM] Nexus download event received: Game: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[CZTMM] [STANDARD NEXUS ACCOUNT DETECTED] \n"
    "[CZTMM] Don't forget to press 'Slow Download' in your browser!\n"
    "[CZTMM] CZT will auto install your file once the download is complete.\n"
    "[CZTMM] Please wait...\n"
)

# ===== nexus/account_type_status.py (logs) =====
LOG_NEXUS_ACCOUNT_TIER_FAILED = "[CZTMM] Could not resolve Nexus account tier, defaulting to standard: {error}"

# ===== nexus/manual_download_install.py (logs) =====
LOG_NO_DOWNLOAD_DETECTED = "[CZTMM] No recently completed download detected; auto-install skipped."
LOG_INSTALLING_DOWNLOAD = "[CZTMM] Installing downloaded file: {chosen_path}"

# ===== nexus/browse_mods/browser_ext.py (logs) =====
LOG_BROWSER_JS_WITH_SOURCE = "[NEXUS_BROWSER][JS] {text} ({source}:{line_number})"
LOG_BROWSER_JS = "[NEXUS_BROWSER][JS] {text}"

# ===== nexus/browse_mods/marquee_label.py =====
BANNER_TEXT_FREE = (
	"Standard Nexus account detected — "
	"This feature is designed for premium accounts — "
	"Direct downloads from remote apps are restricted by Nexus for free accounts — "
	"Nexus enforces the same limitations on Vortex."
)
BANNER_TEXT_PREMIUM = (
	"You do not need to sign-in to browse or download mods, that's what the API key is for in the setup menu "
	"— To use this browser, navigate to a mod of your choice, then click the 'Download + Install Current Mod' button "
	"— Mod info is saved to your local mod list file at the time of download"
)
LOG_ACCOUNT_TIER_FALLBACK = "[NEXUS_BROWSER] Could not resolve account tier, defaulting to free: {error}"

# ===== nexus/protocol_handler/nxm/nxm_runtime.py (logs) =====
LOG_NXM_STARTUP_REG_FAILED = "[NXM] Failed to apply startup registration setting: {error}"
LOG_NXM_SENT_URL = "[NXM] Sent URL to running instance: {protocol_url_arg}"
LOG_NXM_SEND_FAILED = "[NXM] Failed to send URL to running instance: {error}"
LOG_NXM_IPC_FAILED = "[NXM][ERROR] Failed to start NXM IPC server"

# ===== nexus/protocol_handler/nxm/nxm_register.py (logs) =====
LOG_NXM_REGISTERED = "[NXM] Registered nxm:// protocol handler: {command}"
LOG_NXM_REGISTER_FAILED = "[NXM][ERROR] Failed to register nxm:// handler: {error}"
LOG_NXM_UNREGISTERED = "[NXM] Unregistered nxm:// protocol handler"
LOG_NXM_UNREGISTER_FAILED = "[NXM][ERROR] Failed to unregister nxm:// handler: {error}"

# ===== nexus/protocol_handler/cztmm/cztmm_register.py (logs) =====
LOG_CZTMM_REGISTERED = "[CZTMM] Registered cztmm:// protocol handler: {command}"
LOG_CZTMM_REGISTER_FAILED = "[CZTMM][ERROR] Failed to register cztmm:// handler: {error}"
LOG_CZTMM_UNREGISTERED = "[CZTMM] Unregistered cztmm:// protocol handler"
LOG_CZTMM_UNREGISTER_FAILED = "[CZTMM][ERROR] Failed to unregister cztmm:// handler: {error}"

# ===== loadout_system/ls_ui_manage_dialog.py (logs) =====
LOG_LOADOUT_ROOT_NOT_SET = "[LOADOUT] Root folder not set. Cannot manage loadouts."

# ===== loadout_system/download_list.py (logs) =====
LOG_LOADOUT_SAVE_FAILED_DL = "[LOADOUT] Failed to save imported loadouts from Download Mod List."
LOG_LOADOUT_IMPORTED_DL = "[LOADOUT] Imported {added_count} loadout(s) into saved loadouts for profile '{profile_name}' from Download Mod List."
LOG_DOWNLOAD_CANCELED = "[LOADOUT DOWNLOAD] Download Mod List canceled at redownload confirmation prompt."
LOG_DOWNLOAD_SUMMARY = "[SUMMARY] Downloaded: {downloaded} | Skipped existing: {skipped} | Failed: {failed}"
LOG_DOWNLOAD_INSTALL_QUEUED = "[INSTALL] Another in-app download install is running. Queuing this install request."
LOG_DOWNLOAD_INSTALL_FAILED = "[INSTALL] Download-install worker failed: {error}\n{traceback}"
LOG_LOADOUT_AUTO_SELECT_FAILED = "[LOADOUT] Failed to auto-select imported loadout '{loadout_name}': {error}"

# ===== loadout_system/importing.py (logs) =====
LOG_LOADOUT_IMPORTED = (
    "[LOADOUT] Imported {added_count} loadout(s) from '{imported_path}'. \n"
    "Entries added to primary mod list: {profile_metadata_added}. \n"
    "Entries updated in primary mod list: {profile_metadata_updated}."
)

# ===== loadout_system/build_loadout.py (logs) =====
LOG_LOADOUT_MERGE_FAILED = "[LOADOUT] Failed to save merged loadouts for profile '{profile_name}': {error}"

# ===== loadout_system/apply_loadout.py (logs) =====
LOG_LOADOUT_ROOT_NOT_SET_APPLY = "[LOADOUT] Root folder not set. Cannot apply loadout."
LOG_LOADOUT_NO_MODS = "[LOADOUT] No mods found for loadout '{loadout_name}'."
LOG_LOADOUT_ROOT_NOT_SET_APPLY_MULTI = "[LOADOUT] Root folder not set. Cannot apply loadouts."
LOG_LOADOUT_NO_MODS_MULTI = "[LOADOUT] No mods found for selected loadouts."

# ===== loadout_system/storage.py (logs) =====
LOG_LOADOUT_REMOVE_FAILED = "[LOADOUT] Failed to remove existing loadout files: {error}"
LOG_LOADOUT_SAVE_FAILED = "[LOADOUT] Failed to save loadouts: {error}"

# ===== loadout_system/select_file_variant.py (logs) =====
LOG_FILE_PIN_SKIPPED = "[LOADOUT] File pinning skipped for '{display_name}' ({cache_key}): {error}"

# ===== loadout_system/ls_utilities.py (logs) =====
LOG_FILE_CANDIDATES_FAILED = "[LOADOUT] Failed to load file candidates for {loadout_name}:{mod_id}: {error}"
LOG_FILE_PIN_SELECTION_SKIPPED = "[LOADOUT] File pin selection skipped for {loadout_name}:{mod_id}: {error}"

# ===== Get_SteamLibraries.py (logs) =====
LOG_STEAM_SCAN_DRIVE = "[STEAMLIB][SCAN] Scanning drive {drive_root} for libraryfolders.vdf (UPDATED)"
LOG_STEAM_SCAN_LEGACY = "[STEAMLIB][SCAN] Scanning drive {drive_root} for libraryfolder.vdf (LEGACY)"
LOG_STEAM_SEARCHING = "[STEAMLIB][SCAN] Searching... {pattern}"
LOG_STEAM_LOCATED = "[STEAMLIB] [LOCATED] libraryfolders.vdf @ {vdf} (UPDATED)"
LOG_STEAM_LOCATED_LEGACY = "\n[STEAMLIB] [LOCATED] libraryfolder.vdf @ {vdf} (LEGACY)"
LOG_VDF_PARSING = "[VDF] Parsing VDF file..."
LOG_STEAM_ADDED = "[STEAMLIB][ADDED] \u21be {lib_common}"
LOG_STEAM_PARSE_WARN = "[WARN] Could not parse Steam libraries: {error}"
LOG_STEAM_SKIP_SCAN = "[STEAMLIB] Skipping Steam library scan: pathing mode for '{current_profile}' is '{pathing_mode}'."
LOG_STEAM_RUN_UTIL = "[RUN UTIL] \u25b6 SteamLibrarySearchUtility \u25c0"
LOG_STEAM_SCANNING = "[STEAMLIB] Scanning for Steam libraries..."
LOG_STEAM_SCAN_SUCCESS = "[STEAMLIB] [SCAN SUCCESSFUL]\n    \u21be All Steam library paths updated."
LOG_STEAM_WARN_NO_ROOT = "\u26a0\ufe0f [WARNING] Cannot save config because czt_root_folder does not exist."
LOG_EXE_DETECTED = "[EXE DETECTED] Found @ {path}"
LOG_EXE_NOT_FOUND = "[EXE DETECT] No valid exe found."
