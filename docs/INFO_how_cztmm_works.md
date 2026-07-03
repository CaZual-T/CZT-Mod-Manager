⬅️ [RETURN TO HOMEPAGE](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/README.md)

## Where does CZT store mods?
- All mods are stored within "{RootDriveSelectedAtSetup}:\CZT Mod Manager\czt_mod_data\installed_mods\{profile_name}"

## How does CZT know where to install mods?
### CZT Mod Manager utilizes multiple 'engines'</br>
<img width="275" height="256" alt="image" src="https://github.com/user-attachments/assets/05e5b8a1-6b3d-4a7e-a8cb-96b8c49249b6" /></br>
- These are the main components that drives installations, and linking for every profile.
- Seperate engines also allow me to update and maintain profiles efficiently without breaking the entire manager.

### Game Specific Info:
- All mods are installed the same way for every profile.
- After you download mods
LAUNCH WITH CZT FROM THE MAIN MENU TO INJECT MODS TO THE ACTIVE GAME PROFILE.</br>
or PRESS F7 TO PRELINK MODS AND THEN LAUNCH THROUGH STEAM/EXE.

- Ready or Not:
  - Content mods are the ones that go into Content/FMOD, MOVIES, SPLASH, VO_MOD
  - Pak files go into Content/PAKS/Mods/
    - Uninstall (F8/Safe Mode) removes the linked files from all content folders and any potential .dll/.asi mods from root (exe location)
    - Simple because all RoN mods are additions and never directly replace vanilla files.
- Forza Horizon 6:
  - Here we essentially take a snapshot of the vanilla files + some assistance from .ext filtering to recreate the vanilla structure 1:1.
  - Forza mods are then normalized to a mediapc/{scope} structure and "overlayed" (installed) into the game.
    - Automatically scope and fix improper mod structures upon install (mods missing mediapc/cars/ etc)
  - CZT also normalizes mods to mediapc to simply keep things cleaner.
    - Uninstall (F8/Safe Mode) reverts the game back to vanilla by utilizing the files we staged earlier.
    - This is a bit more complicated but its how managers like mo2 work from my understanding. 
- Schedule I:
  - The simplest out of all of them due to how it utilizes a traditional mods/plugins folder.
    - Uninstall (F8/Safe Mode) removes linked mods from the "mods/plugins" folder.
- Dying light (all):
  - Installs .pak files to source.
    - automatically detects conflicting pak names, and will rename at the users discretion.
    - .dll and .asi are handled accordingly and linked to the games exe.
      - Uninstall (F8/Safe Mode) simply removes the linked files from the source folder and any potential .dll/.asi mods from root (exe location)
     
🟢 Remember: this is just an explanation of how it works. All YOU have to do is press 1-2 buttons.
