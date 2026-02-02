using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

public interface INodeContent
{
    string GetSignature();
    int OriginalOrder { get; set; }
}

public class ParameterContent : INodeContent
{
    public string Value { get; set; } = string.Empty;
    public string Key { get; set; } = string.Empty;
    public int OriginalOrder { get; set; }
    public string GetSignature() => Key;
}
    public class ChildNodeContent : INodeContent
    {
        public ScrMerger.ScriptNode Node { get; set; }
        public int OriginalOrder { get; set; }
        public string GetSignature()
        {
            if (Node.Signature.Trim().StartsWith("DLC_Set")) 
            {
                return ScrMerger.GetUniqueKeyForDlcBlock(Node);
            }
            return ScrMerger.TryParseKey(Node.Signature) ?? Node.Signature;
        }
    }


public interface IScriptMerger
{
(string MergedContent, string? UpdatedPreferredSource) Merge(ModFile original, List<ModFile> mods, string? currentPreferredSource, MergeReporter reporter);
}

public class ScrMerger : IScriptMerger
{
public class ScriptNode
{
    public ScriptNode? Parent { get; set; }
    public string Signature { get; set; } = string.Empty;
    public List<string> HeaderComments { get; set; } = new List<string>();
    public List<INodeContent> Contents { get; set; } = new List<INodeContent>();
    public int OriginalOrder { get; set; }
}

private static readonly HashSet<string> ValueBasedKeyFunctions = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
{ "Health", "HealthTotalMul" };

public (string MergedContent, string? UpdatedPreferredSource) Merge(ModFile original, List<ModFile> mods, string? currentPreferredSource, MergeReporter reporter)
{
    reporter.StartNewFile(original.FullPathInPak, mods.Select(m => m.SourcePak).ToList());
    var encoding = Encoding.UTF8;
    var originalContentString = encoding.GetString(original.Content);
    var originalTree = ParseToTree(originalContentString);
    var modTrees = mods.Select(mod => (Source: mod.SourcePak, Tree: ParseToTree(encoding.GetString(mod.Content)))).ToList();
    var mergedTree = RecursiveMerge(originalTree, modTrees, reporter);
    var finalContent = RebuildScriptFromTree(mergedTree);
    return (finalContent, null);
}

private ScriptNode ParseToTree(string scriptContent)
{
    var lines = scriptContent.Replace("\r\n", "\n").Split('\n');
    var root = new ScriptNode { Signature = "ROOT" };
    var currentNode = root;
    var headerComments = new List<string>();
    int orderCounter = 0;
    Stack<ScriptNode> nodeStack = new Stack<ScriptNode>();
    nodeStack.Push(root);
    for (int i = 0; i < lines.Length; i++)
    {
        string line = lines[i];
        string trimmedLine = line.Trim();
        if (string.IsNullOrWhiteSpace(trimmedLine)) continue;
        if (trimmedLine.StartsWith("//")) { headerComments.Add(line); continue; }
        if (trimmedLine.StartsWith("}")) { if (nodeStack.Count > 1) { nodeStack.Pop(); currentNode = nodeStack.Peek(); } continue; }
        int braceIndex = trimmedLine.IndexOf('{');
        string signaturePart = braceIndex != -1 ? trimmedLine.Substring(0, braceIndex).Trim() : trimmedLine;
        bool isBlockStart = false;
        if (braceIndex != -1 && IsBlockSignature(signaturePart)) isBlockStart = true;
        else { var nextLine = (i + 1 < lines.Length) ? lines[i + 1].Trim() : ""; if (nextLine.StartsWith("{") && IsBlockSignature(trimmedLine)) { isBlockStart = true; signaturePart = trimmedLine; i++; } }
        if (isBlockStart)
        {
            var newNode = new ScriptNode { Signature = signaturePart, Parent = currentNode, OriginalOrder = orderCounter, HeaderComments = new List<string>(headerComments) };
            currentNode.Contents.Add(new ChildNodeContent { Node = newNode, OriginalOrder = orderCounter++ });
            nodeStack.Push(newNode);
            currentNode = newNode;
            headerComments.Clear();
            if (braceIndex != -1)
            {
                string restOfLine = trimmedLine.Substring(braceIndex + 1).Trim();
                if (restOfLine.EndsWith("}"))
                {
                    string innerContent = restOfLine.TrimEnd('}');
                    if (!string.IsNullOrWhiteSpace(innerContent))
                    {
                        var key = TryParseKey(innerContent.Trim()) ?? Guid.NewGuid().ToString();
                        newNode.Contents.Add(new ParameterContent { Value = innerContent.Trim(), Key = key, OriginalOrder = 0 });
                    }
                    nodeStack.Pop();
                    currentNode = nodeStack.Peek();
                }
            }
        }
        else
        {
            string key;
            var match = Regex.Match(line.Trim(), @"^(\w+)\s*\(");
            if (match.Success && ValueBasedKeyFunctions.Contains(match.Groups[1].Value))
            {
                key = match.Groups[1].Value;
            }
            else
            {
                key = TryParseKey(line) ?? Guid.NewGuid().ToString();
            }

            currentNode.Contents.Add(new ParameterContent { Value = line, Key = key, OriginalOrder = orderCounter++ });
            headerComments.Clear();
        }
    }
    return root;
}

private string RebuildScriptFromTree(ScriptNode node, int indentLevel = 0)
{
    var sb = new StringBuilder();
    string indent = new string('\t', indentLevel);
    if (node.Signature != "ROOT")
    {
        foreach (var comment in node.HeaderComments) sb.AppendLine(indent + comment);
        sb.AppendLine(indent + node.Signature);
        sb.AppendLine(indent + "{");
    }
    string contentIndent = node.Signature == "ROOT" ? "" : indent + "\t";
    foreach (var content in node.Contents.OrderBy(c => c.OriginalOrder))
    {
        if (content is ParameterContent param) sb.AppendLine(string.IsNullOrWhiteSpace(param.Value) ? "" : (char.IsWhiteSpace(param.Value[0]) ? param.Value : contentIndent + param.Value.Trim()));
        else if (content is ChildNodeContent child) sb.Append(RebuildScriptFromTree(child.Node, node.Signature == "ROOT" ? indentLevel : indentLevel + 1));
    }
    if (node.Signature != "ROOT") sb.AppendLine(indent + "}");
    return sb.ToString();
}

public static string GetUniqueKeyForDlcBlock(ScriptNode node)
{
    foreach (var content in node.Contents)
    {
        if (content is ParameterContent param)
        {
            var idMatch = Regex.Match(param.Value.Trim(), @"^ID\s*\(\s*(\d+)\s*\)");
            if (idMatch.Success) return $"{TryParseKey(node.Signature)}_ID_{idMatch.Groups[1].Value}";
        }
    }
    return $"{TryParseKey(node.Signature)}_{Guid.NewGuid()}";
}

private ScriptNode RecursiveMerge(ScriptNode originalNode, List<(string Source, ScriptNode Tree)> modNodes, MergeReporter reporter)
{
    var mergedNode = new ScriptNode { Signature = originalNode.Signature, HeaderComments = new List<string>(originalNode.HeaderComments) };
    var allSignatures = new HashSet<string>();

    Action<INodeContent> addSignature = (content) => {
        allSignatures.Add(content.GetSignature());
    };

    originalNode.Contents.ForEach(addSignature);
    modNodes.ForEach(mod => mod.Tree.Contents.ForEach(addSignature));

    var signaturesInMods = new HashSet<string>();
    modNodes.ForEach(mod => mod.Tree.Contents.ForEach(c => signaturesInMods.Add(c.GetSignature())));


    var allSignaturesOrdered = allSignatures
        .Select(sig => (Signature: sig, Order: originalNode.Contents.FirstOrDefault(c => c.GetSignature() == sig)?.OriginalOrder ?? modNodes.SelectMany(m => m.Tree.Contents).FirstOrDefault(c => c.GetSignature() == sig)?.OriginalOrder ?? int.MaxValue))
        .OrderBy(x => x.Order)
        .Select(x => x.Signature)
        .ToList();

    foreach (var signature in allSignaturesOrdered)
    {
        var originalContent = originalNode.Contents.FirstOrDefault(c => c.GetSignature() == signature);
        var modContents = modNodes.Select(m => (Source: m.Source, Content: m.Tree.Contents.FirstOrDefault(c => c.GetSignature() == signature))).Where(mc => mc.Content != null).ToList();

        if (originalContent != null && !signaturesInMods.Contains(signature) && modNodes.Any())
        {
            continue;
        }

        if (originalContent == null)
        {
            var distinctNewContents = modContents.GroupBy(m => RebuildContent(m.Content!))
                                                 .Select(g => g.First())
                                                 .ToList();

            if (!distinctNewContents.Any()) continue;

            foreach (var newContent in distinctNewContents)
            {
                if (newContent.Content is ChildNodeContent newChild)
                {
                    reporter.LogNewBlock(newChild.Node.Signature, newContent.Source);
                    newChild.Node.HeaderComments.Insert(0, $"// -- [UTM Merge] Block added from {newContent.Source} --");
                }
                mergedNode.Contents.Add(newContent.Content!);
            }
            continue;
        }
        if (originalContent is ParameterContent originalParam)
        {
            var actualChanges = modContents.Where(mc => mc.Content is ParameterContent && (mc.Content as ParameterContent).Value.Trim() != originalParam.Value.Trim()).Select(mc => ((mc.Content as ParameterContent), mc.Source)).ToList();
            if (actualChanges.Count == 0)
            {
                mergedNode.Contents.Add(originalParam);
            }
            else
            {
                var distinctChanges = actualChanges.GroupBy(c => c.Item1.Value.Trim()).Select(g => (Param: g.First().Item1, Sources: g.Select(c => c.Source).ToList())).ToList();
                ParameterContent chosenParam; string sourceForComment;
                if (distinctChanges.Count == 1) { chosenParam = distinctChanges[0].Param; sourceForComment = distinctChanges[0].Sources.First(); }
                else chosenParam = HandleUserChoiceForParams(distinctChanges, originalParam, out sourceForComment);
                string ogValue = ExtractValueFromLine(originalParam.Value) ?? "N/A", chosenValue = ExtractValueFromLine(chosenParam.Value) ?? "N/A";
                reporter.LogParameterChange(originalNode.Signature, originalParam.Key, ogValue, chosenValue, sourceForComment);
                var paramToAdd = new ParameterContent { Key = chosenParam.Key, OriginalOrder = chosenParam.OriginalOrder, Value = AppendUtmComment(chosenParam.Value, $"[UTM Merge] updated from {sourceForComment} (OG Value: {ogValue})") };
                mergedNode.Contents.Add(paramToAdd);
            }
        }
        else if (originalContent is ChildNodeContent originalChild)
        {
            var modChildren = modContents.Select(m => (m.Source, Tree: (m.Content as ChildNodeContent)!.Node)).ToList();
            if (modChildren.Any())
            {
                var mergedChildNode = RecursiveMerge(originalChild.Node, modChildren, reporter);
                var signatureChange = modChildren.FirstOrDefault(m => m.Tree.Signature != originalChild.Node.Signature);
                if (signatureChange != default)
                {
                    string oldSignature = originalChild.Node.Signature;
                    string newSignature = signatureChange.Tree.Signature;
                    mergedChildNode.Signature = newSignature;
                    reporter.LogParameterChange(originalNode.Signature, oldSignature, "(Block Signature itself)", newSignature, signatureChange.Source);
                    mergedChildNode.HeaderComments.Add($"// -- [UTM Merge] Block from {signatureChange.Source} --");
                }
                mergedNode.Contents.Add(new ChildNodeContent { Node = mergedChildNode, OriginalOrder = originalChild.OriginalOrder });
            }
            else
            {
                mergedNode.Contents.Add(originalChild);
            }
        }
    }
    return mergedNode;
}
private string RebuildContent(INodeContent content)
{
    if (content is ParameterContent param) return param.Value;
    if (content is ChildNodeContent child) return RebuildScriptFromTree(child.Node);
    return string.Empty;
}

private ParameterContent HandleUserChoiceForParams(List<(ParameterContent Param, List<string> Sources)> distinctChanges, ParameterContent originalParam, out string sourceForComment)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine($"\n[CHOICE REQUIRED] Conflict for key '{originalParam.Key}'!");
    Console.ResetColor();
    for (int j = 0; j < distinctChanges.Count; j++)
    {
        string sources = string.Join(", ", distinctChanges[j].Sources);
        Console.Write($"    {j + 1}. (");
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Write(sources);
        Console.ResetColor();
        Console.Write("): ");
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine(distinctChanges[j].Param.Value.Trim());
        Console.ResetColor();
    }

