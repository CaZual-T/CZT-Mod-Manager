# Welcome to the CZT Mod Manager homepage! 
~ Go to ["First Time Setup"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#czt-mod-manager-setup)</br>
~ Go to ["How to Use"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#how-to-use-czt-mod-manager)</br>
~ Go to ["Track Mods/Other Options"](https://github.com/CaZual-T/CZT-Mod-Manager?tab=readme-ov-file#how-to-track-modsupdate-info)</br>
~ Go to ["Plugins BETA"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#plugins-beta)</br>
~ Go to ["All Controls"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#below-is-a-complete-function-dictionary)</br>
~ Go to ["Troubleshooting"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#common-errors-w-solutions)</br>

# CZT Core:
- Built using Python and PyQt5 gui library; EXE compiling method = Nuitka Standalone.
- UnRAR: Supports extraction and management of compressed mod files of any compression type.

# Features:
- EZ Setup & Launch: Automatically locates or creates required configuration files, ensuring seamless setup for users.
- ⭐ Steam Library Detection: Scans drives for Steam libraries to auto-detect game installations. (detects custom paths and names)
- ⭐ Supports multi drive steam libraries. (any drive letter C-Z)
- ⭐ Manual pathing available for EPIC and OTHER platforms. 
- Game Profiles: Handles multiple games. Custom settings built specifically for each game.
- EZ Management: Allows users to install, delete, and track mods, with precise user options.
- ⭐ Toggle Mods: Launch with or without mods enabled.
- ⭐ Set mod load order. (Press F2)
- ⭐ Disable mods individually & Restore at anytime.
- Nexus Mods Integration: Connects to the Nexus Mods API to collect mod info, and check versions for potential updates.
- "Available Updates" Notification @ Launch: Built-in check for CZT that allows the user to simply download and update CZT in app.
- Drag-and-Drop Support: Simplifies mod addition for users.
- Shift + left click mod name to edit the display name.
- CTRL+SHIFT+S will open detailed debug console.
- Shift + H will display all hotkeys.
- Search bar to easily filter mods.
- Sort mods A-Z/Z-A by mod display name.
- Sort mods A-Z/Z-A by mod creator name.
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
### 1:) Download and Run installer

### 2:) Create Root 
- Go to the 'User Settings' Tab and click "Create Root".
  - Select a Drive:</br>
  - This is where your config and mod files will be stored.</br>
> [!NOTE]
> You wont be able to save any custom settings until you create root.
<img width="1111" height="221" alt="image" src="https://github.com/user-attachments/assets/0309d2f3-b9be-46d0-ba89-7069a135780c" />

### 3:) Install Unrar 
- Go to the 'User Settings' Tab and click "Install Unrar"
- Click browse when the installer popup appears.</br>
    <img width="520" height="390" alt="image" src="https://github.com/user-attachments/assets/51d1ffec-1d01-4665-963b-f55279ffcdce" /></br>

- YOU MUST INSTALL TO > /CZT Mod Manager/czt_tools/unrar.exe</br>
    <img width="401" height="248" alt="image" src="https://github.com/user-attachments/assets/ee9f8b5f-5657-4bee-8d23-fb64ca512068" /></br>
- You can click 'Install UnRar' again to rescan and set its path. (it should automatically set after install though)

### 4:) Retrieve and save your NEXUS API key 
- Why? This is how CZT communicates with the nexus website to retrieve mod info.
- Go to <https://next.nexusmods.com/settings/api-keys>
- Scroll to the bottom to get your personal key.</br>
- CZT uses the api to simply fetch mod data such as thumbnail, creator name, mod name and current version.</br>
  - all of this gets displayed within the gui.</br>

### 5:) Select Game profile
- Select an option from the drop down on the left.  (you can change this at any time)
- Choose pathing mode (It's set to steam 'auto' by default)
- Click DETECT STEAM at the bottom.
  - Alternatively you can use manual pathing and follow the instructions in the log box.
###
<img width="507" height="112" alt="image" src="https://github.com/user-attachments/assets/87ff2e94-5d68-45c3-b7f4-3694ac6deca3" /></br>

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# How to install mods:
### 1:) Select Game Profile in the MAIN tab then...
- Drag & Drop your mods to anywhere within the log box (.zip, .rar, .7z, or already extracted .pak)
  - File based mods (.pak, .dll, .asi etc) do not need extracted before install.
  - Folder mods need to be extracted first to avoid double foldering.
  - Mods with a _mod_info.json file attached DO NOT need extracted before install, regardless of the type.

> [!NOTE]
> [NEW USERS] Before continuing to the next step...</br>
> - First time users with mods already installed at default locations...</br>
> - Go to your mod install location...</br>
>     ...drag and drop any mods you may have, into CZT. (to install later)</br>
> - Delete the old mod files from the old default location. You wont need them anymore.</br>

### 2:) Select mods:
- Select mods to install.
- Click '➡️' to install selected mods.
<img width="328" height="110" alt="image" src="https://github.com/user-attachments/assets/ff2db525-90e5-4001-8455-e47711a319a0" />

### 3:) Launch Game:
- Click the green launch button in the main menu (or) press CTRL+SHIFT+L 
- You only have to launch with CZT when you want to toggle mods on or off or recently installed/deleted mods.
- Once mods are toggled on/off that is the state they will stay in until changed by the user.

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# How To Use Manager Controls:
### - Update Mod Info
- 1.) Go to the 'Manage' Tab.
- 2.) Enter the selected mods corresponding nexus full url (or just the id). <img width="79" height="29" alt="image" src="https://github.com/user-attachments/assets/7a189cef-bd94-4492-9ed7-464f7dc9175b" />
- 3.) Ensure checkbox next to the mod you entered the url for is checked. <img width="180" height="22" alt="image" src="https://github.com/user-attachments/assets/6670f70a-7437-4ebd-904f-839c78872dfe" />
- 4.) Click save data button. <img width="120" height="35" alt="image" src="https://github.com/user-attachments/assets/f0e0a2b7-e69d-4d37-b295-a8d9bb5ad8e8" />
- RESULT:
<img width="974" height="73" alt="image" src="https://github.com/user-attachments/assets/3878382b-af1c-42f5-85a4-341f46570e70" />


### [Check Mods For Updates]
- Select as many mods as you want.
- click '🔄️ Scan'
  - This will also update the version number in the LATEST column.
>[!TIP]
> - You can select and scan all of your mods for updates at once if you choose.
>   - This may take a few minutes depending on total mod count and internet connection. 

### [Disable/Restore Mods]
- Select mods then click 'Disable Selected'
- You can click 'Restore Disabled' at anytime.
- Disabling mods results in them not being linked at launch. (good for trouble shooting broken mods)

### [Forcible options]
- These options allow users to overwrite existing data within the profile_mod_list.json when 'Save Data' is clicked.
- Extremely useful for DataN.pak mods.
```
'Force Update Mod Image'
'Force Update Display Name'
'Force Update Local Version'
'Force Update Install Date'
```

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
<img width="501" height="226" alt="image" src="https://github.com/user-attachments/assets/43cdf134-1c7b-4403-a42f-3c68c8bd2c16" />

<img width="1920" height="100" alt="Untitled (2)" src="https://github.com/user-attachments/assets/cab67cc2-30e9-4fc8-8b10-beb2f904f485" />

# All Controls:
### Global Hotkeys
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
        
### Main Tab:
    [Left side buttons]
        > {profile_select}: select which game you want to manage mods for.
        > Select Path Mode
        > Set Install & Exe (For Manual Pathing)
    [Right side buttons]
        > Select all.
        > Deselct all.
        > Delete Selected.
        > Patch DataN: Patches the number and mod info file if found so users dont have to manually.
        > Install Selected: Scans mod for potential manifest, if found, runs dedicated logic for manifest based installs. If not found, runs legacy install.
    [Main Logbox]
        > Logs (shows output of) all primary functions.
    [Bottom row buttons]
        > Join Discord: Opens official CZT discord
        > Open Github: Opens main github page.
        > Detect Steam: Scan all installed drives for steams vdf file, parses that file, and uses the found library path(s) for other functions.
        > Save Config: Peace of mind manual save of all current settings.
        > Launch Game: Launch with or without mods. Uses symlink.
<img width="1112" height="610" alt="image" src="https://github.com/user-attachments/assets/cb2af00c-ecf1-4dd6-a42d-56ed401d86a3" />

### Manage Mods Tab:
    [Top Row Labels]
        > {current game} | Installed Mods
        > Local Version: Most recent version installed.
        > Latest: Newest version available on nexus.
        > Nexus Link: Entry for each mods nexus link. (used to grab info like mod name, version, and thumbnail)
    [Mod List Display (per row)]
        > Mod Name or File Name (this will auto fill if the mod installed used a _mod_info.json file)
        > Creator Name (this will auto fill if the mod installed used a _mod_info.json file)
        > Install Date
        > Version installed (this will auto fill if the mod installed used a _mod_info.json file)
        > Mods newest version available
        > Nexus link
    [Controls (Sort & Search)]
        > Search Bar for easy filtering
        > Sort by Creator Name A-Z (Right Arrow)
        > Sort by Mod Name A-Z (Left Arrow)
    [Controls (buttons)]
        > Select All
        > Deselect All
        > Select Outdated (use this after running 'Update Scan')
        > Open Selected: Opens the webpage of each selected mod.
        > Update Scan: Compares the selected mods saved info within mod_list.json to the available metadata on the nexus site.
        > Merge Mods: Line by line merging for DataN.pak mods in Dying Light Games. Easy and Advanced options.
        > Disable Selected: Moves selected mods to a quarantined folder to prevent them from loading at launch. Great for troubleshooting problematic mods.
        > Restore Disabled: Individually select which mods you want to re-enable.
        > Delete Selected: There is a yes no confirmation before the action completes. THIS CANNOT BE UNDONE.
        > Save Data: Saves the data of SELECTED MODS. YOU MUST SELECT THE MOD THEN CLICK THIS BUTTON. OTHERWISE IT DOESNT SAVE.
    [Checkboxes]
        - I added these to ensure DataN.pak mods could easily be overwritten within the mod_list.json at the users discretion.
        - CZT uses a mod list to display mod info. Due to the naming of dataN.pak mods this can cause mixed info to be displayed. 
        - These settings ensure you can easily overwrite them to prevent them from displaying the wrong info. Just ensure the link is correct for the mod you installed.
        > Force Update Image
        > Force Update Display Name
        > Force Update Local Version
<img width="1111" height="609" alt="image" src="https://github.com/user-attachments/assets/bc87b0b3-e137-46de-854b-7a0c8c65f975" />

### User Settings Tab
    [Setup Options]
        > Source Folder: Opens main czt root folder.
        > Unrar Path: opens the unrar.exe path
        > Nexus Api Key: opens nexus website and takes user to api page.
    [Startup Options]
        > Set 'Install' as home tab - When CZT is launched, this tab display first.
        Set 'Manage' as home tab - When CZT is launched, this tab display first.
    [Audio Options]
        > Select Track
        > Volume (menu music/track)
        > Enable/Disable checkboxes for Menu Music, Button Hover/Click sound effects.
    [Color & Font Options]
    - You can reset these to default values at anytime.
        > Custom Color selection (hexadecimal so literally any color is available)
        > Custom font selection - 75+ Fonts available
<img width="1110" height="607" alt="image" src="https://github.com/user-attachments/assets/41cb57a5-394e-4065-9500-6e0bc698f503" />

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

### [ERROR] Permission denied: [WinError 3]
- press ctrl + o , open the config file.
- find resolved_profile_paths, resolved_exe_paths, and set_profile_path and delete their blocks/lines.
- Then press 'detect steam' (or set your paths again manually for other install types)>
- Launch Game.
```
  "resolved_profile_paths": {
     "Ready or Not": "D:\\Program Files (x86)\\Steam\\steamapps\\common\\Ready or Not\\ReadyOrNot\\Content\\Paks\\Mods"
      },
  "resolved_exe_paths": {
     "Ready or Not": "D:\\Program Files (x86)\\Steam\\steamapps\\common\\Ready or Not\\ReadyOrNot.exe"
      },

  "set_profile_path": "D:\\Program Files (x86)\\Steam\\steamapps\\common\\Ready or Not\\ReadyOrNot\\Content\\Paks\\Mods"
```


