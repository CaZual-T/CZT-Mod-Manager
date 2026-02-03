import os
import subprocess

def run(plugin_api, *args, **kwargs):
    try:
        cfg = getattr(plugin_api, 'cfg', {}) or {}

        # Resolve root folder from live config first, then fall back to plugin-relative path
        root = cfg.get('czt_root_folder')
        if not root:
            root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

        exe_path = os.path.join(root, 'plugins', 'scripts', 'UTM_plugin', 'UnleashTheMods_Plugin.exe')

        # Prefer per-profile resolved paths; fall back to any direct path value
        profile = getattr(plugin_api, 'current_profile', '') or cfg.get('current_game_profile', '')
        source = cfg.get('resolved_profile_paths', {}).get(profile) or cfg.get('set_profile_path')

        mods = os.path.join(root, 'profile_mods', profile or 'default')
        staging_area = os.path.join(root, 'mods_source')

        if not source or not os.path.isdir(source):
            plugin_api.czt_log(f"[ERROR] Source folder not found: {source}")
            return
        if not os.path.isfile(exe_path):
            plugin_api.czt_log(f"[ERROR] Plugin EXE not found: {exe_path}")
            return
        if not os.path.isdir(mods):
            plugin_api.czt_log(f"[ERROR] Mods folder not found: {mods}")
            return
        if not os.path.isdir(staging_area):
            os.makedirs(staging_area, exist_ok=True)

        # Build command
        cmd = [exe_path, source, mods, staging_area]
        try:
            proc = subprocess.Popen(cmd)
        except Exception as e:
            plugin_api.czt_log(f"[ERROR] Failed to launch EXE: {e}")
    except Exception as e:
        plugin_api.czt_log(f"[PLUGIN ERROR] Unhandled exception: {e}")
    return