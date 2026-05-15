# Features: 
- ⭐ EZ Setup & Launch: Automatically locates or creates required configuration files.
  - If you have any problems just make your way to discord so i can help you.
- ⭐ Handles .pak, .asi, .dll, FMOD (.bank), Splash (.png), Movies (.mp4), VO_MOD (folder/.ogg).
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
- 🚫 Does NOT support Linux.</br>

<img width="1254" height="620" alt="image" src="https://github.com/user-attachments/assets/9cdec0f9-ef4e-4bdd-b4d4-002eded6b397" />
<img width="1251" height="618" alt="image" src="https://github.com/user-attachments/assets/9f27b17f-87b6-41c5-ab70-6658c7a44bf3" />

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
    - Start with mods 
    - Start without mods 
    - Cancel, Do not launch
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
# Manage Mods tab - basic controls (left to right):
<img width="1094" height="39" alt="image" src="https://github.com/user-attachments/assets/620b4def-f476-4855-aa6a-e238f9c73092" />

| Action | Type | Description |
|---|---|---|
| [Search Bar] |<img width="256" height="37" alt="image" src="https://github.com/user-attachments/assets/6f463aa3-d375-4d83-aa8b-9a4a849a13f1" />|search using mod names, creators or categories to quickly filter mods. only mods that match what you type will be displayed|
| [Sort/Filter Menu] |<img width="100" height="34" alt="image" src="https://github.com/user-attachments/assets/837bf92a-8779-4dba-b997-864076895bdd" />| 17 total filters, select one to quickly sort your mods. |
| [Loadouts Menu] |<img width="96" height="31" alt="image" src="https://github.com/user-attachments/assets/55a0f581-202e-48a9-95f9-41ec4fc0778e" />| Here you can save, delete, merge, update, share and download loadouts. |
| [Select All] | ✅ | Select or Deselect all mods for bulk actions.
| [check for updates] | 🔄️ | checks all mods (enabled and disabled) for updates. |
| [Save as Loadout | 💾 | Enabled mods will be saved as a loadout | 
| [Create Backup] | ➕ | Create a backup of mod files + loadouts + profile mod list. |
| [Restore Backup] | 🛡️ | select a backup to restore |
| [Browse Nexus site] | 🔎 | Directly opens the nexus website for the profile currently enabled. |
| [Delete] | 🗑️ | delete selected mods |
| [List View] |<img width="38" height="35" alt="image" src="https://github.com/user-attachments/assets/92e0d713-c41a-42d7-8fc8-dbe84c067940" />|mods are listed vertically |
| [Grid View] |<img width="36" height="32" alt="image" src="https://github.com/user-attachments/assets/1a3a2381-9da9-4c10-ab2c-9b9a5c531bd8" />|mods are listed in a 2x5 sccrolable grid |
| [Hide Disabled] |<img width="121" height="34" alt="image" src="https://github.com/user-attachments/assets/75cb1d9a-8659-44cb-a799-793fd1444d23" />|disabled mods will be hidden from the main list. |
| [Bulk Toggle] |<img width="61" height="40" alt="image" src="https://github.com/user-attachments/assets/3ecbaea3-afcc-4804-a729-7f01ddca3afd" />|Enable/Disable all |
| [Update Mod Info] | RMB | Right click a mod to see in-depth mod info, or change the display name. |


#
# Global Hotkeys
    [HOTKEY CONTROLS]
    > F2           : Open Load Order Menu.
    > F3           : Open Plugins Menu.
    > F5           : Re-center main window on screen.
    > F9           : Detect missing mods from a saved loadout.
    > CTRL+O       : Open CZT root folder.
    > Shift+H      : Show hotkey options.
    > Shift+C      : Show current config.
    > Shift+R      : Show resource file paths.
    > Ctrl+Shift+L : Launch game.
    > Ctrl+Shift+S : Launch debug console.
#
# Plugins
- Place plugins in:
  - CZT Mod Manager/plugins/>here<
    - Press F3 to load. 
