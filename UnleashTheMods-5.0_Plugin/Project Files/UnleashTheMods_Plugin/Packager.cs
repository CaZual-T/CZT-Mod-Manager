using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;

public static class Packager
{
    public static void PackageFiles(string sourceDirectory, string stagingDirectory, string profileModsDirectory, Dictionary<string, byte[]> finalFileContents, Dictionary<string, List<string>> mergeSummary) // CZT PATCH
    {
        Console.WriteLine("\n\n--- Merge Completed ---");

        Console.WriteLine("\n--- Creating Final .pak File ---");

        // CZT PATCH - Ensure mods_source directory exists
        if (!Directory.Exists(stagingDirectory))
            Directory.CreateDirectory(stagingDirectory);

        foreach (var fileEntry in finalFileContents)
        {
            string fullPath = Path.Combine(stagingDirectory, fileEntry.Key);
            Directory.CreateDirectory(Path.GetDirectoryName(fullPath) ?? string.Empty);
            File.WriteAllBytes(fullPath, fileEntry.Value);
        }
        Console.WriteLine($"{finalFileContents.Count} files written to temporary staging directory.");

        string finalPakPath = Path.Combine(profileModsDirectory, "data7.pak"); // CZT PATCH
        if (File.Exists(finalPakPath)) File.Delete(finalPakPath);

        ZipFile.CreateFromDirectory(stagingDirectory, finalPakPath, CompressionLevel.Optimal, false);

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"\nSUCCESS! All mods have been merged and saved as '{Path.GetFileName(finalPakPath)}' in the profile mods folder: {profileModsDirectory}"); // CZT PATCH
        Console.ResetColor();

        string logPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Merge_Log.txt");
        if (File.Exists(logPath))
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"A detailed merge log has been created: Merge_Log.txt");
            Console.ResetColor();
        }

        if (mergeSummary.Any())
        {
            Console.WriteLine();
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("╔══════════════════════════════════════════════════════════╗");
            Console.WriteLine("║                      QUICK MERGE SUMMARY                 ║");
            Console.WriteLine("╠══════════════════════════════════════════════════════════╣");

            var totalMods = mergeSummary.Values.SelectMany(mods => mods).Distinct().Count();

            string modsLine = $"  Total Mods Processed: {totalMods}";
            string filesLine = $"  Total Files Merged  : {mergeSummary.Count}";

            Console.ForegroundColor = ConsoleColor.White;

            Console.Write("║");
            Console.Write(modsLine.PadRight(58));
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("║");

            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("║");
            Console.Write(filesLine.PadRight(58));
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("║");

            Console.WriteLine("╚══════════════════════════════════════════════════════════╝");
            Console.ResetColor();
            Console.WriteLine();

            var groupedByDirectory = mergeSummary
                .Select(kvp => new { Directory = Path.GetDirectoryName(kvp.Key), FileName = Path.GetFileName(kvp.Key), Mods = kvp.Value })
                .GroupBy(f => f.Directory)
                .OrderBy(g => g.Key);

            foreach (var group in groupedByDirectory)
            {
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.WriteLine($"  ▼ {group.Key?.Replace('\\', '/')}/");
                Console.ResetColor();

                var filesInGroup = group.ToList();
                for (int i = 0; i < filesInGroup.Count; i++)
                {
                    var file = filesInGroup[i];
                    bool isLastFile = (i == filesInGroup.Count - 1);

                    string filePrefix = isLastFile ? "    └─" : "    ├─";
                    string modsPrefix = isLastFile ? "       " : "    │  ";

                    Console.ForegroundColor = ConsoleColor.White;
                    Console.WriteLine($"{filePrefix} {file.FileName}");

                    Console.ForegroundColor = ConsoleColor.Gray;
                    Console.WriteLine($"{modsPrefix}└─ Contributing Mods: {string.Join(", ", file.Mods)}\n");
                }
                Console.ResetColor();
            }
        }

        //Directory.Delete(stagingDirectory, true); // CZT

        // CZT Patch - Clean staging directory instead of deleting it fully
        string[] foldersToDelete = { "scripts", "temp", "mods" };
        string[] fileExtensionsToDelete = { ".czt", ".txt", ".md" };

        // Delete specific folders recursively and log each deletion
        Console.WriteLine($"[CLEAN] Check for, and remove leftover files from merge process...");
        foreach (var dir in Directory.GetDirectories(stagingDirectory, "*", SearchOption.AllDirectories))
        {
            string dirName = Path.GetFileName(dir);
            if (foldersToDelete.Contains(dirName, StringComparer.OrdinalIgnoreCase))
            {
                try
                {
                    Directory.Delete(dir, true);
                    Console.WriteLine($"[CLEAN] Deleted folder: {dir}");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[ERROR] Failed to delete folder '{dir}': {ex.Message}");
                }
            }
        }

        // Delete specific file extensions recursively and log each deletion
        foreach (var ext in fileExtensionsToDelete)
        {
            foreach (var file in Directory.GetFiles(stagingDirectory, $"*{ext}", SearchOption.AllDirectories))
            {
                try
                {
                    File.Delete(file);
                    Console.WriteLine($"[CLEAN] Deleted file: {file}");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[ERROR] Failed to delete file '{file}': {ex.Message}");
                }
            }
        }
    }
}