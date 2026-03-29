# Features: 
- ⭐ EZ Setup & Launch: Automatically locates or creates required configuration files.
     - If you have any problems just make your way to discord so i can help you.
- ⭐ Plug and play mod install by using the "Mod Manager Download" button on the nexus site to auto trigger CZT.
- ⭐ Direct (in-app) Downloads from nexus website available for nexus premium users. (official nexus api restriction)
- ⭐ Detects when mods have Updates Available/Hidden Mod Page/Removed from Site and if they are corrupted.
- ⭐ Steam Library Detection: Scans drives for Steam libraries to auto-detect game installations. 
     - Supports custom named and multi drive steam libraries. (any drive letter C-Z)
- ⭐ Manual pathing available for EPIC and OTHER platforms.
- ⭐ Users can easily download, install, toggle, track, and delete mods with precise user options.
- ⭐ Toggle Mods: Launch with or without mods enabled.
- ⭐ Set mod load order. (Press F2)
- ⭐ Disable mods individually & Restore at anytime.
- ⭐ Create, Share and Download custom profile loadouts.
- ⭐ Connects to the Nexus Mods API to collect mod info, and check versions for potential updates.
- ⭐ CZT will show a popup when the manager itself has an available update.
- ⭐ Detect new mods in downloads folder. (drag and drop is also supported)
- ⭐ Shift + H will display all hotkeys in the main menu log box.
- ⭐ Search bar and sort filters to easily navigate mods.
- ⭐ Error Handling & Recovery: Stress tested for reliability.
- ⭐ In-Depth user logs for both normal processes and errors.
- ⭐ Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- ⭐ Currently Supports Ready or Not, Schedule I, Dying Light 1/2, and Dying Light The Beast.
- 🟡 Merge Utility: Combine multiple .paks into one. (limited to dying light games)
     - ↳ Download the [UTM plugin](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/UnleashTheMods-5.0_plugin/UTM_plugin.rar). 
- 🚫 Does NOT support Linux.</br>

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

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
     - That is also why CZT detect archive files in your downloads folders so you can skip the dnd and simply install.﻿

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

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
- Why? This is how CZT communicates with the nexus website to retrieve mod info.
- Go to <https://next.nexusmods.com/settings/api-keys>
- Scroll to the bottom to get your personal key.</br>
- CZT uses the api to simply fetch mod data such as thumbnail, creator name, mod name and current version.</br>
  - all of this gets displayed within the gui.</br>

### 5:) Select Game profile
- Select an option from the drop down on the left.  (you can change this at any time)
- Choose pathing mode (It's set to steam 'auto' by default)
- Click DETECT STEAM. (you should see someting like the image below)
<img width="726" height="279" alt="image" src="https://github.com/user-attachments/assets/2bf4962a-a637-4f5d-93d4-7dcfdc581f9f" />

  - Alternatively you can use manual pathing and follow the instructions in the log box.
###

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# How to install mods (NEW USER):
🟡 OPTION 1:
  - First time users with mods already installed at default locations... </br>
  - ...Move them into your downloads folder. (NOT INCLUDING mod.io, do not touch mod.io folder) 
  - Delete the old mod files from the old default location. You wont need them anymore.</br>
  - Select the profile (game) you want to use in CZT
  - Select all of your mods in the right panel (you can use the check mark to select all)
  - Click the top right arrow to install.
  - Go to the manage tab. Since these mods werent installed by czt, they wont have their info saved.
  - You will have to manually right click each one and save their nexus url.</br>

 🟢 OPTION 2:
  - Delete all of your current mods.
  - Redownload using the steps below. 

# How to install mods (normal):
1.) Download mods on the nexus site using the "Mod Manager Download" button.

<img width="358" height="53" alt="image" src="https://github.com/user-attachments/assets/a8ebf771-2580-4554-97f2-9822576511bb" />

   - This will automatically trigger CZT and the app will automatically handle install + saving mod info.
<img width="577" height="203" alt="image" src="https://github.com/user-attachments/assets/af59b34a-9d04-41c7-9c8e-43cb5c425f07" />

