import os
import shutil
import subprocess

from utilities_global.file_system.Required_Folders import build_profile_folder_paths, build_required_root_paths


def run(plugin_api, *args, **kwargs):
    try:
        cfg = getattr(plugin_api, 'cfg', {}) or {}
        log = getattr(plugin_api, 'czt_log', print)

        # Resolve root folder from live config first, then fall back to plugin-relative path
        root = cfg.get('czt_root_folder')
        if not root:
            root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

        exe_path = os.path.join(root, 'plugins', 'scripts', 'UTM_plugin', 'UnleashTheMods_Plugin.exe')

        # Prefer per-profile resolved paths; fall back to any direct path value
        profile = str(getattr(plugin_api, 'current_profile', '') or cfg.get('current_game_profile', '') or '').strip()
        resolved_paths_raw = cfg.get('resolved_profile_paths', {})
        resolved_paths = resolved_paths_raw if isinstance(resolved_paths_raw, dict) else {}
        source = resolved_paths.get(profile) or cfg.get('set_profile_path')

        game_profiles = getattr(plugin_api, 'GAME_PROFILES', {}) or {}
        profile_for_paths = profile or 'default'
        profile_cfg = game_profiles.get(profile_for_paths, {}) if isinstance(game_profiles, dict) else {}
        profile_paths = build_profile_folder_paths(root, profile_for_paths, profile_cfg)
        root_paths = build_required_root_paths(root)

        mods = profile_paths.get('mods_dir', '')
        staging_root = str(root_paths.get('mods_src', '') or '')
        staging_area = os.path.join(staging_root, '_utm_temp') if staging_root else ''

        if not source or not os.path.isdir(source):
            log(f"[ERROR] Source folder not found: {source}")
            return
        if not os.path.isfile(exe_path):
            log(f"[ERROR] Plugin EXE not found: {exe_path}")
            return
        if not os.path.isdir(mods):
            log(f"[ERROR] Mods folder not found: {mods}")
            return
        if not staging_area:
            log("[ERROR] Staging path is not configured.")
            return

        # Get only the selected/checked mods from the mod manager
        selected_mods = []
        if hasattr(plugin_api, 'get_checked_mod_relpaths'):
            selected_mods = [
                str(relpath).strip()
                for relpath in (plugin_api.get_checked_mod_relpaths() or [])
                if str(relpath).strip()
            ]

        if not selected_mods:
            log("[UTM] No mods selected. Check the mods you want to merge first.")
            return

        # Prepare a temp folder with only the selected mods
        selected_mods_dir = os.path.join(staging_area, '_selected_mods')
        if os.path.exists(selected_mods_dir):
            shutil.rmtree(selected_mods_dir)
        os.makedirs(selected_mods_dir, exist_ok=True)

        for relpath in selected_mods:
            src = os.path.join(mods, relpath)
            dst = os.path.join(selected_mods_dir, relpath)
            if not os.path.exists(src):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        if not os.listdir(selected_mods_dir):
            log("[UTM] None of the selected mods were found on disk.")
            shutil.rmtree(selected_mods_dir, ignore_errors=True)
            return

        # Build command: source, selected mods input, staging temp, output profile mods dir
        cmd = [exe_path, source, selected_mods_dir, staging_area, mods]
        try:
            proc = subprocess.Popen(cmd)
            log("[UTM] Merge started. Waiting for completion...")

            def attempt_refresh_on_completion(retries=30):
                try:
                    active_modal = None
                    if hasattr(plugin_api, 'QApplication'):
                        active_modal = plugin_api.QApplication.activeModalWidget()
                    if active_modal is not None and retries > 0:
                        plugin_api.QTimer.singleShot(300, lambda: attempt_refresh_on_completion(retries - 1))
                        return
                    refreshed = False
                    if hasattr(plugin_api, 'refresh_mod_manager_list'):
                        refreshed = plugin_api.refresh_mod_manager_list(delay_ms=0)

                    if not refreshed and hasattr(plugin_api, 'get_mod_manager_tab'):
                        # Fallback direct refresh path in case API helper can't schedule.
                        tab = plugin_api.get_mod_manager_tab()
                        if tab is not None and hasattr(tab, 'refresh_list_args'):
                            from utilities_global.refresh_manager.refresh_manager import RefreshManagerWinList
                            RefreshManagerWinList.refresh_managerWin_list(
                                **tab.refresh_list_args,
                                sort_order=getattr(tab, 'sort_order', 'az'),
                                sort_by=getattr(tab, 'sort_by', 'mod')
                            )
                            refreshed = True

                    if refreshed:
                        # Run a second pass shortly after to catch filesystem lag.
                        plugin_api.QTimer.singleShot(700, lambda: plugin_api.refresh_mod_manager_list(delay_ms=0))
                        log("[UTM] Merge complete. Mod list refreshed.")
                    else:
                        log("[UTM] Merge complete, but refresh was not available.")
                except Exception as refresh_error:
                    log(f"[UTM] Merge complete, but refresh failed: {refresh_error}")

            def check_process_and_refresh():
                try:
                    code = proc.poll()
                    if code is None:
                        plugin_api.QTimer.singleShot(300, check_process_and_refresh)
                        return
                    if code != 0:
                        log(f"[UTM] Merge process exited with code {code}.")
                    else:
                        attempt_refresh_on_completion()
                except Exception as wait_error:
                    log(f"[UTM] Could not monitor merge completion: {wait_error}")

            plugin_api.QTimer.singleShot(300, check_process_and_refresh)
        except Exception as e:
            log(f"[ERROR] Failed to launch EXE: {e}")
    except Exception as e:
        log(f"[PLUGIN ERROR] Unhandled exception: {e}")
    return