import os, sys
import importlib

ADDED_PROFILE_NAMES = []
LAST_PLUGIN_API = None

# Official CZT Plugin: Custom_Profiles (adds additional game profile to in-memory config)
# Usage: Place this file in plugins/scripts, then run it from the CZT Mod Manager plugin menu.
# You can use this to... 
#   ↳ add NEW profiles for games that are not included in the main CZT Mod Manager or to 
#   ↳ add multiple profiles for the same game. (allowing you to quickly switch between mod setups for the same game)

def run(plugin_api):
    try:
        global ADDED_PROFILE_NAMES, LAST_PLUGIN_API
        LAST_PLUGIN_API = plugin_api
        # Find the root (parent of plugins/scripts) // When i made this i had the .py file in CZT Mod Manager/plugins/scripts and just edited it directly
        GAME_PROFILES = plugin_api.GAME_PROFILES
        if GAME_PROFILES is None:
            plugin_api.czt_log("[PLUGIN] Could not access GAME_PROFILES in context.")
            return
        profiles_to_add = {
            "RoN_Custom_1": { # <--------------------------------------------------- Name of the profile as it will appear in the CZT Mod Manager game profile dropdown.
                "steam_appid": 1144200, # <------------------------------------------ Steam App ID (get these from https://steamdb.info/)
                "launch_exe": [r"ReadyOrNot.exe"], # < ------------------------------ Relative path to the game executable.
                "path": [r"\Ready or Not\ReadyOrNot\Content\Paks\Mods"], # <--------- Where mods are symlinked to @ game launch.
                "load_order_type": "pakchunkNum", # <-------------------------------- Set load order type - dataNum (dataN.pak), pakchunkNum (pakchunkN.pak) and NumName (Number_ModName). This is how CZT chooses a method for naming symlinked mod files to ensure proper load order.
                "foldered_mods": False, # <------------------------------------------ If True, mods are expected to be in their own folders within the Mods directory (games like 7dtd where mods remain in a folder)
                "allow_file_type_dll": False, # <------------------------------------ If True, .dll files can be installed
                "allow_file_type_asi": False, # <------------------------------------ If True, .asi files can be installed
                "allow_file_type_pak": True, # <------------------------------------- If True, .pak files can be installed
                "symlink_asi_and_dll_to_exe": False, # <----------------------------- If True, .dll and .asi files will be linked to the exe path when game is launched.
                "official_game_data_paks": [], # <----------------------------------- List of official .pak files. This prevents them from being modified or deleted.
                "auto_rename_pak": False, # <---------------------------------------- If True, rename .pak files during copy/transfer / if False, overwrite files of the same name. // 9/28/25: Deprecated, now handled by DataN patcher.
                "default_mods_dir": True, # <---------------------------------------- If True, installs directly to path. If False, uses set_mod_dir_name below.
                "set_mod_dir_name": "Mods", # <--------------------------------------- Set mod folder name. The name "Mods" is used for most games, but some games dont care about the name and this can be set to anything.
                "per_file_symlink": True, # <---------------------------------------- If True, enables per-file symlink mode (each mod file is symlinked separately)
                "per_folder_symlink": False, # <------------------------------------- If True, enables per-folder symlink mode (each mod folder is symlinked as a whole) // Had to make this for games like 7dtd that have a default dependency, in 7dtd's case its "0_TFP_Harmony"
                "nexus_game_link": "https://www.nexusmods.com/readyornot/mods/", # <- Link to the game's overall Nexus Mods page.
                "mod_folder": "RoN_Custom_1_Mods", # < ----------------------------- Name of the mod storage folder: CZT Mod Manager/profile_mods/mod_folder.
                "description": "Custom Ready or Not profile added by plugin.",
                "created_by_plugin": True
            },
            "RoN_Custom_2": {
                "steam_appid": 1144200,
                "launch_exe": [r"ReadyOrNot.exe"],
                "path": [r"\Ready or Not\ReadyOrNot\Content\Paks\Mods"],
                "load_order_type": "pakchunkNum",
                "foldered_mods": False,
                "allow_file_type_dll": False,
                "allow_file_type_asi": False,
                "allow_file_type_pak": True,
                "symlink_asi_and_dll_to_exe": False,
                "official_game_data_paks": [],
                "auto_rename_pak": False,
                "default_mods_dir": True,
                "set_mod_dir_name": "Mods",
                "per_file_symlink": True,
                "per_folder_symlink": False,
                "nexus_game_link": "https://www.nexusmods.com/readyornot/mods/",
                "mod_folder": "RoN_Custom_2_Mods",
                "description": "Custom Ready or Not profile added by plugin.",
                "created_by_plugin": True
            }
        }
        for profile_name, profile_data in profiles_to_add.items():
            if profile_name in GAME_PROFILES:
                plugin_api.czt_log(f"[PLUGIN] Profile '{profile_name}' already exists in memory.")
            else:
                GAME_PROFILES[profile_name] = profile_data
                ADDED_PROFILE_NAMES.append(profile_name)
                plugin_api.czt_log(f"[PLUGIN] Profile '{profile_name}' has been added as a usable profile.")
        plugin_api.czt_log(" > Custom profiles will remain in-memory until plugin is removed.")
    except Exception as e:
        plugin_api.czt_log(f"[PLUGIN] Error adding profile to GAME_PROFILES: {e}")

