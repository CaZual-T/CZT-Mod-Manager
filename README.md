# Features: 
- ⭐ EZ Setup & Launch: Automatically locates or creates required configuration files.
  - If you have any problems just make your way to discord so i can help you.
- ⭐ Handles .pak, .asi, .dll, FMOD (.bank), Splash (.png), Movies (.mp4), VO_MOD (.ogg).
- ⭐ Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- ⭐ Plug and play mod install by using the "Mod Manager Download" button on the nexus site to auto trigger CZT.
- ⭐ Direct (in-app) Downloads available for nexus premium users.
- ⭐ Detects when mods have Updates Available/Hidden Mod Page/Removed from Site and if they are corrupted.
- ⭐ Steam Library Detection: Scans drives for Steam libraries to auto-detect game installations.
  - Supports custom named and multi drive steam libraries. (any drive letter C-Z)
- ⭐ Manual pathing available for EPIC and OTHER platforms.
- ⭐ Users can easily download, install, toggle, track, and delete mods with precise user options.
- ⭐ Toggle Mods: Launch with or without mods enabled.
- ⭐ Set mod load order. (Press F2)
- ⭐ Disable mods individually & Restore at anytime.
- ⭐ Create, Share and Download custom profile loadouts.
- ⭐ Search bar and sort filters to easily navigate mods.
- ⭐ Error Handling & Recovery: Stress tested for reliability.
- ⭐ In-Depth user logs for both normal processes and errors.
- ⭐ Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- ⭐ Currently Supports Ready or Not, Schedule I, Dying Light 1/2, and Dying Light The Beast.
- 🟡 Merge Utility: Combine multiple .paks into one. (limited to dying light games)
  - ↳ Download the [UTM plugin](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/plugins/UnleashTheMods_plugin/UTM_plugin.rar). 
- 🚫 Does NOT support Linux.</br>
#
# Common errors w/ solutions:
### [WinError 3] Permission Denied at launch.
- ENABLE DEVELOPER MODE.
  - (Windows) Settings > Advanced > For Developers (Toggle Developer Mode On)
    - This allows symlinks and essential folders to be created without granting CZT admin permissions.

### IF you chose to not enable developer mode, Run CZT as ADMIN if you encounter the following errors:
- "[ERROR] No write permission to drive"
- "[ERROR] Permission denied: ':\czt_write_test.tmp'."
- "[ERROR] A required privilege is not held by the client"

### "I cant drag and drop downloaded mods into CZT"
- That will happen when CZT is running as Admin.
   - Its IMPOSSIBLE for windows explorer to move files to an app with higher permissions. This is a windows limitation.
     - That is also why CZT detect archive files in your downloads folders so you can skip the dnd and simply install.
    
### "A mod i have installed has an update available butCZT isnt flagging it"
  - This happens when creators upload a new version of a mod but didnt use/update the exisiting file.
    - When uploading to a mod page, users can choose to upload a new file, or update an existing one.
      - If they uploaded a new one instead of updating an existing one it breaks the file_id branch.
      - Theres no real fix for this other than to manually download from nexus, and hope the creator doesnt keep updating incorrectly.
      - I could make it compare against mod page version, or when a new file is uploaded, but that is messy and leads to false positives.
#
# Install/Setup Instructions:
>[!TIP]
>- Almost every ui element has a tooltip. Hover over buttons and drop downs etc to see them.
### 1:) Download and Run installer

### 2:) Create Root 
- Click 'SETUP' on the main menu.
  <img width="1112" height="155" alt="image" src="https://github.com/user-attachments/assets/3a8b9a2d-300d-465a-be20-2b72bbedb54b" />

