## Version: 3.1

- Published: Coming Soon (You can go to the github release page and test the latest beta version)
- Url: Coming Soon (You can go to the github release page and test the latest beta version)

- Added support for additional ready or not mod types.
    - FMOD
    - Movies
    - Splash
    - VO_MOD
    - DLL
- Rebuilt plugin API and plugin manager window.
    - Plugin support has been significantly improved.
    - Supports .dll, .exe, and .py scripts
    - Loaded plugins with executable functions will be available in the plugin drop down, top right of the main app.
    - All documentation for plugin users & creators will be posted on the main github page.
    - Move existing plugins OUT of the old scripts/standalone folders into the main 'plugins' folder 
         - You can delete the old 'scripts' & 'standalone_exe' folders as they wont be used anymore.
- Added support for specific game engines along with stubs to implement more via plugins.
    - This is what drives installs and symlinks in conjunction with the profiles global settings.
- Updated Install, Loadouts, Cache, and a few other utilities to work with the new api, engine and file types.
- Added color option for "settings group box".
- Fixed an issue that caused metadata to be wiped from new mod types during update scans.
- Fixed a bug that would break the main layout when unloading a plugin.
     - This was due to destroying the plugins dropdown when no plugins were actively loaded. 
     - This has been fixed by simply 'hiding' it when it isn't in use. 
- Resizable window to help fit other languages.
     - CZT will remember its last location on screen when closed. (kinda like windows explorer)
     - New hotkey to recenter the window. (F5)
- Added patch notes button to main menu. 
     -  There is an option to force check for updates on this popup aswell.
- Small qol addition for future updates. beta version will show up to 5 of the past version instead of just the 1 most recent.
- Updated language files to be current with new logs, also added a few things i missed previously like the hotkey list.
- Added dev tool plugins to the main repo.
- tweaked main user config format.
     - moved color and font settings into styles_config.json 
- updated dialog windows for install, replace, download, and loadout prompts. 
     - unified style and much cleaner work flow. 
- added a 'download selected' button on the manage tab.
- tweaked global progress bar.
     - added a popup that displays all downloads happening in parallel. 
     - more accurate progression tracking.
     - triggered upon all major functions.
- fixed an issue that would make the app appear frozen when attempting to move the window while saving loadouts.
- fixed grid view
     - add / subtract columns on window resize.
     - larger tiles.
     - reorganized info displayed. 
- updated mod entry window (this is the window that appears when right clicking a mod)
     - mod stats (downloads, endorsements, dates)
     - description.
     - local and remote info (version, size, file name etc)
     - added progress bar to the popup itself during actions. (save & check for update)
     - reorganized layout. 
     - removed old force options.
     - refresh icon on this window is now the 'check for updates' button.
     - relocated download button (top right but beneath the checck for updates icon)
     - added delete button.
- changed scrolling from step to per px, so scrolling through mods will be smoother.
- disabled scroll wheel from effecting drop down boxes. 
- made a few changes to the overall app window to handle resizing better. (especially useful for other languages)
- manage tab search bar now supports categories. (try typing 'audio' 'weapons' 'visual' etc)
- fixed an issue that caused loadouts to apply incorrectly if all mods were disabled at the time of applying. 
     - main problem: czt was enabling mods that weren't listed within the selected loadout. 
          - this mainly effected FMOD, VO_MOD, Splash, Movies.
 - cleanup and consolidation of redundant functions.
 - updated language files.
 - fixed button styling for additional languages.
 - czt overview corner (bottom left, main menu)
	 - click to change widgets.

## Version: 3.0.9.2
 
- Published: 2026-05-01
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.9.2

- Added progress bar to the app update process.
- Added progress bar to 'Auto download mods flagged as update available' (swear i did this before lol)

## Version: 3.0.9.1

- Published: 2026-04-21
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.9.1

- Updated language files for the following:
   - Load order menu.
   - Plugins menu.
   - Mod manger tab info.
   - Mod entry popup.
- Fixed a few areas where text was clipping behind other ui elements.

## Version: 3.0.9.0

- Published: 2026-04-20
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.9.0

- fixed the buttons on the 'restore backup' delete backup popup.
- fixed an issue that caused category names to not be applied upon download.
   - note: update scans will backfill missing metadata.
- fixed spinboxes in custom settings.
- misc custom setting improvements related to font and color options.
   - live language, font, and color previews.
- fixed a bug that caused the music volume slider to fallback to defaults when set to 0%.
   - music slider will adjust the volume in realtime.

- migrated to nexus api v3 for update scans.
   - significantly more accurate.
   - tracks file ID and direct file version instead of comparing to the overall page version.

## Version: 3.0.8.5

- Published: 2026-04-15
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.8.5

