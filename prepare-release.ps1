#Requires -Version 5.1
<#
.SYNOPSIS
  Hide development files under _hidden/ so the mod folder can be uploaded.

.DESCRIPTION
  Run from the mod root (or invoke this script by path). Moves, preserving
  relative paths into _hidden/:

    .cursor/, gdd/, scripts/, tools/
    .git* at the mod root
    *.hsl, *.hml, *.include anywhere except _hidden/
    this script
#>
$ErrorActionPreference = 'Stop'

$Root = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$Hidden = Join-Path $Root '_hidden'
$Self = $PSCommandPath

function Test-UnderHidden([string]$FullPath) {
    $prefix = $Hidden.TrimEnd('\') + '\'
    return $FullPath.Equals($Hidden, [StringComparison]::OrdinalIgnoreCase) -or
        $FullPath.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)
}

function Get-HiddenDestination([string]$FullPath) {
    $relative = $FullPath.Substring($Root.Length).TrimStart('\')
    return Join-Path $Hidden $relative
}

function Move-ToHidden {
    param(
        [Parameter(Mandatory)]
        [string]$SourcePath
    )
    if (-not (Test-Path -LiteralPath $SourcePath)) {
        return
    }
    $full = (Resolve-Path -LiteralPath $SourcePath).Path
    if (Test-UnderHidden $full) {
        return
    }

    $dest = Get-HiddenDestination $full
    $destDir = Split-Path -Parent $dest
    if (-not (Test-Path -LiteralPath $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    if (Test-Path -LiteralPath $dest) {
        Write-Warning "Already in _hidden, skipped: $($full.Substring($Root.Length).TrimStart('\'))"
        return
    }

    Move-Item -LiteralPath $full -Destination $dest
    Write-Host "  $($full.Substring($Root.Length).TrimStart('\'))"
    $script:Moved++
}

$script:Moved = 0
New-Item -ItemType Directory -Path $Hidden -Force | Out-Null

Write-Host "Hiding development files -> _hidden\"
Write-Host ""

foreach ($name in @('.cursor', 'gdd', 'scripts', 'tools')) {
    Move-ToHidden (Join-Path $Root $name)
}

Get-ChildItem -LiteralPath $Root -Force | Where-Object {
    $_.Name -like '.git*'
} | ForEach-Object {
    Move-ToHidden $_.FullName
}

Get-ChildItem -LiteralPath $Root -Recurse -File -Force | Where-Object {
    $_.Extension -in @('.hsl', '.hml', '.include') -and
        -not (Test-UnderHidden $_.FullName)
} | ForEach-Object {
    Move-ToHidden $_.FullName
}

Write-Host ""
Move-ToHidden $Self
Write-Host ""
Write-Host "Done. Moved $Moved item(s)."
