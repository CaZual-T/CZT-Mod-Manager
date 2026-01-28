using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        Console.Title = "Unleash The Mods - Mod Merge Utility V5.0";
        Console.WriteLine("Unleash The Mods - Mod Merge Utility");
        Console.WriteLine("By MetalHeadbang a.k.a @unsc.odst");
        Console.WriteLine("Patched By CaZual_T ...x_x");

        string baseDirectory = AppDomain.CurrentDomain.BaseDirectory;
        // CZT PATCH // Use command-line arguments if provided, otherwise fall back to defaults
        string sourceDirectory = args.Length > 0 ? args[0] : Path.Combine(baseDirectory, "source");
        string modsDirectory = args.Length > 1 ? args[1] : Path.Combine(baseDirectory, "mods");
        string stagingDirectory = args.Length > 2 ? args[2] : Path.Combine(baseDirectory, "staging_area");

        Console.WriteLine($"[LOG] Source directory: {sourceDirectory}");
        Console.WriteLine($"[LOG] Mods directory: {modsDirectory}");
        Console.WriteLine($"[LOG] Staging directory: {stagingDirectory}");

        if (!Directory.Exists(sourceDirectory) || !Directory.Exists(modsDirectory))
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("\nERROR: 'source' and 'mods' folders not found!");
            Console.ResetColor();
            Console.ReadKey();
            return;
        }
        Console.WriteLine("'source' and 'mods' folders found.\n");

        string gamePakPath = Path.Combine(sourceDirectory, "data0.pak");
        if (!File.Exists(gamePakPath))
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("\nERROR: 'data0.pak' not found in source folder! Tool needs this file to work.");
            Console.ResetColor();
            Console.ReadKey();
            return;
        }
        
        var modCacher = new ModCacher(gamePakPath); // CZT
        var pakFiles = new[] { "data0.pak", "data1.pak" } // CZT
            .Select(name => Path.Combine(sourceDirectory, name)) // CZT
            .Where(File.Exists) // CZT
            .ToList(); // CZT
        var originalFiles = modCacher.LoadAllModFilesFromPaks(pakFiles.ToArray()); // CZT
        Console.WriteLine($"{originalFiles.Count} total files loaded from original game packages.");

        var moddedFiles = modCacher.LoadAndProcessMods(modsDirectory);

        if (moddedFiles.Count == 0)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("\nWarning: Couldn't find a compatible mod file (.pak, .zip, .rar, .7z) to merge in the 'mods' folder.");
            Console.ResetColor();
            Console.WriteLine("\nÇıkmak için herhangi bir tuşa basın...");
            Console.ReadKey();
            return;
        }

        Console.WriteLine("\n--- Merging Initializing ---");
        var resolver = new ConflictResolver(originalFiles);
        var (finalFileContents, mergeSummary) = resolver.Resolve(moddedFiles);

        // Go up three directories to reach the CZT Mod Manager root
        string rootDirectory = Path.GetFullPath(Path.Combine(baseDirectory, @"..\..\..")); // CZT

        // Use the root directory for the profile_mods output
        string profileModsDirectory = Path.Combine(rootDirectory, "CZT Mod Manager", "profile_mods", "DL The Beast"); // CZT
        if (!Directory.Exists(profileModsDirectory)) // CZT 
        {
            Directory.CreateDirectory(profileModsDirectory); // CZT
        }
        Packager.PackageFiles(sourceDirectory, stagingDirectory, profileModsDirectory, finalFileContents, mergeSummary); // CZT

        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();
    }
}
