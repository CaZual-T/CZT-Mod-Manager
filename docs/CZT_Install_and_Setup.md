Video Guide (it's not great, but provides a visual for the guide below): https://youtu.be/0D4QZrE7Cws
- I HIGHLY suggest actually reading the guide below.
  
# Install/Setup Instructions: 
Latest Release: https://github.com/CaZual-T/CZT-Mod-Manager/releases

### 1:) Install CZT Mod Manager
- Run Installer</br>
  <img width="591" height="460" alt="image" src="https://github.com/user-attachments/assets/59bf3727-a474-456c-8387-9dd7aadf4eb8" />
  <img width="592" height="459" alt="image" src="https://github.com/user-attachments/assets/8226a656-4a15-47a4-baa5-5ff635b5c30a" />
  <img width="595" height="458" alt="image" src="https://github.com/user-attachments/assets/70a9e31b-33f9-4b62-b84b-7b243713de8f" />
##
>[!TIP]
>- Almost every ui element has a tooltip. Hover over buttons and drop downs etc to see them.

### 2:) Create Root 
- Click 'SETUP' on the main menu.
  <img width="1112" height="155" alt="image" src="https://github.com/user-attachments/assets/3a8b9a2d-300d-465a-be20-2b72bbedb54b" />

- This popup will appear.
  <img width="841" height="161" alt="image" src="https://github.com/user-attachments/assets/77aeaa09-02cd-4f94-b34c-f350e6bc3dfb" />

  - Click create root.</br>
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
  - Install to > DriveThatYouChoseForRootFolder:/CZT Mod Manager/czt_tools/unrar.exe</br>
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
- Select an option from the drop down on the left.  (you can change this at any time)</br>
  <img width="165" height="216" alt="image" src="https://github.com/user-attachments/assets/f0df65c9-2035-44c1-83bd-bdca5edcc608" />

### 6:) Set Path Mode:
### 🔵 STEAM </br>
- Ensure the path mode is set to **Steam** (should be by default).</br>
<img width="168" height="91" alt="image" src="https://github.com/user-attachments/assets/ba250395-74f6-4114-89e9-ef28d774841e" /></br>
  - Click DETECT STEAM.</br>
  <img width="174" height="123" alt="image" src="https://github.com/user-attachments/assets/9971edd9-8921-4fe8-a52b-17b492d583b5" /></br>
    - This will check your steam .vdf file for every game CZT manages and automatically set applicable paths.</br>
    <img width="726" height="279" alt="image" src="https://github.com/user-attachments/assets/2bf4962a-a637-4f5d-93d4-7dcfdc581f9f" /></br>

### 🟡 XBOX, Epic Games, 'Other' </br>
- Click "Path Modes"
  - Select "Manual"</br>
<img width="171" height="93" alt="image" src="https://github.com/user-attachments/assets/90e50273-8253-4a9c-9513-81dd73d5c92a" /></br>
<img width="641" height="423" alt="image" src="https://github.com/user-attachments/assets/415dbaf3-03fd-46c7-a91d-18b400b700d0" /></br>
  - 🔴 FORZA HORIZON 6 'XBOX/GAMEPASS' USERS ⚠️ [--> CLICK HERE <--](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/GUIDE_xbox_forzahorizon6.md) ⚠️</br>

### Once your paths are set you're ready to start downloading and installing mods!
- Read the "how to install/update mods" guide below!
##
🆘 Click [HERE](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/GUIDE_install-update_mods.md) for a guide on how to install/update mods.</br>
🆘 Click [HERE](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/FAQ-HELP.md) for FAQ.</br>
