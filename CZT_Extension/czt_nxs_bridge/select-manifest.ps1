param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("chrome", "firefox")]
    [string]$Target
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifestPath = Join-Path $root "manifest.json"

if (-not (Test-Path $manifestPath)) {
        throw "Manifest not found: $manifestPath"
}

$backgroundChrome = @"
    "background": {
        "service_worker": "background.js"
    },
"@

$backgroundFirefox = @"
    "background": {
        "scripts": ["background.js"]
    },
"@

$content = Get-Content -Path $manifestPath -Raw

# Replace only the background block so the rest of the manifest stays unchanged.
$pattern = '(?ms)^[ \t]*"background"\s*:\s*\{.*?\}\s*,'
if (-not [regex]::IsMatch($content, $pattern)) {
    throw "Could not find background block in $manifestPath"
}

$replacement = if ($Target -eq "firefox") { $backgroundFirefox } else { $backgroundChrome }
$updated = [regex]::Replace($content, $pattern, $replacement, 1)
Set-Content -Path $manifestPath -Value $updated -NoNewline

Write-Host "Updated background in $manifestPath for target '$Target'."
