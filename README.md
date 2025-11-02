# Welcome to the CZT Mod Manager homepage!

~ Go to 'First Time Setup' : [CLICK TO TELEPORT](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#czt-mod-manager-setup)</br>
~ Go to 'How to Use' : [CLICK TO TELEPORT](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#how-to-use-czt-mod-manager)</br>
~ Go to 'Track Mods/Other Options' : [CLICK TO TELEPORT](https://github.com/CaZual-T/CZT-Mod-Manager?tab=readme-ov-file#how-to-track-modsupdate-info)

# CZT Core:
- Built using Python and PyQt5 gui library; EXE compiling method = Nuitka Standalone.
- Python: Core coding language. This app is 100% python.
- PyQt5: Provides a modern, customizable GUI for a more personal user experience.
- UnRAR: Supports extraction and management of compressed mod files of any compression type.

# Features:
- EZ Setup & Launch: Automatically locates or creates required configuration files, ensuring seamless setup for users.
- Steam Library Detection: Scans drives for Steam libraries to auto-detect game installations.
- Supports custom steam installs and folder names.
- Supports ANY drive letter, and multi drive libraries.
- Game Profile Support: Handles multiple game profiles, with custom settings and paths for each.
- Mod Installation & Management: Allows users to install, delete, and track mods, with precise user options.
- Toggle Mods: Launch with or without mods.
- Nexus Mods Integration: Connects to the Nexus Mods API for mod info, updates, and direct downloads.
- Customizable UI: Users can personalize colors, fonts, and layouts for accessibility and aesthetics.
- Update Checking: Built-in update checker for both the manager and mods, keeping everything current.
- Drag-and-Drop Support: Simplifies mod addition for users.
- Error Handling & Recovery: Stress tested for reliability.
- User Information: In-Depth user logs for both normal processes and errors.
- Merge Utility: Combine multiple .paks into one. (limited to dying light games)

- Currently Supports 7DTD, Ready or Not, Schedule I, Dying Light 1/2, and Dying Light The Beast. More to be added!
- Built for STEAM and WINDOWS. Does not support EPIC Games, Cracked version, or Linux.</br>
<img width="1113" height="608" alt="{42D27C9B-05C4-45CB-B295-BE1BAF747E4A}" src="https://github.com/user-attachments/assets/83d40d53-db60-4e23-a7b4-f5269172af6d" />


# CZT Mod Manager Setup:
~ Go to homepage : [CLICK TO TELEPORT](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#welcome-to-the-czt-mod-manager-homepage)</br>
### - 1:) Download and Run installer
<img width="174" height="41" alt="{7EB16B48-08C8-4FFD-98D0-5B2268A55CE7}" src="https://github.com/user-attachments/assets/e7a5422c-d50a-44f9-9d7d-f1647d57bca0" />

### - 2:) Create Root
- Click the "Create Root" button in the top right of the CZT window.
- Select Drive, this will be where your mods are stored.
- All folders will be automatically created for you at the root of the drive you chose.
<img width="172" height="258" alt="{CEACEE52-38AD-4307-8A2E-CA00EBC285F2}" src="https://github.com/user-attachments/assets/03f0bbdc-daa5-4fe6-b535-e5c56ae5f3bb" />

### - 3:) Install Unrar (click the button top right) (FOLLOW ON SCREEN PROMPTS)
- YOU MUST INSTALL TO > Drive_selected_in_step_2/CZT Mod Manager/czt_tools/unrar.exe
- After installing UnRar, Click UnRar again to auto detect and set its path.

### - 4:) Select Game profile
- Click LOAD STEAM LIBRARIES at the bottom.
- Then select the drop down on the left.  (you can change this at any time)
<img width="178" height="359" alt="{D4BEC0A2-DD47-4693-AD3C-936974E4EF7B}" src="https://github.com/user-attachments/assets/6ca83fb3-5ea6-4119-aa77-b4e9a920e6d1" />


### - 5:) Retrieve and save your NEXUS API key 
- Why? This is how CZT communicates with the nexus website to retrieve mod info.
- Go to <https://next.nexusmods.com/settings/api-keys>
- Scroll to the bottom to get your personal key.
<img width="1100" height="252" alt="{1AFC4493-C6F1-4FD9-A589-B7C0DC868802}" src="https://github.com/user-attachments/assets/482ae145-98f7-4e4c-b84d-9739c28e3627" />



# How to use CZT Mod Manager
~ Go to homepage : [CLICK TO TELEPORT](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#welcome-to-the-czt-mod-manager-homepage)</br>
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
> - Go to your mod install location,</br>
> drag and drop any mods you may have installed into the install tab. (to install later)</br>
> - Delete the old mod files/mod folder. You wont need them anymore.</br>

### - 2:) Select mods
- Select mods to install.
<img width="379" height="157" alt="{B12E874C-4456-4379-AAEC-AA24F2A1A491}" src="https://github.com/user-attachments/assets/99b369d6-009f-4baa-8b6b-0f559ff5df37" />

- Click 'Install Selected'
<img width="647" height="81" alt="{4F1AE783-5E3F-4864-B202-51A2C0BEA97A}" src="https://github.com/user-attachments/assets/abf63bbc-a0b5-4bc0-8e97-7d2fa397e320" />

### - 3:) Launch Game.
- Go to the MAIN tab and then click the green launch button.
- You only have to launch with CZT when you want to toggle mods on or off or recently installed/deleted mods.
- Once mods are toggled on/off that is the state they will stay in until changed by the user.
>[!NOTE]
>If you run into this error "A required privilege is not held by the client" when launching, try running the program as administrator. (Most users wont have to do this)
<img width="1112" height="581" alt="{068958E5-CCE1-41EB-9C44-7750CF13E781}" src="https://github.com/user-attachments/assets/50f44dea-2d0d-4769-93e8-430089008b84" />

# How To Track Mods/Update Info
~ Go to homepage : [CLICK TO TELEPORT](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main?tab=readme-ov-file#welcome-to-the-czt-mod-manager-homepage)</br>
- Go to the 'Manage' Tab.
- Enter the selected mods corresponding nexus url.
- Select checkbox next to mod, click save data button.
- To check for updates simply select the mod, click check for updates. This will also update the version number in the LATEST column.

# Other Features
### - Disabled/Restore Mods
- Select mods then click 'Disable Selected'
- You can click 'Restore Disabled' at anytime.
- Disabling mods results in them not being linked at launch. (good for trouble shooting broken mods)

### Forcible options
- These allow users to overwrite existing data within the profile_mod_list.json.
- Extremely useful for DataN.pak mods.
```
'Force Update Mod Image'
'Force Update Display Name'
'Force Update Local Version'
```