- Centralized custom options module (more v3.1 prep, nothing you'll notice on the outside)
- New settings for font and color options.
   - Hover Effects: border, text
   - Text Effects: all, hover 
- Migrated czt patch notes from release descriptions to the new [patch notes](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/patch_notes.md) file.
- Updated [language files](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main/language_packs).
   - Main Menu button text.
   - Settings color/font button text. 

## Version: 3.0.8.4

- Published: 2026-04-13
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.8.4

- Fixed a crash that would occur on startup when "scan mods for updates on startup" was enabled.
- Crash monitor logs will auto clear once they reach 2mb in size.
- Crash monitor log locations:
  - Win key, search: %appdata% 
    - App Data/Local/CZT Mod Manager/logs/
   - Root
     - press ctrl + o in app to open the root location.
       - CZT Mod Manager/logs/
- Log files in both app data and root mirror eachother.
- View the file in appdata if you crash on startup. (most reliable)
- View the file in czt root for ease of access but note that it can miss logs that are created before the config is found on startup.

---

## Version: 3.0.8.3

- Published: 2026-04-12
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.8.3

- Updated language files.
   - Buttons, Sub Menus, and Popups all have custom language keys now.
- Added 2 new languages (es, ru) (ai translated)
   - I personally wont be adding any more. Mainly added these 2 just to ensure that it all worked properly. 

⚠️ Read the patch notes for v3.0.8.2 If you still aren't on v3.0.8.0+ by the time you see this.  
   - warning above only applies to users on v3.0.7.7 or earlier

---

## Version: 3.0.8.2

- Published: 2026-04-11
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.8.2

⚠️ READ THIS If you're updating from 3.0.7.7 

- BEFORE UPDATING - 
- Close this update popup, then go to the manage tab and click create backup (choose > backup files + list)
- After the backup completes, Press ctrl + o > Create a backup of your 'CZT Mod Manager' folder.
- You can now Restart CZT and update to 3.0.8.2
- Report your crash logs to the discord if you crash upon startup after updating.

⚠️ New users (3.0.8.0+) and legacy users that got 3.0.8.0 to work on their own: 
   - You can ignore the warning above and proceed with update.

Patch Notes:
- started crash monitor earlier to ensure logs are generated even during crashes at launch.
- auto open startup crash logs upon crash. (AppData/Local/CZT Mod Manager/logs/)

---

## Version: 3.0.8.0

- Published: 2026-04-10
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.8.0

- improved install/extract process for loadout installs.
- fixed a crash that would occur when more than 75+ mods were installed at once.
- restructured czt root file system.
- added physical crash logs (czt root/logs/)
- backend modules cleaned up, and getting everything ready for v3.1

---

## Version: 3.0.7.7

- Published: 2026-04-04
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.7.7

---

## Version: 3.0.7.6

- Published: 2026-04-04
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.7.6

- Fixed a bug that was causing version mismatches when using the Manual Download button on nexus. (czt extension)
- This issue was causing instant 'update available' flags in some cases even if the user just installed the mod. 
- I thought i fixed this in v3.0.7.2 but i guess i missed it in the extension handler. my fault.

---

## Version: 3.0.7.5

- Published: 2026-04-04
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.7.5

- Fixed a bug that caused custom names to be overwritten when "auto download mods marked as 'update available' " was enabled.
- Fixed F9 'missing mods from loadout detection' false positives.
- Added unhandled exceptions to the main logs so you don't need to open the debug window to see them.
- Added custom language support.
   - Default is English
   - You can download the example language pack files from github. 
   - If you create a translation pack, feel free to release those translation files as your own mod on nexus. Just tag me!
   - Language packs are installed at (root) CZT Mod Manager/plugins/language_packs/>pack folder<

---

## Version: 3.0.7.2

- Published: 2026-04-02
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.7.2

---

## Version: 3.0.7.1

- Published: 2026-04-02
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.7.1

- HOTFIX:
  - Fixed a metadata sync issue that was happening when a user would update an existing mod. 
    - This error caused the version number to never increase, resulting in an 'update available' loop.

---

## Version: 3.0.7

- Published: 2026-04-02
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.7

- Refactored install logic:
  - Dying Light profiles: 
    - Will now always prompt you to replace or install as new. 
    -  Auto rename pak files to avoid conflict.
  - Schedule I:
    - Fixed the issue where .dll kept getting force sent to exe instead of mods folder.
    - Fixed the profiles internal config settings.
- Added an install safety:
  - This will prevent accidental installs into the wrong profile by comparing the active profile to the incoming metadata at the time of download.
- Removed old legacy functions and unused code.
- Removed manual dataN.pak patcher button from main menu tab.
- Removed deselect all button from main menu tab (select all [✔️] now does both)

---

## Version: 3.0.6.8

- Published: 2026-04-01
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.6.8

- Fixed an error that was preventing CZT from creating a "Mods" folder when it was missing from the active profiles directory. (RoN, S1)
- Added Xbox Games platform support for Ready or Not.

---

## Version: 3.0.6.6

- Published: 2026-03-31
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.6.6

- File selection prompts include main and optional categories. (in both download and loadout pins)
- Fixed a bug that would cause custom display names to be overwritten when updating/validating a loadout.
- Fixed an issue that would cause standard users to get redirected to a mods page after using "mod manager download"
- Fixed a bug that would lead to premium account users to have double downloads in some cases.
- Fixed DataN.pak patcher.
- Added 'pause menu music when game is launched' option.
- Clean function is now a popup with 3 selectable options.
  - Remove stale entries from mod list.
  - Delete in-app download history.
  - Remove existing symlinks from current profile.
- Updated launch game popup to be more descriptive.
- Updated UTM plugin (check main github page for more info + download)
  - https://github.com/CaZual-T/CZT-Mod-Manager/tree/main/UnleashTheMods-5.0_plugin
- Updated czt nxm bridge extension. (check main github page for more info + download)
  - https://github.com/CaZual-T/CZT-Mod-Manager/tree/main/CZT_Extension

---

## Version: 3.0.6.5-beta

- Published: 2026-03-30
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.6.5-beta

- test build for czt nexus extension.
- go to https://github.com/CaZual-T/CZT-Mod-Manager/tree/main/CZT_Extension for more info.

---

## Version: 3.0.6.2

- Published: 2026-03-27
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.6.2

- All download buttons now work for free users by instantly redirecting you to the mods download page.
  - Premium users can still remote download with one click of course.
  
- Thank you Kurtis from @NexusSupport for the suggestion.

---

## Version: 3.0.6.1

- Published: 2026-03-27
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.6.1

### Updated API:
  - Using the "Mod Manager Download" button to download files on the nexus site will now automatically send the file directly to CZT to download & install.

    - download this update.
    - start czt.
    - open nexus mods in your browser.
    - download a mod using the "Mod Manager Download" button.

### Premium account users:
  - Not only can you take advantage of the feature above, but I've also added an in-app browser feature that allows you to install any mod with 2 clicks without ever leaving the app. 
    - first go to your settings in the main menu, and under general you need to enable the CZT browser option.
    - next, go to the manage tab. click the button in-between restore backup (admin shield icon) and delete (trash can icon) at the top. the button looks like a magnifying glass on a piece of paper.
    - once the window opens, navigate to the mod of your choice, open its page, then click the download button in the top right. You don't even have to go to the files tab in the browser. literally just click a mods, click download top right. done.

### QOL Changes:      
  - Fixed a bug that would cause the wrong path to be set for the current profile at the time of running steam detection.

  - New Controls (manager tab):
     - Backup/Restore.
     - Loadout manager (majorly improved)
        - update, verify links, merge, load, save, overwrite, download missing.
     - Loadout quick actions.
  
  - Rebuilt the settings window + added NEW features:
    - New General Settings:
       - use downloads folder as source
       - use mods_source folder  as source 
       - only check enabled mods
       - auto download mods flagged
       - protect enabled mods from deletion
       - auto delete archives after install
    - New Advanced Settings:
       - Max downloads.
       - Max background threads available for processes.
       - Live progress log threshold (how big a file has to be to trigger progress log in main menu)
       - Cache file selection (per session).
       - Cache file selection (persistent).
          - auto clear cache file threshold (file size limiter).
       - Similarity Detection Controls:
          - read the scrollable text box in the 'advanced' column for more info on this specific setting.

---

## Version: 3.0.6.0-beta

- Published: 2026-03-26
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.6.0-beta

- added in-app browser (replaced merge button)
   - DL users, if you used the merge, sorry, use the UTM plugin. 
- direct access to nexus site for downloads
- site functions just like it does in a normal browser.
   - no sign in required because CZT uses your nexus api key to communicate. 
- premium users can use the top right 'download+install current mod' button.
   - Auto applies all metadata to your profile_mods_list.json file. 
- standard accounts still have to manually download the file like normal 
   - (you can do it in the app browser), then install, and enter the ID.


Note: This version of CZT is a bit larger (139mb) than past versions due to the PySide6-WebEngine library.

---

## Version: 3.0.5.3-beta

- Published: 2026-03-25
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.5.3-beta

- Fixed a bug that would cause the wrong path to be set for the current profile at the time of running steam detection.

---

## Version: 3.0.5.2-beta

- Published: 2026-03-25
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.5.2-beta

- New Controls (manager tab):
   - Backup/Restore.
   - Loadout manager (majorly improved)
      - update, verify links, merge, load, save, overwrite, download missing.
   - Loadout quick actions.

- Rebuilt the settings window + added NEW features:
  - New General Settings:
     - use downloads folder as source
     - use mods_source folder  as source 
     - only check enabled mods
     - auto download mods flagged
     - protect enabled mods from deletion
     - auto delete archives after install
  - New Advanced Settings:
     - Max downloads.
     - Max background threads available for processes.
     - Live progress log threshold (how big a file has to be to trigger progress log in main menu)
     - Cache file selection (per session).
     - Cache file selection (persistent).
        - auto clear cache file threshold (file size limiter).
     - Similarity Detection Controls:
        - read the scrollable text box in the 'advanced' column for more info on this specific setting.

---

## Version: 3.0.3-stable

- Published: 2026-03-20
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.3-stable

- Module optimization.
   - Refactored the following functions:
      - install mods
         - improved comparison logic during install. 
      - launch game
      - loadout system
      - refresh manager
      - nexus (updates, mod info parsing, downloads)
- The czt update notification will show patch notes from the 3 most recent updates.

---

## Version: 3.0.2.8-beta

- Published: 2026-03-20
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.2.8-beta

- testing, and feedback is appreciated.
- backend module optimization.
   - logic refactored:
      - install mods
      - launch game
      - loadout system
      - refresh manager
      - nexus (updates, mod info parsing, downloads)
- the czt update notification will show patch notes from the 3 most recent updates.

---

## Version: 3.0.2.7

- Published: 2026-03-19
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.2.7

- Fixed a bug that caused CZT to crash during install after in app downloads.
- Implemented multi threaded actions:
   - improved download speed.
   - improved update scan speed.
   - improved detect steam library speed.
   - improved install speed.
   - improved write speed (to mod list json).
- Updated progress bar logic:
   - Large actions are linked to the progress bar on both the main and manage tab.
- Improved logs for install and download process.
- Added a prompt for users to choose which mod they want to install when a mod archive has multiple options nested inside.
- New 'beta release' option in settings. 
   - Enable this for pre release builds. 
      - Main version releases will be released at a more controlled rate after this update. If you want the latest build with potential new features and would like a say in approving/denying features before i add dumb shit i suggest enabling this feature in settings and joining the discord. More feedback = Better results)

