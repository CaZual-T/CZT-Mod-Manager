using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

public class MergeReporter
{
    private readonly StringBuilder _log = new StringBuilder();
    private string _currentFile = string.Empty;
    public void StartNewFile(string filePath, List<string> modSources)
    {
        if (_log.Length > 0)
        {
            _log.AppendLine("\n");
        }
        _log.AppendLine("==============================================================================");
        _log.AppendLine($"MERGED FILE: {filePath}");
        _log.AppendLine("==============================================================================");
        _log.AppendLine($"\nContributing Mods:\n - {string.Join("\n - ", modSources)}\n");
        _currentFile = filePath;
    }

    public void LogParameterChange(string blockSignature, string key, string originalValue, string chosenValue, string sourceMod)
    {
        _log.AppendLine($"-- CHANGE in block '{blockSignature}' for key '{key}' --");
        _log.AppendLine($" -> Original Value: {originalValue}");
        _log.AppendLine($" -> Change from '{sourceMod}': {chosenValue}\n");
    }
    public void LogNewBlock(string newBlockSignature, string sourceMod)
    {
        _log.AppendLine($"-- NEW BLOCK ADDED from '{sourceMod}' --");
        _log.AppendLine($" -> Block Signature: {newBlockSignature}\n");
    }

    public bool HasEntries() => _log.Length > 0;
    public string GetReport() => _log.ToString();
}