- This popup will appear.
  <img width="841" height="161" alt="image" src="https://github.com/user-attachments/assets/77aeaa09-02cd-4f94-b34c-f350e6bc3dfb" />

  - Click create root.
    <img width="160" height="167" alt="image" src="https://github.com/user-attachments/assets/f08378bf-7d88-4615-9156-c9d860d37c7c" />

  - Select a Drive:</br>
    <img width="357" height="199" alt="image" src="https://github.com/user-attachments/assets/e7092185-1c80-4f53-94f0-82ae1dd5a78e" />

  - This is where your config and mod files will be stored. 'SelectedDrive:\CZT Mod Manager\' </br>

> [!NOTE]
> You WILL NOT be able to save any custom settings, loadouts or load orders until you create root.
> - Creating root is what generates the config.
> - Without the config you cannot save settings.
>   - Placing it at the root of the drive ensures my tool only has to peek into a drive one layer deep.
>   - This allows CZT to find the config on startup and load profiles significantly faster.
>   - Simple math, but there's always one...

### 3:) Install/Set Unrar 
- Click "Install Unrar"
  - Alternative: Download from: https://www.rarlab.com/rar/unrarw64.exe and place it in /CZT Mod Manager/czt_tools/unrar.exe
- Click browse when the installer popup appears.</br>
  - Install to > /CZT Mod Manager/czt_tools/unrar.exe</br>
    - Right now you have to do it this way.
    - I meant to set it up so you could set a path to winrar if you already had that installed,
    - but i guess i fuckered it all up so it only works if unrar is in the czt_tools folder.
- You can click 'Install UnRar' again to rescan and set its path automatically.
  - Or click set path (again it HAS to be to /CZT Mod Manager/czt_tools/unrar.exe)

### 4:) Retrieve and save your NEXUS API key
- Click the Nexus Api Key button or go to <https://next.nexusmods.com/settings/api-keys>
  <img width="822" height="47" alt="image" src="https://github.com/user-attachments/assets/b2175dc8-0950-448b-b3ab-3f93814171fc" />

- Scroll down to CZT Mod Manager a click 'Request API Key'.</br>
  - DO NOT USE YOUR PERSONAL KEY AT THE BOTTOM OF THE PAGE.
    <img width="652" height="205" alt="image" src="https://github.com/user-attachments/assets/aa364e24-e9eb-4c52-aabf-a018e954365d" />

### 5:) Select Game profile
- Select an option from the drop down on the left.  (you can change this at any time)
- Choose pathing mode (It's set to steam 'auto' by default)
- Click DETECT STEAM. (you should see someting like the image below)
  <img width="726" height="279" alt="image" src="https://github.com/user-attachments/assets/2bf4962a-a637-4f5d-93d4-7dcfdc581f9f" />

  - Alternatively you can use manual pathing and follow the instructions in the log box.
###
#
# How to install mods (NEW USER):
🟡 OPTION 1:
  - First time users with mods already installed at default locations... </br>
  - ...Move them into your downloads folder. (NOT INCLUDING mod.io, do not touch mod.io folder) 
  - Delete the old mod files from the old default location. You wont need them anymore.</br>
  - Select the profile (game) you want to use in CZT
  - Select all of your mods in the right panel (you can use the check mark to select all)
  - Click the top right arrow to install.
  - Go to the manage tab. Since these mods were manually installed by czt, they wont have their info saved.
  - You will have to manually right click each one and save their nexus url.</br>

 🟢 OPTION 2:
  - Delete all of your current mods.
  - Redownload using the steps below. 
#
# How to install new mods (normal):
1.) Download mods on the nexus site using the "Mod Manager Download" button.
  - If the mod manager download button is missing, download the [czt extension](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main/CZT_Extension) and use the manual download button.
    <img width="358" height="53" alt="image" src="https://github.com/user-attachments/assets/a8ebf771-2580-4554-97f2-9822576511bb" />

  - This will trigger CZT and the app will automatically handle install + saving mod info.
    <img width="577" height="203" alt="image" src="https://github.com/user-attachments/assets/af59b34a-9d04-41c7-9c8e-43cb5c425f07" />