def on_unload():
    global ADDED_PROFILE_NAMES, LAST_PLUGIN_API
    plugin_api = LAST_PLUGIN_API
    if plugin_api is None:
        return
    try:
        def refresh_any_open_ui():
            try:
                from PyQt5.QtWidgets import QApplication
                for w in QApplication.topLevelWidgets():
                    tab = getattr(w, "user_setup_tab", None)
                    if tab and hasattr(tab, "refresh_profile_dropdown"):
                        if hasattr(tab, "GAME_PROFILES"):
                            tab.profiles = list(tab.GAME_PROFILES.keys())
                        tab.refresh_profile_dropdown()
                        return True
            except Exception:
                pass
            return False

        def remove_from(target_dict):
            removed_local = []
            if not target_dict:
                return removed_local
            for name in list(ADDED_PROFILE_NAMES):
                if name in target_dict:
                    del target_dict[name]
                    removed_local.append(name)
            return removed_local

        removed = []
        removed += remove_from(getattr(plugin_api, "GAME_PROFILES", None))
        if getattr(plugin_api, "user_setup_tab", None) is not None:
            removed += remove_from(getattr(plugin_api.user_setup_tab, "GAME_PROFILES", None))
        if getattr(plugin_api, "mod_manager_tab", None) is not None:
            removed += remove_from(getattr(plugin_api.mod_manager_tab, "GAME_PROFILES", None))
        try:
            from var_global.Global_Configs import GAME_PROFILES as GLOBAL_GAME_PROFILES
            removed += remove_from(GLOBAL_GAME_PROFILES)
        except Exception:
            pass

        ADDED_PROFILE_NAMES = []
        if removed:
            plugin_api.czt_log(f"[PLUGIN] Removed profiles on unload: {', '.join(sorted(set(removed)))}")
        if getattr(plugin_api, "user_setup_tab", None):
            if hasattr(plugin_api.user_setup_tab, "profiles") and getattr(plugin_api, "GAME_PROFILES", None):
                plugin_api.user_setup_tab.profiles = list(plugin_api.GAME_PROFILES.keys())
            if hasattr(plugin_api.user_setup_tab, "refresh_profile_dropdown"):
                plugin_api.user_setup_tab.refresh_profile_dropdown()
        else:
            refresh_any_open_ui()
    except Exception as e:
        try:
            plugin_api.czt_log(f"[PLUGIN] Error during unload cleanup: {e}")
        except Exception:
            pass

# ================================================================================================================================================

# [Game Profile Variable Reference] [EXAMPLES BELOW THESE COMMENTS]

# [VAR_NAME] ----------------------------- [DESCRIPTION]
# steam_appid: ---------------------------> Steam App ID for the selected game (used for Steam library path resolution)
# launch_exe: ----------------------------> Relative path to the game’s main executable
# path: ----------------------------------> Main content or mods folder path for this game (Essentially the path used for manual mod installation)
# foldered_mods: -------------------------> If True, mods are expected to be in their own folders within the Mods directory (games like 7dtd where mods remain in a folder)
# allow_file_type_dll: -------------------> If True, .dll files can be installed
# allow_file_type_asi: -------------------> If True, .asi files can be installed
# allow_file_type_pak: -------------------> If True, .pak files can be installed
# load_order_type: -----------------------> Set load order type - dataNum (dataN.pak), pakchunkNum (pakchunkN.pak) and NumName (Number_ModName). This is how CZT chooses a method for naming symlinked mod files to ensure proper load order.
# symlink_asi_and_dll_to_exe -------------> If True, .dll and .asi files will be linked to the exe path when game is launched.
# official_game_data_paks: ---------------> List of official .pak files. This prevents them from being modified or deleted.
# auto_rename_pak: -----------------------> If True, rename .pak files during copy/transfer / if False, overwrite files of the same name. // 9/28/25: Deprecated, now handled by DataN patcher.
# default_mods_dir: ----------------------> If True, installs directly to path. If False, uses set_mod_dir_name below.
# set_mod_dir_name: -----------------------> Set mod folder name. The name "Mods" is used for most games, but some games dont care about the name and this can be set to anything.
# per_file_symlink: ----------------------> If True, enables per-file symlink mode (each mod file is symlinked separately)
# per_folder_symlink: --------------------> If True, enables per-folder symlink mode (each mod folder is symlinked as a whole) // Had to make this for games like 7dtd that have a default dependendy, in 7dtd's case its "0_TFP_Harmony"
# nexus_game_link: -----------------------> Link to the game's overall Nexus Mods page.
# dependency_mods: -----------------------> List of dependency mod filenames or patterns (these will then be detected and handled by the below var)
# copy_dependency_to_profile: ------------> This is where the dependency will be copied to in terms of structure within the game profile. (refer to schedule I profile for example)
# link_dependency_to_path: List of dicts -> This is for manually controlling where dependency links are placed in the game directory during launch. 
# ↳---------------------------------------> (we use the steam library paths from config and append the path given here in the profile)

