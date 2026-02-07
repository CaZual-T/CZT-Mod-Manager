> [!NOTE]
> README IS UPDATED FOR V3. IF YOU'RE ON AN OLDER VERSION THEN THIS WONT TRANSLATE.

# CZT Core:
- Built using Python and Pyside6 gui library; EXE compiling method = Nuitka Standalone.
- UnRAR: Supports extraction and management of compressed mod files of any compression type.
<img width="1112" height="613" alt="image" src="https://github.com/user-attachments/assets/88c2651d-10c6-4c06-a7d1-be2cd1cb6a4c" />
<img width="1110" height="614" alt="image" src="https://github.com/user-attachments/assets/39a0e5e6-b557-46a3-a7a6-2fa6d3651521" />


# Features:
- EZ Setup & Launch: Automatically locates or creates required configuration files, ensuring seamless setup for users.
- ⭐ Steam Library Detection: Scans drives for Steam libraries to auto-detect game installations. (detects custom paths and names)
- ⭐ Supports multi drive steam libraries. (any drive letter C-Z)
- ⭐ Manual pathing available for EPIC and OTHER platforms. 
- Game Profiles: Handles multiple games. Custom settings built specifically for each game.
- EZ Management: Allows users to install, delete, and track mods, with precise user options.
- ⭐ Toggle Mods: Launch with or without mods enabled.
- ⭐ Set mod load order. (Press F2)
- ⭐ Script & EXE plugin support. (Press F3 for plugin manager)
- ⭐ Disable mods individually & Restore at anytime.
- Nexus Mods Integration: Connects to the Nexus Mods API to collect mod info, and check versions for potential updates.
- "Available Updates" Notification @ Launch: Built-in check for CZT that allows the user to simply download and update CZT in app.
- Drag-and-Drop Support: Simplifies mod addition for users.
- CTRL+SHIFT+S will open detailed debug console.
- Shift + H will display all hotkeys.
- Search bar to easily filter mods.
- Many sort filters.
- Error Handling & Recovery: Stress tested for reliability.
- In-Depth user logs for both normal processes and errors.
- Merge Utility: Combine multiple .paks into one. (limited to dying light games)
  - ↳ Merge button in manage tab is NOT the same logic as the UnleashTheMods plugin. It's 2 different things.
  - ↳ UTM plugin is more reliable imo.  
- Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- Currently Supports 7DTD, Ready or Not, Schedule I, Dying Light 1/2, and Dying Light The Beast. More to be added!
- Does NOT support Linux.</br>

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# Install/Setup Instructions:
>[!TIP]
>- Almost every ui element has a tooltip. Hover over buttons and drop downs etc to see them.
### 1:) Download and Run installer

### 2:) Create Root 
- Click 'SETUP' on the main menu.
  - Click create root.
  - Select a Drive:</br>
  - This is where your config and mod files will be stored.</br>
> [!NOTE]
> You wont be able to save any custom settings until you create root.

### 3:) Install/Set Unrar 
- Click "Install Unrar"
- Click browse when the installer popup appears.</br>
  - Install to > /CZT Mod Manager/czt_tools/unrar.exe</br>
- You can click 'Install UnRar' again to rescan and set its path automatically.

### 4:) Retrieve and save your NEXUS API key 
- Why? This is how CZT communicates with the nexus website to retrieve mod info.
- Go to <https://next.nexusmods.com/settings/api-keys>
- Scroll to the bottom to get your personal key.</br>
- CZT uses the api to simply fetch mod data such as thumbnail, creator name, mod name and current version.</br>
  - all of this gets displayed within the gui.</br>

### 5:) Select Game profile
- Select an option from the drop down on the left.  (you can change this at any time)
- Choose pathing mode (It's set to steam 'auto' by default)
- Click DETECT STEAM.
  - Alternatively you can use manual pathing and follow the instructions in the log box.
###

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# How to install mods:
### 1:) Select Game Profile in the MAIN tab then...
- Drag & Drop your mods to anywhere within the log box on the Main Menu tab. (.zip, .rar, .7z, or Raw Files/Folders)
  - Most mods do not need extracted before install. (CZT handles extraction)
    - Extract folder based mods to desktop and drag the raw folder into CZT if you experience double foldering issues.
  - Mods with a _mod_info.json file attached will automatically have their mod info updated in the manage tab.
    - Image, Mod Name, Creator, Install Date, Version, Nexus URL (ID)

> [!NOTE]
> [NEW USERS] Before continuing to the next step...</br>
> - First time users with mods already installed at default locations...</br>
> - Go to your mod install location...</br>
>     ...drag and drop any mods you may have into the log box of CZT. (to install later)</br>
> - Delete the old mod files from the old default location. You wont need them anymore.</br>

### 2:) Select mods:
- Select mods to install.
- Click the arrow in the top right to install selected mods.

### 3:) Launch Game:
- Click launch game in the main menu (or) press CTRL+SHIFT+L 
- You only have to launch with CZT when you want to toggle mods on or off or recently installed/deleted mods.
- Once mods are toggled on/off that is the state they will stay in until changed by the user.

# How To Use Manager Controls:
### [Update Mod Info]
- Right click mod, enter its url or just the ID, click save.

### [Check Mods For Updates]
- click '🔄️' to scall all mods or right click an entry and individually scan.

### [Disable/Restore Mods]
- Utilize the toggle in the top right to enable/disable all mods at once. 

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

# Common errors w/ solutions:
### TO AVOID HAVING TO RESTART THE APP BETWEEN MAJOR FUNCTIONS. ENABLE DEVELOPER MODE.
- (Windows) Settings > Advanced > For Developers (Toggle Developer Mode On)
  - This allows symlinks to be created without admin permissions.
  - 99% of errors are solved by enabling this.

### IF you chose to not enable developer mode, Run CZT as ADMIN if you encounter the following errors:
- "[ERROR] No write permission to drive"
- "[ERROR] Permission denied: ':\czt_write_test.tmp'."
- "[ERROR] A required privilege is not held by the client"

### Q: Why does czt need write permissions?
A: This is so CZT can create required folders and properly edit the profile_mods_list.json (file that contains all your mod info)

### Q: Why does CZT need admin permissions when launching my game?
A: Not all, but some users may need to launch their game with CZT as admin to ensure symlinking works correctly.

### "I cant drag and drop downloaded mods into CZT"
- Don't run CZT as admin when installing mods.
- Its IMPOSSIBLE for windows explorer to move files to an app with higher permissions. This is a windows limitation.﻿

- If you are already in the manage tab at the time of merge you will not see data7 until you reload the ui.mod list. </br>
  - You can do this by simply switching to any other tab then going back to the manage tab.