---

## Version: 3.0.2.1

- Published: 2026-03-17
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.2.1

### v3.0.2.1
- Updated the dialogue on the install safety popup to be more direct.

### v3.0.2.0 (previous patch notes)
- Added direct download for premium nexus users. (nexus API restricts free users.)
  - Blue arrow next to file size in list view. 
- Loadouts:
   - When exporting a loadout you can choose to include a specific file id for mod pages with multiple options. (this will auto prompt)
      - Added "download mod list" to the loadouts menu. 
- New Sort filters (hidden, and removed on top)
    - When you scan mods for updates there's 4 statuses it can be in > up to date, update available, hidden or removed,
- Fixed mod deletion not working when a mod was in the disabled state.
- Added a safety to the install process that allows the user to select which file they would like to update upon install if a match is found.
   - This will help prevent improper replacements when creators slightly change a mods file name.

### v3.0.1.6 (previous patch notes)
- Fixed mod deletion not working when a mod was in the disabled state.
- Added a safety to mod install process that allow the user to select which file they would like to update upon install if a match is found.
   - This will help prevent improper replacements when creators slightly change a mods file name.

---

## Version: 3.0.1.5

- Published: 2026-03-14
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0.1.5

## Changes made in 3.0.0.1-3.0.1.5

- 3.0.1.4 Patch Notes:
   - Enhanced the install process of existing mods. CZT can now detect small file name differences
     - Example, if you updated a new version of SuperTacticalM4a1_DW3.pak, but the new version is SuperTacticalM4a1_BP4.pak, czt will know to replace the old file.