# [Variables for plugin profiles]
# [VAR_NAME] ----------------------------- [DESCRIPTION]
# mod_folder: ----------------------------> Name of the mod storage folder: CZT Mod Manager/profile_mods/mod_folder.
# description: ---------------------------> Simple desc "Custom Ready or Not profile added by plugin.",
# created_by_plugin: ---------------------> True/False flag to indicate profile was created by plugin.

# ================================================================================================================================================

# [Example]
# "GAME_NAME": {    <-------------------------------- THIS WILL BE THE KEY IN THE GAME PROFILE DROPDOWN
#     "steam_appid": "3164500",
#     "launch_exe": "...",
#     "path": "...",
#     "foldered_mods": False,
#     "allow_file_type_dll": False,
#     "allow_file_type_asi": False,
#     "allow_file_type_pak": True,
#     "load_order_type": "pakchunkNum", # other types listed above
#     "symlink_asi_and_dll_to_exe": False,
#     "official_game_data_paks": [],
#     "auto_rename_pak": True,
#     "default_mods_dir": False,
#     "set_mod_dir_name": "mod.czt",
#     "per_file_symlink": False,
#     "per_folder_symlink": True,

# // Just an example, Most of the main profiles dont use the dependency mod system. Only schedule I does. (good for games that require dll loaders)
#     "dependency_mods": ["MelonLoader*"], 
#     "copy_dependency_to_profile": [
#         {"dep_source_name": "MelonLoader", "dep_copy2profile_path": "profile_mods/Schedule I/"},
#         {"dep_source_name": "MelonLoader.x64.zip", "dep_copy2profile_path": "profile_mods/Schedule I/"}
#     ],
#     "link_dependency_to_path": [
#         {"dep_symlink_source_name": "MelonLoader", "dep_symlink_path": "Schedule I\\MelonLoader"},
#         {"dep_symlink_source_name": "version.dll", "dep_symlink_path": "Schedule I\\version.dll"}
#     ],
# },

# ================================================================================================================================================

# Real working examples from CZT Mod Manager's code.
# Ignore the fact these  dont include plugin variables. 
#   ↳ CZT doesnt need them in the main code, only in the plugin added profiles. (mod_folder, description, created_by_plugin)
#   ↳ Reference the actual plugin code above for an accurate example.

#     "Ready or Not": {
#         "steam_appid": 1144200, 
#         "launch_exe": [r"ReadyOrNot.exe"],
#         "path": [r"\Ready or Not\ReadyOrNot\Content\Paks\Mods"],
#         "load_order_type": "pakchunkNum",
#         "foldered_mods": False,
#         "allow_file_type_dll": False,
#         "allow_file_type_asi": False,
#         "allow_file_type_pak": True,
#         "symlink_asi_and_dll_to_exe": False,
#         "official_game_data_paks": [],
#         "auto_rename_pak": False,
#         "default_mods_dir": True,
#         "set_mod_dir_name": "Mods",
#         "per_file_symlink": True,
#         "nexus_game_link": "https://www.nexusmods.com/readyornot/mods/",
#     },    

