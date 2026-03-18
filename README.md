# Features:
- ⭐ EZ Setup & Launch: Automatically locates or creates required configuration files.
     - If you have any problems just make your way to discord so i can help you.
- ⭐ Direct Downloads from nexus website (available only to nexus premium users. (nexus api restriction)
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
     - ↳ Merge button in manage tab is NOT the same logic as the UnleashTheMods plugin. It's 2 different things.
     - ↳ UTM plugin is more reliable imo.
- 🚫 Does NOT support Linux.</br>

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# Common errors w/ solutions:
### TO AVOID HAVING TO RESTART THE APP BETWEEN MAJOR FUNCTIONS. ENABLE DEVELOPER MODE.
- (Windows) Settings > Advanced > For Developers (Toggle Developer Mode On)
  - This allows symlinks and essential folders to be created without giving CZT admin permissions.
  - 99% of errors are solved by enabling this. Including the infamous [WinError 3]

### IF you chose to not enable developer mode, Run CZT as ADMIN if you encounter the following errors:
- "[ERROR] No write permission to drive"
- "[ERROR] Permission denied: ':\czt_write_test.tmp'."
- "[ERROR] A required privilege is not held by the client"

### "I cant drag and drop downloaded mods into CZT"
- That will happen when CZT is running as Admin.
   - Its IMPOSSIBLE for windows explorer to move files to an app with higher permissions. This is a windows limitation.﻿

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

# How to install mods:
> [!NOTE]
> [NEW USERS] Before continuing to the next step...</br>
> - First time users with mods already installed at default locations... </br>
> - ...Move them into your downloads folder. (NOT INCLUDING mod.io, do not touch mod.io folder) 
> - Delete the old mod files from the old default location. You wont need them anymore.</br>

- 1:) Select Game Profile in the MAIN tab then...
  - Download mods from nexus.
     - CZT will see the file in your downloads folder. (you can also drag files into the panel that's to the right of the log box)

- 2:) Select mods from the far right panel. Then click the top right arrow button. (you can install multiple mods at once as well)
  <img width="236" height="119" alt="image" src="https://github.com/user-attachments/assets/ea11206a-1f2e-4871-b506-f1da5375bbca" />

- 3:) Launch Game:
   - Click launch game in the main menu (left), or press CTRL+SHIFT+L.
     - [YES] will symlink mods that are currently enabled at the time of launch 
     - [NO] will remove all symlinks from the games directory. (fresh launch, no mods)
> [!TIP]
> - You only have to launch with CZT when you install new mods, or enable/disable mods using the toggle switches within CZT.
> - If your mod list hasn't changed, then you dont have to launch with CZT every single time you play.

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# Manage Mods tab basic controls:
### [Update Mod Info]
- Right click a mod, enter its nexus url or just the ID, click save.
   - <img width="305" height="39" alt="image" src="https://github.com/user-attachments/assets/e14ca7b2-0263-49a3-aaea-b6e223104a2e" />
   - <img width="255" height="103" alt="image" src="https://github.com/user-attachments/assets/b4bc0eb9-8c49-46ce-852a-faedda22dd86" />

### [Check Mods For Updates]
- click '🔄️' on the manager tab to scan all mods, or right click an entry and click "check for updates" at the bottom of the popup.

### [Disable/Restore Mods]
- Individual mod enable/disable toggle. 
- Toggle in the top right will enable/disable all mods at once.

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# Global Hotkeys
    [HOTKEY CONTROLS]
        > F2           : Open Load Order Menu.
        > F3           : Open Plugins Menu.
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
    - Example plugin ➡️ [here](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/profile_addon_plugin.py)