- 3.0.1.3 Patch Notes:
   - New loadout features:
      - Import Loadouts (meaning you can share your loadouts.json file with friends)
      - Export single loadout.
      - Export ALL loadouts.
   - New loadout manager features:     
      - Overwrite existing (select a profile then click save current)
      - Multi select and delete (ctrl + left click to select multiple)
   - New 'Mod Manager' tab features:
      - Sort by category 
      - Category displayed by authors name (list view only)

- Patch Notes: Version 3.0.1.2   
   - Reworked mod update detection.
      - Mods will now remain marked as "update available" even if the creator doesn't bump the page version number.
      - This works by comparing install date (local) to the most recent upload date (on nexus)
   
- 3.0.0.1/3.0.1.1 Patch Notes:
   - Fixed a load order issue for ready or not.
   - Fixed an issue where certain mods wouldn't appear for ready or not when symlinked. 
      - Typically these mods were character asset related like tattoos and custom models. 
      - The main problem was how my load order system renamed files and removed the prefix _P.... 🤦‍♂️
   - Added a progress bar to the main menu. 
      - Progress bar will only appear during mod installation, it will disappear once completed.
   - Fixed the Large/Small file size sort filter.
   - Fixed the new user log. Now it will say "click setup button" instead of "go to user tab"

---

## Version: 3.0

- Published: 2026-02-07
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/3.0

### Main
- Upgraded from PyQT5 to Pyside6 gui library.
- Everything UI related has been rebuilt from scratch.

