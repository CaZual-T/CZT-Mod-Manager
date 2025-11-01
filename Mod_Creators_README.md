==========================================================================================
[!] This information is for mod creators. 

[!] Manifest file name should always = "_mod_info.json"
	> Place manifest at top level of your folder or compressed file. See example mods.
==========================================================================================

[Variable_Definitions]

# "profile_name" = game your mod is for.
+ Available profiles to use in 'profile_name' var.
> 7DTD
> Dying Light 1
> Dying Light 2
> DL The Beast
> Ready or Not
> Schedule I

# "display_name" = Whatever you want to show as the mod name in the UI
# "mod_local_version" = version number to display in UI
# "nexus_url" = url of mod
# "files_to_install" = name of file(s) to install
# "folder_to_install" = name of single folder to install
# "folders_to_install" = dict of folders to install

# "destination" = 
+ Available destination to use in 'destination' var.
> profile_mods/7DTD/Mods/
> profile_mods/Ready or Not/mod.czt/
> profile_mods/Dying Light 1/
> profile_mods/Dying Light 2/
> profile_mods/DL The Beast/
> profile_mods/Schedule I/Mods/

===========================================
// Single File Manifest (_mod_info.json)
===========================================

{
  "profile_name": "Ready or Not",
  "nexus_url": "https://www.nexusmods.com/readyornot/mods/741",
  "files_to_install": [
    {
        "source": "pakchunk96-Mods_NVG_P.pak",
        "display_name": "Fullscreen NVG Rework",
        "mod_local_version": "2.0"
    }
  ],
  "destination": "profile_mods/Ready or Not/mod.czt/"
}

[NOTES] 
# display_name = Name that will display in gui
# mod_local_vesrion = Local version to display in gui
# files_to_install = Source: file to install | Destination: Profile path/file_to_install

===========================================
// Multi File Manifest (_mod_info.json)
===========================================

{
  "profile_name": "Ready or Not",
  "nexus_url": "https://www.nexusmods.com/readyornot/mods/3796",
  "files_to_install": [
    {
        "source": "pakchunk999-Mods_BAL_UE5_CTS-7290_Flashbangs_P.pak",
        "display_name": "Flashbangs Pack",
        "mod_local_version": "1.1"
    },
    {
        "source": "pakchunk998-Mods_BAL_RC_Attachment-Expansion_P.pak",
        "display_name": "Attachment Expansion",
        "mod_local_version": "1.2"
    },
    {
        "source": "pakchunk999-Mods_BAL_LSS3_Addon_KAC_L403A1_P.pak",
        "display_name": "KAC L403A1 Addon",
        "mod_local_version": "1.3"
    },
    {
        "source": "pakchunk999-Mods_BAL_RC_Addon_BCM-Recce14-KMR_P.pak",
        "display_name": "BCM Recce 14 KMR Addon",
        "mod_local_version": "1.4"
    },
    {
        "source": "pakchunk999-Mods_BAL_UE5_Nightvision-Expansion_P.pak",
        "display_name": "Nightvision Expansion",
        "mod_local_version": "1.5"
    }
  ],
  "destination": "profile_mods/Ready or Not/mod.czt/"
}

[NOTES] 
# display_name = Name that will display in gui
# mod_local_vesrion = Local version to display in gui
# files_to_install = Source: file to install | Destination: Profile path/file_to_install

===========================================
// Single Folder Manifest (_mod_info.json)
===========================================

{
  "profile_name": "7DTD",		
  "display_name": "A Mod For 7DTD",	
  "mod_local_version": "6.29",
  "nexus_url": "https://www.nexusmods.com/dyinglightthebeast/mods/120",
  "folder_to_install": "7DTD_MOD_TEST",
  "destination": "profile_mods/7DTD/Mods/" 
}

[NOTES] 
# display_name = Name that will display in gui
# mod_local_vesrion = Local version to display in gui
# destination = Use the destinations from the top of the file. You do not need to include anything after that. 
> CZT will append your folder name(s) from above to the destination you set.

===========================================
// Multi Folder Manifest (_mod_info.json)
===========================================

{
  "profile_name": "7DTD",
  "nexus_url": "https://www.nexusmods.com/7daystodie/mods/3285",
  "folders_to_install": [		 
    "Pants Weapon Pack Laser Weapons",
    "FullautoLauncher",
    "CustomMuzzleFlash",
    "0-CustomParticleLoader",
    "Pants Weapon Pack"
  ],
  "folders_info": {
    "Pants Weapon Pack": {
      "display_name": "Main Weapon Pack",
      "mod_local_version": "4.6"
    },
    "Pants Weapon Pack Laser Weapons": {
      "display_name": "Laser Weapons",
      "mod_local_version": "1.0"
    },
    "FullautoLauncher": {
      "display_name": "Fullauto Launcher",
      "mod_local_version": "2.1"
    },
    "CustomMuzzleFlash": {
      "display_name": "Custom Muzzle Flash",
      "mod_local_version": "1.5"
    },
    "0-CustomParticleLoader": {
      "display_name": "Custom Particle Loader",
      "mod_local_version": "1.2"
    }
  },
  "destination": "profile_mods/7DTD/Mods/"
}

[NOTES]
# folders_to_install = The exact names of the folders you wish to have installed.
# display_name = Name that will display in gui.
# mod_local_vesrion = Local version to display in gui.
# destination = Use the destinations from the top of the file. You do not need to include anything after that. 
> CZT will append your folder name(s) from above to the destination you set.