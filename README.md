# Welcome to the CZT Mod Manager homepage!

~ Go to ["First Time Setup"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#czt-mod-manager-setup)</br>
~ Go to ["How to Use"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#how-to-use-czt-mod-manager)</br>
~ Go to ["Track Mods/Other Options"](https://github.com/CaZual-T/CZT-Mod-Manager?tab=readme-ov-file#how-to-track-modsupdate-info)</br>
~ Go to ["Function Definitions"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#below-is-a-complete-function-dictionary)</br>
~ Go to ["Troubleshooting"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#common-errors-w-solutions)

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
- Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- Currently Supports 7DTD, Ready or Not, Schedule I, Dying Light 1/2, and Dying Light The Beast. More to be added!
- Does NOT support Linux.</br>

# Common errors w/ solutions:

### TO AVOID HAVING TO RESTART THE APP BETWEEN MAJOR FUNCTIONS. ENABLE DEVELOPER MODE.
- (Windows) Settings > Advanced > For Developers (Toggle Developer Mode On)
- This allows symlinks to be created without admin permissions.</br>

IF you chose to not enable developer mode, Run CZT as ADMIN if you encounter the following errors:</br>
    - "[ERROR] No write permission to drive" </br>
    - "[ERROR] Permission denied: ':\\czt_write_test.tmp'."</br>
    - "[ERROR] A required privilege is not held by the client"</br>
    
Q: Why does czt need write permissions?</br>
A: This is so CZT can create required folders and properly edit the profile_mods_list.json (file that contains all your mod info)</br>

Q: Why does CZT need admin permissions when launching my game?</br>
A: Not all, but some users may need to launch their game with CZT as admin to ensure symlinking works correctly.</br>

"I cant drag and drop downloaded mods into the install tab". </br>
    - Don't run CZT as admin when installing mods. </br>
    - Its IMPOSSIBLE for windows explorer to move files to an app with higher permissions. This is a windows limitation.</br>

# CZT Mod Manager Setup:
### - 1:) Download and Run installer

### - 2:) Create Root 
- Go to the 'User Settings' Tab and click "Create Root".
- Select Drive, this will be where your mods are stored.
- All folders will be automatically created for you at the root of the drive you chose.</br>
NOTE: You wont be able to save any custom settings until you create root.
<img width="1111" height="221" alt="image" src="https://github.com/user-attachments/assets/0309d2f3-b9be-46d0-ba89-7069a135780c" />

### - 3:) Install Unrar (under create root button) (FOLLOW ON SCREEN PROMPTS)
- Click browse when the installer popup appears.
- YOU MUST INSTALL TO > Drive_selected_in_step_2/CZT Mod Manager/czt_tools/unrar.exe
- After installing UnRar, Click UnRar again to auto detect and set its path.
<img width="401" height="248" alt="image" src="https://github.com/user-attachments/assets/ee9f8b5f-5657-4bee-8d23-fb64ca512068" />

### - 4:) Retrieve and save your NEXUS API key 
- Why? This is how CZT communicates with the nexus website to retrieve mod info.
- Go to <https://next.nexusmods.com/settings/api-keys>
- Scroll to the bottom to get your personal key.
<img width="637" height="72" alt="image" src="https://github.com/user-attachments/assets/5ace9d82-339f-4d9c-8f50-05bb50117efe" />

### - 5:) Select Game profile
- Select an option from the drop down on the left.  (you can change this at any time)
- Click DETECT STEAM at the bottom. (Alternatively you can use manual pathing and follow the instructions in the log box)
<img width="507" height="112" alt="image" src="https://github.com/user-attachments/assets/87ff2e94-5d68-45c3-b7f4-3694ac6deca3" />

# How to use CZT to install mods
### - 1:) Select Game Profile in the MAIN tab then...
- Drag & Drop your mods to anywhere within the log box (.zip, .rar, .7z, or already extracted .pak)
- File based mods (.pak, .dll, .asi etc) do not need extracted before install.
- Folder mods need to be extracted first to avoid double foldering.
- Mods with a _mod_info.json file attached DO NOT need extracted before install, regardless of the type.

> [!NOTE]
> Before continuing to the next step...</br>
> - Users with mods already installed...</br>
> - Go to your mod install location...</br>
>     ...drag and drop any mods you may have installed into CZT. (to install later)</br>
> - Delete the old mod files. You wont need them anymore.</br>

### - 2:) Select mods:
- Select mods to install.
- Click ➡️ 'Install Selected'

### - 3:) Launch Game:
- Click the green launch button.
- You only have to launch with CZT when you want to toggle mods on or off or recently installed/deleted mods.
- Once mods are toggled on/off that is the state they will stay in until changed by the user.

# How To Track Mods/Update Info:
- Go to the 'Manage' Tab.
- Enter the selected mods corresponding nexus url.
- Select checkbox next to mod, click save data button.
- To check for updates simply select the mod, click check for updates. This will also update the version number in the LATEST column.

# Other Features:
### - Disabled/Restore Mods
- Select mods then click 'Disable Selected'
- You can click 'Restore Disabled' at anytime.
- Disabling mods results in them not being linked at launch. (good for trouble shooting broken mods)

### Forcible options:
- These allow users to overwrite existing data within the profile_mod_list.json.
- Extremely useful for DataN.pak mods.
```
'Force Update Mod Image'
'Force Update Display Name'
'Force Update Local Version'
'Force Update Install Date'
```

### Below is a complete function dictionary:
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