2.) Launch Game:
  - Click launch game in the main menu (left), or press CTRL+SHIFT+L.
    <img width="376" height="180" alt="image" src="https://github.com/user-attachments/assets/4c0d48ba-02da-4b06-8bf5-a2d341dbd5c1" />

> [!NOTE]
> - You only have to launch with CZT when you install new mods, or enable/disable mods using the toggle switches within CZT.
> - If your mod list hasn't changed, then you dont have to launch with CZT every single time you play.
> - CZT supports drag and drop on the main menus far right panel. (unless running as admin, view faq at the top)
#
# Updating Mods
- Click the download arrow next to the mod in grid view.
  <img width="1068" height="55" alt="image" src="https://github.com/user-attachments/assets/6e922b50-1afa-43cd-bd0f-463e85ebfdb8" />

     - Premium Nexus accounts:
       - Instant direct download and install. 
         - You can enable auto update outdated mods in your settings as well.
     - Standard Nexus accounts:
       - Auto opens mod page on nexus.
       - When downloading mods that you already have installed, use the mod manger download button.
       - If the mod manger download button doesnt exist, get the czt extension and use the 'manual download' button.
         - Both methods will trigger CZT to run the install process and automatically apply updated metadata.   
#
# Manage Mods tab basic controls (left to right):
<img width="1094" height="39" alt="image" src="https://github.com/user-attachments/assets/620b4def-f476-4855-aa6a-e238f9c73092" />

### [Search Bar]

### [Sort/Filter Menu]
  - 17 total filters, select one to quickly sort your mods.

### [Loadouts Menu]
 - Loadout Manager:
  - Here you can save, delete, merge, update, share and download loadouts.

### [Select All] ✅
### [Scan all mods for updates] 🔄️
  - click '🔄️' to scan all mods, or right click an entry and click "check for updates" at the bottom of the popup.
### [Save mods that are currently enabled as a loadout] 💾
### [Create Backup] ➕
  - Files + list = Actual mod files + loadouts + profile mod list.
  - Files Only = Backup mod + loadout files
  - mod_list.json Only = Backup loadouts + profile mod list.

### [Restore Backup] 🛡️

### [Browse Nexus site] 🔎
  - Default: Directly opens the nexus website for the profile currently enabled.
    - Custom: enable the custom CZT browser in the setting under general to user the custom in-app browser.
      - Premium nexus account is recommended for the in-app browser feature.
### [Delete] 🗑️
### [List View] 
  - Clicking a mods image in list view will take you to a mods nexus page.
   <img width="1062" height="60" alt="image" src="https://github.com/user-attachments/assets/cb003a24-2dff-4304-bde5-fccbb8f881f9" />

### [Grid View]
  - Clicking the 🔗 icon will take you to a mods nexus page.

### [Hide Disabled]

### [Enable/Disable all mods toggle]

### [Update Mod Info] (legacy - still works as a fallback)
  - Right click a mod, enter its nexus url or just the ID, click save.
#
# Global Hotkeys
    [HOTKEY CONTROLS]
        > F2           : Open Load Order Menu.
        > F3           : Open Plugins Menu. (beta)
        > CTRL+O       : Open CZT root folder.
        > Shift+H      : Show hotkey options.
        > Shift+C      : Show current config.
        > Shift+R      : Show resource file paths.
        > Ctrl+Shift+L : Initiate a missile launch.
        > Ctrl+Shift+S : Launch debug console.
        > Ctrl+Alt+P   : Open paypal donation page.
#
# Plugins (Deprecated)
- Place plugins in:
  - CZT Mod Manager/plugins/exe_standalone/>here<
    - Press F3 to load. 
    - optional launch with admin prompt for plugins that may need it.
    - EXE plugins are not persistent and only launch when a user loads from the plugin menu.
  - CZT Mod Manager/plugins/scripts/>here<
    - Press F3 to load.
    - You can set scripts to persistently load at launch.