### New features
- TOOLTIPS: hover over almost any widget or button to get a brief description.
- Loadouts. (allows you to save groups of mods and quickly swap between presets)
- Right click clicking mod entries will display a popup with the selected mods info etc.
   - That popup is also where you save the nexus link and display name now.
   - Clicking the refresh icon in that popup force refreshes all info.
- Storage overview. (Disk Usage, Mods enabled/disabled, Corrupted, Updates Available)
- List/Grid view for manage tab. (huge QOL improvement)
- Click mod image to open nexus link. (List view only, click 🔗 in grid view)
- Toggle switch to enable/disable mods. (individual or all)
- New sort filters. (11 in total)

### Improved:
- 'Launch Game' flow. (added logic to detect if running as admin/dev)
   - Popup will explain why admin is needed for symlinks.
   - Gives 3 Options, Run as admin/Open Windows Settings/Cancel
   - Personally i use Dev mode to avoid it all together 
      - click the "open windows settings" button.
      - scroll down to developer mode > enable.
- Check for mod updates. (faster)
- Overall app flow.
- Fixed highlight color in merge utility window.

### Removed from manage tab:
- Save mod data button. (moved to right click menu)
- Force options. (essentially replaced by the refresh button in right click menu)

### Recommendation
- Reset ALL of your custom color and font settings to default after applying this update.

---

## Version: 2.0.1.7

- Published: 2026-02-03
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/2.0.1.7

## Fixed
- Fixed dead Discord invite link (Join Discord button).
- Fixed toggle state and config sync for “Run at Startup” scripts.
- Fixed crashes when root/config didn’t exist (Save Config / Launch Game).
- Improved Steam detection depth (now 5 folders).

## Plugin System
- Plugin menu now has 3 options:
  - Profile (only works for that profile)
  - Global (works across all profiles)
  - Run at Start
- Added “Run at Startup” option in plugin manager (F3).
- Plugin API updated (docs coming soon).
- Plugin support: Press F3 to open menu.
- Plugin folders auto-created if missing:
  - EXE plugins: `CZT Mod Manager/plugins/standalone_exe`
  - Scripts (.py/.bat): `CZT Mod Manager/plugins/scripts`

## New/Updated Features
- Added documentation on GitHub for creators.
- Added plugins to main GitHub page:
  - ProfileAddon
  - UnleashTheMods Merge Utility
  - Epic Games (path mode)
- Dev plugins:
  - dev_api_viewer_plugin
  - dev_ui_scanner_plugin

## Memory System Updates (v2.0.1.5)
- Load order menu (F2)
- Launch game logic
- Autosave system
- Profile selection
- Path mode selection
- Plugin menu options

## Quality of Life
- Missing root folders auto-created at startup.
- Improved plugin manager UI and functionality.
- Path normalization for game launch and symlinks.
- Added help logs for new users.

## Notes
- The goal is a community-friendly plugin system supporting profiles, path modes, and live variables.
- Another update will address the load order menu.
- Soon personal API keys won’t be required. I'm waiting on Nexus approval for CZT. Once approved we will be able to generate keys like other official managers.

---

## Version: 2.0

- Published: 2026-01-23
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/2.0

### IMPORTANT NOTES:
Ready or Not users pre v2 (updated from v1.9.x.x):
- Go to czt root folder > profile_mods> ready or not > open mod.czt  
- Move all mods from that folder into the one before it. Then delete the mod.czt folder.
- If you have an active symlink > delete the mod.czt folder there too. 
- You can get there by clicking browse in the Main Menu tab while having RoN set as your profile.

All users pre  v2 (updated from v1.9.x.x)
- Go to czt root folder > profile_mods >
- Open any profiles you may use and delete the _disabled_ folder.

## UI Changes:
- Complete UI rebuild. (Fully Redesigned)
- Tabs combined to ensure a smoother user experience.
- Moved all settings (including setup) to the settings tab.
- Moved install tab to main menu.
- Install controls redesigned.
- Moved mod manager forcible options to a toolbox.
- Mod manager controls redesigned.

## Bug Fixes/Improvements:
- Search function enhanced.
- Backend modules optimized.
- Improved install success/failure logs.
- Fixed app icon not always appearing in popup windows.
- Fixed fonts not applying to select elements.
- Fixed a bug where a random 'mods' folder would generate when using DataN patch.
- Forcible options on the manager tab are now persistent.

## New Global Features:
- Cancel button to the 'Launch Game' popup.
- Load order menu (Press F2)
- Multiple hotkeys:
	- CTRL + SHIFT + L : launch game from any tab. 
	- SHIFT + C : print full cfg to log box. 
	- SHIFT + H : list all available hotkeys. 
	- CTRL + O : open root folder.
	- SHIFT + R : list resource paths.  
        	- You can replace fx and img files in the resource locations if you want.
        	- Add menu music to the folder in CZT Mod Manager\audio\menu_music

