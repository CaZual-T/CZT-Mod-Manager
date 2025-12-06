# Welcome to the CZT Mod Manager homepage!

~ Go to ["First Time Setup"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#czt-mod-manager-setup)</br>
~ Go to ["How to Use"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#how-to-use-czt-mod-manager)</br>
~ Go to ["Track Mods/Other Options"](https://github.com/CaZual-T/CZT-Mod-Manager?tab=readme-ov-file#how-to-track-modsupdate-info)</br>
~ Go to ["Function Definitions"](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#below-is-a-complete-function-dictionary)

# CZT Core:
- Built using Python and PyQt5 gui library; EXE compiling method = Nuitka Standalone.
- UnRAR: Supports extraction and management of compressed mod files of any compression type.

# Features:
- EZ Setup & Launch: Automatically locates or creates required configuration files, ensuring seamless setup for users.
- Steam Library Detection: Scans drives for Steam libraries to auto-detect game installations. (detects custom paths and names)
- Supports multi drive steam libraries. (any drive letter C-Z)
- Manual pathing available for EPIC and OTHER platforms. 
- Game Profiles: Handles multiple games. Custom settings built specifically for each game.
- EZ Management: Allows users to install, delete, and track mods, with precise user options.
- Toggle Mods: Launch with or without mods enabled.
- Disable mods individually & Restore at anytime.
- Nexus Mods Integration: Connects to the Nexus Mods API to collect mod info, and check versions for potential updates.
- "Available Updates" Notification @ Launch: Built-in check for CZT that allows the user to simply download and update CZT in app.
- Drag-and-Drop Support: Simplifies mod addition for users.
- Search bar to easily jump to any mod.
- Shift + left click mod name to edit the display name.
- CTRL+SHIFT+S will open detailed debug console.
- Sort mods A-Z/Z-A by mod display name.
- Sort mods A-Z/Z-A by mod creator name.
- Error Handling & Recovery: Stress tested for reliability.
- User Information: In-Depth user logs for both normal processes and errors.
- Merge Utility: Combine multiple .paks into one. (limited to dying light games)
- Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- Currently Supports 7DTD, Ready or Not, Schedule I, Dying Light 1/2, and Dying Light The Beast. More to be added!
- Does NOT support Linux.</br>

# Common errors w/ solutions:
Run CZT as ADMIN if you encounter the following errors:</br>
    - "[ERROR] No write permission to drive" </br>
    - "[ERROR] Permission denied: ':\\czt_write_test.tmp'."</br>
    - "[ERROR] A required privilege is not held by the client"</br>
    
Q: Why does czt need write permissions?</br>
A: This is so CZT can create required folders and properly edit the profile_mods_list.json (file that contains all your mod info)</br>

Q: Why does CZT need admin permissions when launching my game?</br>
A: Not all, but some users may need to launch their game with CZT as admin to ensure symlinking works correctly.</br>

"I cant drag and drop". </br>
    - Don't run CZT as admin when installing mods. </br>
    - Its IMPOSSIBLE for windows explorer to move files to an app with higher permissions. This is a windows limitation.</br>

# CZT Mod Manager Setup:
### - 1:) Download and Run installer
<img width="174" height="41" alt="{7EB16B48-08C8-4FFD-98D0-5B2268A55CE7}" src="https://github.com/user-attachments/assets/e7a5422c-d50a-44f9-9d7d-f1647d57bca0" />

### - 2:) Create Root
- Click the "Create Root" button in the top right of the CZT window.
- Select Drive, this will be where your mods are stored.
- All folders will be automatically created for you at the root of the drive you chose.
<img width="172" height="258" alt="{CEACEE52-38AD-4307-8A2E-CA00EBC285F2}" src="https://github.com/user-attachments/assets/03f0bbdc-daa5-4fe6-b535-e5c56ae5f3bb" />
<img width="354" height="189" alt="{FA7CDBF7-1A0F-4E39-9E60-466B44ADEF27}" src="https://github.com/user-attachments/assets/4a11cd57-1997-4a38-a651-f2d1d1b2e567" />


### - 3:) Install Unrar (click the Install Unrar button top right) (FOLLOW ON SCREEN PROMPTS)
- Click browse when the installer popup appears.
- YOU MUST INSTALL TO > Drive_selected_in_step_2/CZT Mod Manager/czt_tools/unrar.exe
- After installing UnRar, Click UnRar again to auto detect and set its path.
<img width="945" height="334" alt="{0E13B432-42D7-46FC-AE13-7CD7ABC503C4}" src="https://github.com/user-attachments/assets/656a078d-188a-4abd-a054-2ee030393657" />


### - 4:) Select Game profile
- Select an option from the drop down on the left.  (you can change this at any time)
- Click LOAD STEAM LIBRARIES at the bottom. (Alternatively you can use manual pathing and follow the instructions in the log box)
<img width="178" height="359" alt="{D4BEC0A2-DD47-4693-AD3C-936974E4EF7B}" src="https://github.com/user-attachments/assets/6ca83fb3-5ea6-4119-aa77-b4e9a920e6d1" />


### - 5:) Retrieve and save your NEXUS API key 
- Why? This is how CZT communicates with the nexus website to retrieve mod info.
- Go to <https://next.nexusmods.com/settings/api-keys>
- Scroll to the bottom to get your personal key.
<img width="1100" height="252" alt="{1AFC4493-C6F1-4FD9-A589-B7C0DC868802}" src="https://github.com/user-attachments/assets/482ae145-98f7-4e4c-b84d-9739c28e3627" />



# How to use CZT Mod Manager
### - 1:) Select Game Profile in the MAIN tab then...
- Go to the INSTALL tab
- Drag & Drop your mods to anywhere within app (.zip, .rar, .7z, or already extracted .pak)
- File based mods (.pak, .dll, .asi etc) do not need extracted before install.
- Folder mods need to be extracted first to avoid double foldering.
- Mods with a _mod_info.json file attached DO NOT need extracted before install, regardless of the type.
<img width="1106" height="237" alt="{9B9FD217-A798-4585-BA6E-BD871B32240D}" src="https://github.com/user-attachments/assets/d1945643-f2bb-40fc-a8e8-7bb83e80318d" />


> [!NOTE]
> Before continuing to the next step...</br>
> - Users with mods already installed...</br>
> - Go to your mod install location...</br>
>     ...drag and drop any mods you may have installed into the install tab. (to install later)</br>
> - Delete the old mod files/mod folder. You wont need them anymore.</br>

### - 2:) Select mods:
- Select mods to install.
<img width="379" height="157" alt="{B12E874C-4456-4379-AAEC-AA24F2A1A491}" src="https://github.com/user-attachments/assets/99b369d6-009f-4baa-8b6b-0f559ff5df37" />

- Click 'Install Selected'
<img width="647" height="81" alt="{4F1AE783-5E3F-4864-B202-51A2C0BEA97A}" src="https://github.com/user-attachments/assets/abf63bbc-a0b5-4bc0-8e97-7d2fa397e320" />

### - 3:) Launch Game:
- Go to the MAIN tab and then click the green launch button.
- You only have to launch with CZT when you want to toggle mods on or off or recently installed/deleted mods.
- Once mods are toggled on/off that is the state they will stay in until changed by the user.
>[!NOTE]
>- If you run into this error "A required privilege is not held by the client" when launching, try running the program as administrator. (Most users wont have to do this)</br>
>- THIS IS ONLY TO LAUNCH THE GAME. DRAG AND DROP WILL NOT WORK WHEN CZT IS RUNNING AS ADMIN. THIS IS A WINDOWS LIMITATION. EXPLORER CANNOT MOVE FILES TO AN APP WITH HIGHER PERMS THAN ITSELF.
<img width="1112" height="581" alt="{068958E5-CCE1-41EB-9C44-7750CF13E781}" src="https://github.com/user-attachments/assets/50f44dea-2d0d-4769-93e8-430089008b84" />

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


# Below is a complete function dictionary:
### Main Tab:
    [Left side buttons]
        > Source Folder: Opens main czt root folder.
        > Unrar Path: opens the unrar.exe path
        > Nexus Api Key: opens nexus website and takes user to api page.
        > {profile_select}: select which game you want to manage mods for.
    
    [Right side buttons]
        > Create Root: Creates main dependency folders for CZT
        > Install Unrar: Downloads and runs the official unrar installer.
        > Save Key: save nexus api key
        > Browse: open current profiles mod install and symlink locations.

    [Manual Path Options] (Greyed out unless the "Manual Pathing" option (below) is checked.)
        > Set Install: Set path to where mods should be linked to at launch.
        > Set EXE: Set path to the exe of the profile you selected.
        
    [Checkbox Options]
        > Manual Path: Used so the user can manually set exe and mod install locations.
        > Auto Path: Uses steam libraries to automatically detect and handle pathing for mods/games.
        
    [Main Logbox]
        > Logs (shows output of) all primary functions.

    [Bottom row buttons]
        > Join Discord: Opens official CZT discord
        > Open Github: Opens main github page.
        > Load Steam Libraries: Scan all installed drives for steams vdf file, parses that file, and uses the found library path(s) for other functions.
        > Save Config: Peace of mind manual save of all current settings.
        > Launch Game: Launch with or without mods. Uses symlink.

### Install Mods Tab:
    [Entire Window]
        > Ability to drag and drop mod zip, rar, 7z files into the window and stage them for install.
    
    [Bottom row buttons]
        > Select all.
        > Deselct all.
        > Patch DataN: Patches the number and mod info file if found so users dont have to manually.
        > Delete Selected.
        > Install Selected: Scans mod for potential manifest, if found, runs dedicated logic for manifest based installs. If not found, runs legacy install.
    
    [Checkbox]
        > Clear source folder after install: Will delete all selected mods AFTER they've been installed.
    
    [Install Log box]
        > Logs (shows output of) all install functions.

### Manage Mods Tab:
    [Top UI]
        > Search bar to jump to any mod.
        > 2 Sort options (By display name A-Z/Z-A) (By creator name A-Z/Z-A)
        > Heaader Labels.
    
    [Mod List Display (per row)]
        > Mod Name or File/Parent Folder Name (Shift + Left Click the mod name to edit the display name)
        > Mod cretors name.
        > Install Date. (date that you installed the mod)
        > Version installed (this will auto fill if the mod installed used a _mod_info.json file)
        > Mods newest version available. (select mod then click update scan for this to fill)
        > Nexus link (used to grab info like mod name, version, and thumbnail)
    
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
        > Force Install Date

### Settings Tab:
    [Startup Options]
        Set 'Install' as home tab - When CZT is launched, this tab display first.
        Set 'Manage' as home tab - When CZT is launched, this tab display first.
    
    [Color & Font Options]
    - You can reset these to default values at anytime.
        Custom Color selection (hexadecimal so literally any color is available)
        Custom font selection - 75+ Fonts available.\

<img width="1110" height="611" alt="{D43A4216-AB82-4B51-B745-D848072E72F3}" src="https://github.com/user-attachments/assets/5de0d36c-ac56-49dd-b5ab-ab89fd63ea92" />
<img width="1109" height="606" alt="{934FBFE6-E478-4798-B215-1F7DB3A20E0C}" src="https://github.com/user-attachments/assets/25d980be-bbdd-42b9-8991-a054bc4949db" />
<img width="1112" height="609" alt="{D666293E-2EF4-4D8A-BB21-0E262B9116BB}" src="https://github.com/user-attachments/assets/04b42cc7-43dd-48f3-ab4e-70fd4b22f66a" />
<img width="1110" height="608" alt="{B82D6E34-6F2A-4B66-8639-64E8E987FCAF}" src="https://github.com/user-attachments/assets/c41e00d3-f4be-4be2-9a84-be257080fdfc" />