2.) Launch Game:
   - Click launch game in the main menu (left), or press CTRL+SHIFT+L.
     - [YES] will symlink mods that are currently enabled at the time of launch 
     - [NO] will remove all symlinks from the games directory. (fresh launch, no mods)
> [!NOTE]
> - You only have to launch with CZT when you install new mods, or enable/disable mods using the toggle switches within CZT.
> - If your mod list hasn't changed, then you dont have to launch with CZT every single time you play.
> - CZT supports drag and drop on the main menus far right panel.

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# Manage Mods tab basic controls (left to right):
<img width="1094" height="39" alt="image" src="https://github.com/user-attachments/assets/620b4def-f476-4855-aa6a-e238f9c73092" />

### [Search Bar]

### [Sort/Filter Menu]
  - 17 total filters, select one to quickly sort your mods.
  - <img width="203" height="394" alt="image" src="https://github.com/user-attachments/assets/919c151a-4e7b-47c0-9971-4c7d47ae89a8" />

### [Loadouts Menu]
-  <img width="189" height="228" alt="image" src="https://github.com/user-attachments/assets/6c474188-73b1-4f5d-81b7-8c7a793acdaa" />

    - Loadout Manager:
      - Here you can save, delete, merge, update, share and download loadouts.
      - <img width="781" height="480" alt="image" src="https://github.com/user-attachments/assets/34b8e1db-7556-4a37-8e24-86d945a283a2" />

### [Select All] ✅
### [Scan all mods for updates] 🔄️
  - click '🔄️' to scan all mods, or right click an entry and click "check for updates" at the bottom of the popup.
### [Save mods that are currently eneabled as loadout] 💾
### [Create Backup] ➕
  - <img width="761" height="127" alt="image" src="https://github.com/user-attachments/assets/52913edd-a9df-40e6-8f13-1e05027d7890" />

    - Files + list = Actual mod files + loadouts + profile mod list.
    - Files Only = Backup mod + loadout files
    - mod_list.json Only = Backup loadouts + profile mod list.

### [Restore Backup] 🛡️
  - <img width="758" height="452" alt="image" src="https://github.com/user-attachments/assets/52f2c021-53a2-4206-a81e-e1076f842b4c" />

 
### [Browse Nexus site] 🔎
  - Default: Directly opens the nexus website for the profile currently enabled.
    - Custom: enable the custom CZT browser in the setting under general to user the custom in-app browser.
      - Premium nexus account is recommended for the in-app browser feature.
### [Delete] 🗑️
### [List View] 
  - Clicking a mods image in list view will take you to a mods nexus page.
  - <img width="1062" height="60" alt="image" src="https://github.com/user-attachments/assets/cb003a24-2dff-4304-bde5-fccbb8f881f9" />

### [Grid View]
  - Clicking the 🔗 icon will take you to a mods nexus page.
  - <img width="1038" height="196" alt="image" src="https://github.com/user-attachments/assets/3dedcebd-3be7-4792-9452-e59b77cccaf9" />

### [Hide Disabled]
  - <img width="114" height="34" alt="image" src="https://github.com/user-attachments/assets/5ee5e268-6081-4d83-857b-13e78bf8ea72" />

### [Enable/Disable all mods toggle]
  - <img width="49" height="40" alt="image" src="https://github.com/user-attachments/assets/ea499028-242a-4bb2-807b-c42ccb6ecb28" />

### [Update Mod Info] (legacy - still works as a fallback)
  - Right click a mod, enter its nexus url or just the ID, click save.
    - <img width="305" height="39" alt="image" src="https://github.com/user-attachments/assets/e14ca7b2-0263-49a3-aaea-b6e223104a2e" />
    - <img width="255" height="103" alt="image" src="https://github.com/user-attachments/assets/b4bc0eb9-8c49-46ce-852a-faedda22dd86" />

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

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
        

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# Plugins (BETA)
- Place plugins in:
  - CZT Mod Manager/plugins/exe_standalone
    - Press F3 to load. 
    - optional launch with admin prompt for plugins that may need it.
    - EXE plugins are not persistent and only launch when a user loads from the plugin menu.
  - CZT Mod Manager/plugins/scripts
    - Press F3 to load.
    - You can set scripts to persistently load at launch.