## Game Specific Features:
- Dying Light Games:
	- Improved merge utility. Now compares using diff instead of line by line.
	- New selection method for merge conflicts. (simple + advanced)
	- All merged lines will have // Merged by (or) Patched by CZT

---

## Version: 1.9.1.317

- Published: 2025-11-27
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.1.317

- Fixed a bug that caused steam users to crash upon launching their selected game.
- This was due to a small oversight during the testing of manual pathing. My fault.

---

## Version: 1.9.1.316

- Published: 2025-11-26
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.1.316

Added option for manual pathing.
- This allows users to override the steam library pathing and set game paths for ANY platform. (EPIC Games, tactically acquired, etc)
- You can set pathing per profile. Meaning DL1 could use auto , and DL2 could use manual, and CZT will know which method to use without needing to restart the app.
- Auto pathing is still based on steam libraries.

New custom settings:
- All settings can be enabled/fully disabled in the custom settings tab (imagine that)
- Sound effects for click/hover (buttons)
- Menu audio  with adjustable volume slider. You can upload your own file to use, hover over the drop down box for instructions,)

---

## Version: 1.9.1.31

- Published: 2025-11-23
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.1.31

- Added a launch elevation prompt. (this will only effect users that have perm issues with symlink @ game launch)
- CZT will attempt to link when 'launch game' is pressed, if it fails due to a permission error, it will ask to relaunch CZT with admin perms.
- I'm tired of explaining this to people so I'm just adding this check.

**NOTE_1:**  If CZT is running as admin it will break the drag and drop feature. This is a Windows limitation. This happens because when czt is running as admin, it has higher perms than explorer. 

**NOTE_2:** If you didn't need admin perms to use CZT before, don't worry, you still don't need them.

---

## Version: 1.9.1.3

- Published: 2025-11-22
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.1.3

- Fixed a bug that caused CZT to crash upon clicking the ‘select outdated’ button.
- Fixed a bug that prevented users from being able to use ‘select outdated’ on folder based mods.
- Fixed a visual bug that displayed the wrong profile in search bar placeholder text.
- Matched the styles within the 'restore' and 'delete' popup windows.
- Changed text color in 'delete' and 'restore' popups to white for better visibility.
- Added Select/Deselect all buttons to the 'restore' popup.

---

## Version: 1.9.1.0

- Published: 2025-11-21
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.1.0

# Added the following features to the manage mods tab:
- Search bar to easily jump to any mod.
- Shift + left click mod name to edit the display name.
- Sort mods A-Z/Z-A by mod display name.
- Sort mods A-Z/Z-A by mod creator name.
- Creator name next to mod name in ui.
- Force update install date checkbox.

---

## Version: 1.9.0.3

- Published: 2025-11-18
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.0.3

- Updated launch logic to use steam app IDs.
- Fixed "Steam client is required" popup at launch for all Dying Light games.

IMPORTANT: RUN "Load Steam Libraries" again so CZT can save steam.exe to your config. This is to ensure the new feature works as intended.

---

## Version: 1.9.0.2

- Published: 2025-11-01
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.0.2

- Separated the "update local info" checkbox logic in the manage tab.
- Added individual checkbox for display name.
- Each check box is now an individual function. Allowing users to have complete control over forcible options. 

- The old style just updated all of that info at once. Resulting in unwanted overwrites for mods that utilized a manifest file at install.

<img width="706" height="55" alt="{FA45E4D1-972C-4C6C-8A23-96BB5F6907C2}" src="https://github.com/user-attachments/assets/0d5f4247-90e6-49f7-9f62-c44de8b57743" />

---

## Version: 1.9.0.1

- Published: 2025-10-31
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.0.1

[Creators]
- I updated how CZT reads _mod_info.json for file base mods (.pak, .dll, .asi etc)
- Format is much cleaner and easier to maintain.
- It also supports an unlimited amounts of file names so you could potentially make packs that a user could literally then install at the click of a button. 

> Review Mod_Creator_README.rar for actual mod examples.

---

## Version: 1.9.0

- Published: 2025-10-30
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.9.0

[Manifest support]
- Mod creators can now add _mod_info.json files inside their zipped folders to include a display name, current version number, and mod url information.
- Mod creators will also be able to specify files or folders to install within the manifest to ensure their mods get automatically installed properly.
[!] See attached file Info_For_Mod_Creators.rar

[Refactored logic for the following functions]
- Launching games 
- Symlink (enabled/disable mods at launch)
- Supporting symlink functions and precise profile variables to ensure proper linking (enable mods)
- Installation methods 
- Supporting install functions for raw, compressed, and manifest driven mods.

[Added]
- New DataN.pak patcher for Dying Light Games.
- 7DTD Profile.
- Folder based mod support.

[Removed]
- Auto rename DataN.pak at install (use patcher now)

