## Resources
--> [CZT - Homepage](https://github.com/CaZual-T/CZT-Mod-Manager/tree/main)</br>
--> [CZT - How it works](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/INFO_how_cztmm_works.md)</br>
--> [CZT - Initial Install/Setup](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/CZT_Install_and_Setup.md)</br>
--> [CZT - Controls](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/GUIDE_controls.md)</br>
--> [How to Install/Update Mods](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/GUIDE_install-update_mods.md)</br>
--> [Xbox: Forza Horizon 6 Guide](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/GUIDE_xbox_forzahorizon6.md)</br>
--> [Schedule I Info](https://github.com/CaZual-T/CZT-Mod-Manager/blob/main/docs/GUIDE_schedule_I.md)

# Common errors w/ solutions:

### Windows says its a virus and stopped my download/install
- CZT Mod Manager is an unsigned app, it will ALWAYS hit windows defender etc.
- NOTE THAT NEXUS STAFF HAS ACCESS TO MY SOURCE CODE. Thats quite literally the only reassurance i can give you.
- Use it, dont use it, idgaf at this point. Im not going to beg/plead with people.

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
    
### "A mod i have installed has an update available but CZT isnt flagging it"
  - This happens when creators upload a new version of a mod but didnt use/update the EXISTING file.
    - When uploading to a mod page, users can choose to upload a new file, or UPDATE an existing one.
      - If they uploaded as new instead of updating an existing one, it breaks the file_id branch.
  - 20260616 
    - Nexus has updated their upload/update process making it much more streamlined.
    - CZT has been updated to the latest nexus v3 endpoints.
      - ~~There's no real fix for this other than to manually download from nexus, and hope the creator doesnt keep updating incorrectly.~~
      - ~~I could make it compare against mod page version, or when a new file is uploaded, but that is messy and leads to false positives.~~

### Download/Update Failure (mods):
- Note_1: Ensure that you have your api key saved in both the main app and the extension (if you use it)
- Note_2: You HAVE to get a new API key if you ever upgrade or downgrade your nexus premium status.

### Updating CZT Mod Manager
- CZT will detect and notify you in app if their is an available update.
- Updates can be downloaded and installed without ever needing to open a browser.
