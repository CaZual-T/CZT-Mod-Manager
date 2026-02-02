using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class ConflictResolver
{
    private readonly List<ModFile> _originalFiles;
    private readonly IScriptMerger _scriptMerger;

    public ConflictResolver(List<ModFile> originalFiles)
    {
        _originalFiles = originalFiles;
        _scriptMerger = new ScrMerger();
    }

    public (Dictionary<string, byte[]> FinalFiles, Dictionary<string, List<string>> MergeSummary) Resolve(List<ModFile> moddedFiles)
    {
        var reporter = new MergeReporter();
        var finalFileContents = new Dictionary<string, byte[]>();
        var modFileGroups = moddedFiles.GroupBy(s => s.FullPathInPak)
                                       .ToDictionary(g => g.Key, g => g.ToList());

        var mergeSummary = new Dictionary<string, List<string>>();

        foreach (var group in modFileGroups)
        {
            string filePath = group.Key;
            List<ModFile> modsTouchingThisFile = group.Value;

            mergeSummary[filePath] = modsTouchingThisFile.Select(m => m.SourcePak).Distinct().ToList();

            if (filePath.EndsWith(".scr", StringComparison.OrdinalIgnoreCase))
            {
                var originalFile = _originalFiles.FirstOrDefault(f => f.FullPathInPak.Equals(filePath, StringComparison.OrdinalIgnoreCase));

                if (originalFile == null)
                {
                    if (modsTouchingThisFile.Count > 1)
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine($"\n[CHOICE REQUIRED] Conflict for NEWLY ADDED script file: '{filePath}'");
                        Console.ResetColor();
                        Console.WriteLine("  This new script is provided by the following mods:");
                        var chosenFile = HandleAssetConflict(modsTouchingThisFile);
                        finalFileContents[filePath] = chosenFile.Content;
                    }
                    else
                    {
                        finalFileContents[filePath] = modsTouchingThisFile[0].Content;
                    }
                    continue;
                }

                var result = _scriptMerger.Merge(originalFile, modsTouchingThisFile, null, reporter);
                finalFileContents[filePath] = new UTF8Encoding(false).GetBytes(result.MergedContent);
            }
            else
            {
                if (modsTouchingThisFile.Count == 1)
                {
                    finalFileContents[filePath] = modsTouchingThisFile[0].Content;
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"\n[CHOICE REQUIRED] Conflict for asset file: '{filePath}'");
                    Console.ResetColor();
                    Console.WriteLine("  This asset is included in the following mods:");
                    var chosenFile = HandleAssetConflict(modsTouchingThisFile);
                    finalFileContents[filePath] = chosenFile.Content;
                }
            }
        }

        if (reporter.HasEntries())
        {
            string logPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Merge_Log.txt");
            File.WriteAllText(logPath, reporter.GetReport());
        }

        return (finalFileContents, mergeSummary);
    }

    private ModFile HandleAssetConflict(List<ModFile> mods)
    {
        for (int i = 0; i < mods.Count; i++)
        {
            Console.Write($"    {i + 1}. ");
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine(mods[i].SourcePak);
            Console.ResetColor();
        }

        int choice = -1;
        while (choice < 1 || choice > mods.Count)
        {
            Console.Write($"Please select which mod's version to use (1-{mods.Count}): ");
            string? input = Console.ReadLine();
            int.TryParse(input, out choice);
        }
        var chosenFile = mods[choice - 1];

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("  -> Choice applied.");
        Console.ResetColor();

        return chosenFile;
    }
}