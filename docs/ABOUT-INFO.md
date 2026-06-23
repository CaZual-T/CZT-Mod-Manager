## Where does CZT store mods?
- All mods are stored within "{Drive}:\CZT Mod Manager\czt_mod_data\installed_mods\{profile_name}"

## How does CZT know where to install mods?
### CZT Mod Manager utilizes multiple 'engines'</br>
<img width="275" height="256" alt="image" src="https://github.com/user-attachments/assets/05e5b8a1-6b3d-4a7e-a8cb-96b8c49249b6" /></br>
- These are the main components that drives installations, and linking for every profile.
- Seperate engines also allow me to update and maintain profiles efficiently without breaking the entire manager.

### Game Specific Info:
  - Ready or Not:
    - Content mods are the ones that go into Content/FMOD, MOVIES, SPLASH, VO_MOD
    - Pak files go into Content/PAKS/Mods/
  - Forza Horizon 6:
    - Here we essentially take a snapshot of the vanilla files + some assistance from .ext filtering to recreate the vanilla structure 1:1.
    - Forza mods are then normalized to a mediapc/{scope} structure and "overlayed". CZT Normalizes mods to mediapc to simply keep things cleaner.
    - Uninstall is simple, Press F8, or launch game --> unlink | safe mode. This then removes our overlayed files and reverts to the vanilla files we staged earlier.
  - Schedule I:
    - The simplest out of all of them due to how it utilizes a traditional mods folder.
  - Dying light (all):
    - Installs .pak files to source.
      - automatically detects conflicting pak names, and will rename at the users discretion.
      - .dll and .asi are handled accordingly. 