---

## Version: 1.8.1

- Published: 2025-10-24
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.8.1

- Added the ability to toggle mods individually. 
- Disabling a mod within the manager tab prevents it from being loaded at launch.
- You can restore disabled mods at anytime.
- Added "Disable Selected" button.
- Added "Restore Disabled" button.
- UI improvements. 
   - Fixed the install time not displaying within the manage tab ui when a user installed multiple mods while using the "auto rename" option.
   - Added the ability to toggle mods individually. 
   - Disabling a mod within the manager tab prevents it from being loaded at launch.
   - You can restore disabled mods at anytime.
   - Added "Disable Selected" button.
   - Added "Restore Disabled" button.
   - Fixed the install time not displaying within the manage tab ui when a user installed multiple mods while using the "auto rename" option.
   - Fixed the "delete selected" button in the install tab, it now functions as it should.
   - Fixed local version install date not appearing within the manage tab ui.
   - Improved informational logs for common processes.
   - Added debug logs to improve support and pinpoint potential errors.
- [QoL/Performance Update]
   - Optimized the changes implemented within 1.8.0.2
   - Faster and more precise scanning/detection for game install paths/exe.
   - Improved initial setup experience, fixed a few bugs that caused users to have to restart the app after initially creating root in order for CZT to detect the root folder and the selected profile exe.
   - Added Multi-Drive Steam Support.
      - Steam libraries are now detected across all existing drives (C-Z), including separate game install locations.
      - This means you can have steam installed on one drive, and your games separated amongst other drives and CZT will detect it.
   - Added a "Load Steam Libraries" button to run library detection at anytime.
   - Fixed mod images not updating correctly upon clicking save data when an image of the same name already existed.
   - Fixed the crash that would occur upon clicking 'save data' in manage tab.
   - Fixed a ui bug that caused unreadable elements for new users.
   - Expanded upon exe detection logic.
   - Added 2 new custom settings (log box font, log text color)

---

## Version: 1.8.0

- Published: 2025-10-20
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.8.0

- Fully converted to PyQt5
- Completed the conversion of all the remaining cTk elements/windows to PyQt5. 
- Removed old cTk window. (These features can now be found in the MAIN tab) 
- Everything is now in one window, utilizing 4 tabs > Main, Install, Manage, Settings.
- Fixed an issue where some users' configs would not load at startup.
- Fixed an issue that prevented new users from creating a root directory.
- Fixed an issue where color and font settings could have multiple defaults.
- Fixed an issue where CZT would not read the user's Nexus API key after saving.
- Fixed an issue where the config would not load properly across all tabs.
- Fixed an issue where the mod list would not update until CZT was restarted.
- Fixed an issue where the merge button would not update until CZT was restarted.
- Fixed an issue where the Nexus API key would not update until CZT was restarted.
- Fixed an issue where the mod update check always reported mods as up to date, even when outdated.
- Refactored Nexus API logic to use global functions for consistency.
- Fixed argument mismatch errors after moving Nexus functions to global scope.
- Improved config reload logic so all tabs reflect changes immediately.
- Improved error handling and user feedback for mod info issues.
- Improved debug logging.

---

## Version: 1.7.1.3

- Published: 2025-10-17
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.7.1.3