    int choice = -1;
    while (choice < 1 || choice > distinctChanges.Count)
    {
        Console.Write($"Please select the version to use (1-{distinctChanges.Count}): ");
        string? input = Console.ReadLine();
        int.TryParse(input, out choice);
    }

    var chosenChange = distinctChanges[choice - 1];
    sourceForComment = chosenChange.Sources.First();
    Console.ForegroundColor = ConsoleColor.Green;
    Console.WriteLine("  -> Choice applied.");
    Console.ResetColor();
    return chosenChange.Param;
}

private bool IsBlockSignature(string trimmedLine) { if (string.IsNullOrWhiteSpace(trimmedLine) || trimmedLine.StartsWith("//")) return false; bool isFunctionLike = trimmedLine.Contains("(") && trimmedLine.Contains(")"); bool isSubroutine = trimmedLine.StartsWith("sub "); return isFunctionLike || isSubroutine; }
    public static string? TryParseKey(string line)
    {
        string trimmedLine = line.Trim();
        if (trimmedLine.StartsWith("//") || string.IsNullOrWhiteSpace(trimmedLine))
        {
            return null;
        }

        var match = Regex.Match(trimmedLine, @"^(\w+)\s*\(");
        if (match.Success)
        {
            string functionName = match.Groups[1].Value;

            var paramMatch = Regex.Match(trimmedLine, @"^(\w+)\s*\(\s*""([^""]+)""");
            if (paramMatch.Success)
            {
                return $"{functionName}_{paramMatch.Groups[2].Value}";
            }

            paramMatch = Regex.Match(trimmedLine, @"^(\w+)\s*\(\s*([^,]+),");
            if (paramMatch.Success)
            {
                string firstParam = paramMatch.Groups[2].Value.Trim().Replace("\"", "");
                return $"{functionName}_{firstParam}";
            }

            paramMatch = Regex.Match(trimmedLine, @"^(\w+)\s*\(([^)]+)\)");
            if (paramMatch.Success)
            {
                string singleParam = paramMatch.Groups[2].Value.Trim().Replace("\"", "");
                return $"{functionName}_{singleParam}";
            }

            return functionName;
        }
        return line;
    }
    private string? ExtractValueFromLine(string line) { if (string.IsNullOrEmpty(line)) return null; var match = Regex.Match(line, @"\((.+)\)"); if (match.Success) return match.Groups[1].Value.Trim(); return line.Trim(); }
private string AppendUtmComment(string line, string comment) { string trimmedLine = line.TrimEnd(); if (trimmedLine.Contains("//")) return $"{trimmedLine} # {comment}"; else return $"{trimmedLine.PadRight(80)}// {comment}"; }
}