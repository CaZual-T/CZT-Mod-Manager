def epic_hotkey(plugin_api):
    current_profile = getattr(plugin_api, 'current_profile', None)
    if not current_profile:
        plugin_api.czt_log('[ERROR][EPIC GAMES PLUGIN] current_profile not set in plugin_api. Please select a profile.')
        return
    cfg = getattr(plugin_api, 'cfg', {})
    profile_mode = cfg.get('profile_path_mode', {}).get(current_profile, '').strip().lower()
    if profile_mode != 'epic-games_plugin':
        plugin_api.czt_log('[WARNING] Epic Games path mode is not selected; scan canceled.')
        return
    plugin_api.czt_log(f'[EPIC GAMES PLUGIN] Epic Pathing mode selected for profile: {current_profile}. Scanning for Epic manifests...')

    def scan():
        manifests = find_epic_manifests(
            plugin_api=plugin_api,
            current_profile=current_profile,
            cfg=cfg,
            save_cfg=getattr(plugin_api, 'save_cfg', None),
            czt_root_folder=cfg.get("czt_root_folder")
        )
        if not manifests:
            plugin_api.czt_log('[EPIC GAMES PLUGIN] No Epic Games manifest data found.')
        else:
            plugin_api.czt_log(f'[EPIC GAMES PLUGIN] Epic Games manifest data saved for profile: {current_profile}')
            for fpath, install_dir, exe_name in manifests:
                plugin_api.czt_log(f"  - {fpath}\n      Game folder: {install_dir}\n      Executable:  {exe_name}")
    threading = getattr(plugin_api, 'threading', None)
    if threading is None:
        scan()
        return
    threading.Thread(target=scan, daemon=True).start()

def find_epic_manifests(plugin_api, max_depth=5, current_profile=None, cfg=None, save_cfg=None, czt_root_folder=None):
    # Search all drives for Epic Games manifest files (*.item) and print their parsed JSON data.
    plugin_api.czt_log("[EPIC GAMES PLUGIN] Scanning for Epic Games manifest files...")
    found_manifests = []
    os = getattr(plugin_api, 'os', None)
    json = getattr(plugin_api, 'json', None)
    if os is None or json is None:
        plugin_api.czt_log('[ERROR][EPIC GAMES PLUGIN] os or json module not available in plugin_api.')
        return found_manifests
    for d in "CDEFGHIJKLMNOPQRSTUVWXYZ":
        drive_root = f"{d}:/"
        if not os.path.exists(drive_root):
            continue
        for root, dirs, files in os.walk(drive_root):
            if os.path.basename(root).lower() == "manifests":
                for fname in files:
                    if fname.endswith(".item"):
                        fpath = os.path.join(root, fname)
                        try:
                            with open(fpath, "r", encoding="utf-8") as f:
                                data = json.load(f)
                            install_dir = data.get("InstallLocation") or data.get("ManifestLocation")
                            exe_name = data.get("LaunchExecutable")
                            game_name = current_profile
                            manifest_game_name = data.get("DisplayName") or os.path.basename(os.path.normpath(install_dir))
                            def norm(s):
                                return str(s).replace(' ', '').replace('-', '').replace('_', '').lower()
                            profile_match = False
                            if game_name and manifest_game_name:
                                if norm(game_name) in norm(manifest_game_name) or norm(manifest_game_name) in norm(game_name):
                                    profile_match = True
                            profile_subfolder = None
                            GAME_PROFILES = getattr(plugin_api, 'GAME_PROFILES', {})
                            profile_info = GAME_PROFILES.get(game_name, {})
                            profile_path = profile_info.get("path")
                            if isinstance(profile_path, list) and profile_path:
                                profile_subfolder = profile_path[0]
                            elif isinstance(profile_path, str):
                                profile_subfolder = profile_path
                            if not profile_match and profile_subfolder:
                                if norm(profile_subfolder) in norm(install_dir) or norm(install_dir) in norm(profile_subfolder):
                                    profile_match = True
                            if not profile_match:
                                plugin_api.czt_log(f"[EPICMANIFEST][SKIP] Manifest does not match active profile: {game_name} vs {manifest_game_name}")
                                continue

                            plugin_api.czt_log(f"[EPICMANIFEST][FOUND] {fpath}")
                            plugin_api.czt_log(f"    Game folder: {install_dir}")
                            plugin_api.czt_log(f"    Executable:  {exe_name}")
                            found_manifests.append((fpath, install_dir, exe_name))
                            if install_dir and exe_name and exe_name.strip() and game_name and cfg and save_cfg and czt_root_folder:
                                if "resolved_exe_paths" not in cfg or not isinstance(cfg["resolved_exe_paths"], dict):
                                    cfg["resolved_exe_paths"] = {}
                                if "resolved_profile_paths" not in cfg or not isinstance(cfg["resolved_profile_paths"], dict):
                                    cfg["resolved_profile_paths"] = {}
                                final_profile_path = build_install_dir_path(plugin_api, install_dir, profile_subfolder)
                                plugin_api.czt_log(f"[DEBUG-EPIC] Final joined profile path: {final_profile_path}")
                                exe_path = os.path.join(install_dir, exe_name)
                                resolved_exe_paths = cfg["resolved_exe_paths"]
                                resolved_profile_paths = cfg["resolved_profile_paths"]
                                resolved_exe_paths[game_name] = exe_path
                                resolved_profile_paths[game_name] = final_profile_path
                                cfg["set_profile_path"] = final_profile_path
                                save_cfg(cfg, czt_root_folder)
                                plugin_api.czt_log(f"[EPICMANIFEST][SAVED] {game_name}:\n    exe: {exe_path}\n    folder: {final_profile_path}")
                            elif not exe_name or not exe_name.strip():
                                plugin_api.czt_log(f"[EPICMANIFEST][SKIP] No executable found in manifest: {fpath}")
                        except Exception as e:
                            plugin_api.czt_log(f"[EPICMANIFEST][ERROR] Could not read {fpath}: {e}")
    if not found_manifests:
        plugin_api.czt_log("[EPICMANIFEST] No Epic Games manifests found on any drive.")
    else:
        plugin_api.czt_log(f"[EPICMANIFEST] Located {len(found_manifests)} manifest(s).")
    return found_manifests

def build_install_dir_path(plugin_api, install_dir, profile_subfolder):
    # Joins Epic install_dir with the FIRST profile subfolder only, never appends multiple paths.
    os = getattr(plugin_api, 'os', None)
    if os is None:
        return install_dir
    if not profile_subfolder:
        return install_dir
    # If profile_subfolder is a list, only use the first entry
    if isinstance(profile_subfolder, list):
        if not profile_subfolder:
            return install_dir
        subfolder = profile_subfolder[0].lstrip("\\/")
    else:
        subfolder = profile_subfolder.lstrip("\\/")
    def normalize_name(name):
        return name.replace(' ', '').lower()
    install_dir_last = os.path.basename(os.path.normpath(install_dir))
    subfolder_parts = os.path.normpath(subfolder).split(os.sep)
    # If the first part of subfolder matches the last part of install_dir (normalized), skip it
    if subfolder_parts and normalize_name(subfolder_parts[0]) == normalize_name(install_dir_last):
        subfolder_to_append = os.path.join(*subfolder_parts[1:]) if len(subfolder_parts) > 1 else ''
    else:
        subfolder_to_append = subfolder
    if subfolder_to_append:
        return os.path.normpath(os.path.join(install_dir, subfolder_to_append))
    return os.path.normpath(install_dir)