#     "Dying Light 1": {
#         "steam_appid": 239140,
#         "launch_exe": [r"DyingLightGame.exe"],
#         "path": [r"\Dying Light\DW"],
#         "load_order_type": "dataNum",
#         "allow_file_type_dll": True,
#         "allow_file_type_asi": True,
#         "allow_file_type_pak": True,
#         "symlink_asi_and_dll_to_exe": True,
#         "official_game_data_paks": [
#             "Data0.pak", "Data1.pak", "Data2.pak", "DataBr.pak", "DataCn.pak", "DataCs.pak", "DataDe.pak", "DataEl.pak", "DataEn.pak", "DataEs.pak", "DataFr.pak", "DataIt.pak", "DataJp.pak", "DataKo.pak", "DataNl.pak", "DataPl.pak", "DataRu.pak", "DataTh.pak", "DataTr.pak", "DataTw.pak",
#             "SpeechBr.pak", "SpeechDe.pak", "SpeechEl.pak", "SpeechEn.pak", "SpeechEs.pak", "SpeechFr.pak", "SpeechIt.pak", "SpeechPl.pak"
#         ],
#         "auto_rename_pak": False,
#         "default_mods_dir": True,
#         "set_mod_dir_name": "",
#         "per_file_symlink": True,
#         "nexus_game_link": "https://www.nexusmods.com/dyinglight/mods/",
#     },

#     "Dying Light 2": {
#         "steam_appid": 534380,
#         "launch_exe": [r"DyingLightGame_x64_rwdi.exe"],
#         "path": [r"\Dying Light 2\ph\source"],
#         "load_order_type": "dataNum",
#         "allow_file_type_dll": True,
#         "allow_file_type_asi": True,
#         "allow_file_type_pak": True,
#         "symlink_asi_and_dll_to_exe": True,
#         "official_game_data_paks": ["data0.pak", "data1.pak"],
#         "auto_rename_pak": False,
#         "default_mods_dir": True,
#         "set_mod_dir_name": "",
#         "per_file_symlink": True,
#         "nexus_game_link": "https://www.nexusmods.com/dyinglight2/mods/",
#     },

#     "DL The Beast": {
#         "steam_appid": 3008130,
#         "launch_exe": [r"DyingLightGame_TheBeast_x64_rwdi.exe"],
#         "path": [r"\Dying Light The Beast\ph_ft\source"],
#         "load_order_type": "dataNum",
#         "foldered_mods": False,
#         "allow_file_type_dll": True,
#         "allow_file_type_asi": True,
#         "allow_file_type_pak": True,
#         "symlink_asi_and_dll_to_exe": True,
#         "official_game_data_paks": ["data0.pak", "data1.pak"],
#         "auto_rename_pak": False, 
#         "default_mods_dir": True,
#         "set_mod_dir_name": "",
#         "per_file_symlink": True,
#         "per_folder_symlink": False,
#         "nexus_game_link": "https://www.nexusmods.com/dyinglightthebeast/mods/",
#     },

#     "Schedule I": {
#         "steam_appid": 3164500,
#         "launch_exe": [r"Schedule I.exe"],
#         "path": [r"\Schedule I"],
#         "allow_file_type_dll": True,
#         "allow_file_type_asi": False,
#         "allow_file_type_pak": True,
#         "symlink_asi_and_dll_to_exe": False,
#         "official_game_data_paks": [],
#         "auto_rename_pak": False,
#         "default_mods_dir": False,
#         "set_mod_dir_name": "Mods",
#         "per_file_symlink": False,
#         "dependency_mods": ["MelonLoader*"],
#         "copy_dependency_to_profile": [
#             {"dep_source_name": "MelonLoader", "dep_copy2profile_path": "profile_mods/Schedule I/"},
#             {"dep_source_name": "MelonLoader.x64.zip", "dep_copy2profile_path": "profile_mods/Schedule I/"}
#         ],
#         "link_dependency_to_path": [
#             {"dep_symlink_source_name": "MelonLoader", "dep_symlink_path": "Schedule I\\MelonLoader"},
#             {"dep_symlink_source_name": "version.dll", "dep_symlink_path": "Schedule I\\version.dll"}
#         ],
#         "nexus_game_link": "https://www.nexusmods.com/schedule1/mods/",
#     },

#     "7DTD": {
#         "steam_appid": 251570,
#         "launch_exe": [r"7DaysToDie.exe"],
#         "path": [r"\7 Days To Die\Mods"],
#         "load_order_type": "NumName",
#         "foldered_mods": True,
#         "allow_file_type_dll": True,
#         "allow_file_type_asi": True,
#         "allow_file_type_pak": True,
#         "symlink_asi_and_dll_to_exe": False,
#         "official_game_data_paks": [],
#         "auto_rename_pak": False,
#         "default_mods_dir": True,
#         "set_mod_dir_name": "",
#         "per_file_symlink": False,
#         "per_folder_symlink": True,
#         "official_game_data_paks": ["0_TFP_Harmony"],
#         "nexus_game_link": "https://www.nexusmods.com/7daystodie/mods/",
#     },