- Added Dying Light 1 Support.
- Added actual nexus names for data.pak style mods. Now it will display in ui as data.pak (Mod_Name)
- Added a simple option and advanced option for merging src/def files.
- Added scrollable window with diff when merging json formatted files.
- Added support for .def files in merger.
- Added settings tab that allows users to change colors and fonts.
- Added settings for launch options.
- Added settings for home tab selection.
- Removed Install button from main window.
- Removed "Install on DnD" checkbox from settings tab (function isn't ready yet)
- Fixed .gui files merging.
- Fixed structure and flattening issues.
- Fixed a crash that would occur if a user attempted to save custom settings when using the "Set Manage Tab to Home" checkbox.
- Fixed Dying Light mod previews overlapping profiles. This happened due to them all sharing datax.pak names.
- Restructured how mod previews are saved.
- Updated czt release notification popup.
- Now automatically downloads and runs installer when user clicks 'Get Update"
- Created new manager window that hosts tabs for all needed UI (install, Manager, Settings)
- Merged Install and Manager windows into 1 main window. (no more having to go back and forth between popups)
- Restructure and modular workflow.
> ALL USERS: Please go to your source folder (click the top left button) and delete your current mods_preview folder.
- This is to ensure compatibility with the new file structure. CZT will recreate and redownload your mod previews accordingly.

---

## Version: 1.6.5.3

- Published: 2025-09-29
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.6.5.3

- Rebuilt my drive, path, and steam library detection.
- Optimized method used to find .exe and other custom pathways
- Optimized load times when changing profiles.
- Fixed custom path exe not found
- Fixed custom path source not found
- Fixed custom library not found
- Added "rename_paks" checkbox to install window (will rename paks when multiple mods share the same name)
- Added ASI and DLL support to Dying Light The Beast and Dying Light 2.
- Added the ability to individually select which mods get merged instead of just batching all of them together.
- Fixed config not loading on startup.
- Fixed drive letter compatibility issues for root folder. (i'm a dumbass and had it hard coded still)
- This time around i tested on C,D, H, and Z
- Works on any drive type including detachable storage like USB.
- Improved and rebuilt merging logic.
// CZT + {Mod it came from} on all lines merged by CZT.
- Fixed an issue that would cause the app to crash when merging after deleting a pak that was actively symlinked.

---

## Version: 1.6.1

- Published: 2025-09-26
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.6.1

- Fixed mod preview images going blank when refreshing. 
- Added mod merge functionality for dying light games
- Changed UI layout in manager window to adapt more controls.
- Fixed "clear source after install" option.
- Fixed symlink for alternative Steam locations.
- Fixed the issues with DL The Beast not launching.
- Added compatibility for users that don't have steam installed in Program Files. x86

---

## Version: 1.5.5

- Published: 2025-09-17
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.5.5

- Converted Install Popup (and others from cTk to PyQt5) PyQt handles long lists and overall heavy gui better.
- Fixed an issue that was preventing the nexus link from saving and loading persistently on some profiles.
- Removed dead (unused) code.
- Added a check at launch that alerts the user that a new version is available for CZT.
- Fixed install time ui not showing properly.
- Fixed an install issue that caused czt to overwrite the same entry within the mod list json when multiple mods were installed at once.
- Fixed an issue where dying light paks would also extract the .pak files contents
- Fixed an issue that prevented schedule 1 from extracting and linking dependencies properly.
- Updated the logic that determines if a mod is outdated
- Updated what nexus meta data gets saved on each step to ensure proper tracking.
- Added 2 new check boxes that allow users to Force update local data and Update the mod preview image.
- Added mod preview image.
- Fixed a crash when trying to drag the main window with the manager window open at the same time
- Fixed an issue where the local version would update even though the mod hadn't been updated yet.
- Fixed the text of a few labels
A few other things but its 5:45am and my brain hurts lol

---

## Version: 1.5.0

- Published: 2025-09-13
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.5.0

- Rebuilt mod manager window. Converted from cTk to PyQt5. This helped with lag issues when scrolling long lists of mods.
- Added Local and New version labels to mod manager window.
- Add nexus link entry for each mod
- Buttons: Select all, Select Outdated, Deselect all, Open selected, Delete Selected, Save Nexus Links, Check for Updates
- Progress bar for Saving Links and Checking for Updates.
- Fixed an issue that was causing an AV flag due to the method used to scan for available drives.
- New method saves selected drive to config at time of using "create root" instead of scanning for the root on every start.
- Made it an option for users to move the root folder from their desktop to any drive.
- Added, Drag and Drop your downloaded mods onto the log box to stage mods. This auto moves the mods to the source (mods_go_here) folder so you dont have too.
- Added, Install mods button now opens a popup and allows you to select which ones to install.
- Added, Uninstall mods is now "Manage Mods" and will open a popup that allows you to select each mod you want to delete.
- Removed Admin requirements.

---

## Version: 1.0.4

- Published: 2025-08-22
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.0.4

- Fixed launch failure
- Fixed false av flags.
Note: there is still one flag on virus total. This is probably due to this tools ability to unzip and move files. Obviously theres no way around this because thats literally what the tool is supposed to do. It can only install what you put into the mods_go_here folder.

### Update from previous versions:
- RENAME YOUR CURRENT CZT Mod Installer folder on your desktop to CZT Mod Manager before launch.
- You can also uninstall the old "CZT Mod Installer". No bs part of the av flag was due to the name having "installer" in it....insane.

---

## Version: 1.0.2

- Published: 2025-08-17
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.0.2

- Ui Rework
- Fixed a backend issue where profiles werent properly filtering pak and dlls based on true / false arg.
- Fixed icon not appearing in app.
- Resolved unrar permissions error
- Fixed drop down selection not saving on restart
- Fixed an issue where the DL2 profile was creating a Mods folder on install. 
- DL2 doesn't utilize a traditional mods folder so it cause the mods to become unreadable.
Added:
- Labels for source folder and unrar path are now buttons and will open their path.
- Uninstall mods button. (yes it has a warning)
- Toggle mods ON or OFF @ Launch (Utilizing SymLink.
     - You can read about this method here: https://learn.microsoft.com/en-us/windows/win32/fileio/symbolic-links)
- Update CZT will Open GitHub patch notes and discord invite.

---

## Version: 1.0.0

- Published: 2025-08-16
- Url: https://github.com/CaZual-T/CZT-Mod-Manager/releases/tag/1.0.0

Initial Release.

---

