⬅️ [RETURN TO HOMEPAGE](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/README.md)

## Where does CZT store mods?
- All mods are stored within "{RootDriveSelectedAtSetup}:\CZT Mod Manager\czt_mod_data\installed_mods\{profile_name}"
- Enabled mods are then 'linked' to the active profile when you press F7 or 'Launch Game' --> 'Link | Modded'

## How does CZT know where to install mods?
### CZT Mod Manager utilizes multiple 'engines'</br>
<img width="122" height="129" alt="image" src="https://github.com/user-attachments/assets/333bf9f7-abdb-4023-8085-fd2695513345" /></br>
- These are the main components that drives installations, and linking for every profile.
- Seperate engines also allow me to update and maintain profiles efficiently without breaking the entire manager.

### Game Specific Info:
- All mods are installed the same way for every profile.
- After you download mods
LAUNCH WITH CZT FROM THE MAIN MENU TO INJECT MODS TO THE ACTIVE GAME PROFILE.</br>
or PRESS F7 TO PRELINK MODS AND THEN LAUNCH THROUGH STEAM/EXE.

- Ready or Not (UE5):
  - Content mods are the ones that go into Content/FMOD, MOVIES, SPLASH, VO_MOD
  - Pak files go into Content/PAKS/Mods/
    - Uninstall (F8/Safe Mode) removes the linked files from all content folders and any potential .dll/.asi mods from root (exe location)
    - Simple because all RoN mods are additional files within a mods folder.
    - Content mods FMOD, MOVIES, SPLASH, VO_MOD never directly replace vanilla files and a backup is automatically made when mods are linked. Making it easy to go back to vanilla files.
- Forza Horizon 6 (ForzaTech):
  - Here we essentially take a snapshot of the vanilla files + some assistance from .ext filtering to recreate the vanilla structure 1:1.
  - Forza mods are then normalized to a mediapc/{scope} structure and "overlayed" (installed) into the game.
    - Automatically scope and fix improper mod structures upon install (mods missing mediapc/cars/ etc)
  - CZT also normalizes mods to mediapc to simply keep things cleaner.
    - Uninstall (F8/Safe Mode) reverts the game back to vanilla by utilizing the files we staged earlier.
    - This is a bit more complicated but its how managers like mo2 work from my understanding. 
- Schedule I (Unity):
  - The simplest out of all of them due to how it utilizes a traditional mods/plugins folder.
    - F7 / Launch Game --> 'Modded' to symlink enabled mods to their "mods/plugins" folder.
    - F8 / Launch Game --> 'Safe Mode' to remove symlinks.
- Dying light (Techland C-Engine):
  - Installs .pak files to source.
    - automatically detects conflicting pak names, and will rename at the users discretion.
    - .dll and .asi are handled accordingly and linked to the games exe.
      - F7 / Launch Game --> 'Modded' to symlink enabled mods to the "source" folder. Any .dll/.asi loaders go to the game root (exe location)
      - F8 / Launch Game --> 'Safe Mode' to remove symlinks from all locations.
     
🟢 Remember: this is just an explanation of how it works. All YOU have to do is press 1-2 buttons.
