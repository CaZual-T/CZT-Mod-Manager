### Nexus Account Status:
- You HAVE to go to the api key page and get a new key, IF you ever upgrade or downgrade your nexus premium status.

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
