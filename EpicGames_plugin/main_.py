import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import epic_hotkey

ui_plugin = True

def run(plugin_api, *args, **kwargs):

    user_setup_tab = getattr(plugin_api, 'user_setup_tab', None)
    if user_setup_tab is None:
        # Defensive: fallback print if plugin_api is missing user_setup_tab
        try:
            plugin_api.czt_log('[ERROR][EPIC GAMES PLUGIN] user_setup_tab not available in plugin_api. Cannot add Epic Pathing checkbox.')
        except Exception:
            print('[ERROR][EPIC GAMES PLUGIN] user_setup_tab not available in plugin_api. Cannot add Epic Pathing checkbox.')
        return

    # Register a hotkey to trigger the Epic Games scan
    if hasattr(plugin_api, 'register_hotkey'):
        plugin_api.register_hotkey('Shift+E', lambda: epic_hotkey(plugin_api))
    else:
        try:
            plugin_api.czt_log('[ERROR][EPIC GAMES PLUGIN] register_hotkey not available in plugin_api. Cannot register Epic Games hotkey.')
        except Exception:
            print('[ERROR][EPIC GAMES PLUGIN] register_hotkey not available in plugin_api. Cannot register Epic Games hotkey.')
        return

    QCheckBox = getattr(plugin_api, 'QCheckBox', None)
    if QCheckBox is None:
        try:
            plugin_api.czt_log('[ERROR][EPIC GAMES PLUGIN] QCheckBox not available in plugin_api. Cannot create Epic Pathing checkbox.')
        except Exception:
            print('[ERROR][EPIC GAMES PLUGIN] QCheckBox not available in plugin_api. Cannot create Epic Pathing checkbox.')
        return

    epic_checkbox = QCheckBox('Epic Games')
    is_epic_games_mode = (
        hasattr(plugin_api, 'current_profile')
        and plugin_api.current_profile
        and plugin_api.cfg.get('profile_path_mode', {}).get(plugin_api.current_profile, '').strip().lower() == 'epic-games_plugin'
    )
    epic_checkbox.setChecked(is_epic_games_mode)
    user_setup_tab.path_mode_layout.addWidget(epic_checkbox)

    def on_checkbox(state):
        if state:
            if hasattr(plugin_api, 'current_profile') and plugin_api.current_profile:
                plugin_api.cfg.setdefault('profile_path_mode', {})[plugin_api.current_profile] = 'epic-games_plugin'
                plugin_api.czt_log('[EPIC GAMES PLUGIN] Epic Pathing mode selected for profile.')
                epic_hotkey(plugin_api)
        else:
            if hasattr(plugin_api, 'current_profile') and plugin_api.current_profile:
                if plugin_api.cfg.get('profile_path_mode', {}).get(plugin_api.current_profile) == 'epic-games_plugin':
                    plugin_api.cfg['profile_path_mode'][plugin_api.current_profile] = ''

    epic_checkbox.stateChanged.connect(on_checkbox)
    if hasattr(user_setup_tab, 'register_pathing_checkbox'):
        user_setup_tab.register_pathing_checkbox('epic-games_plugin', epic_checkbox)
    plugin_api.czt_log('[EPIC GAMES PLUGIN] Epic Games plugin enabled.\n > Select a game profile, then select the "Epic Games" path mode.\n > Use Shift+E to scan for "Epic Games" installations.')




