all of my loader look for a prefix of themselves essentially

version.dll will load anything that contains *-version.dll in the name (version.dll will also load version.asi files)
drd12.dll will load anything that contains *-drd12.dll in the name
dinput8.dll will load anything that contains *-dinput8.dll in the name
dsound.dll will load anything that contains *-dsound.dll in the name
dxgi.dll will load anything that contains *-dxgi.dll in the name

* = name you choose before the prefix.

example:
- InsaneMod has a version.dll --> rename version.dll to Insane-version.dll 
- Same goes for every dll listed above.
