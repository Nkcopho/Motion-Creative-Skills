[CmdletBinding()]
param([ValidateSet('codex','claude','both')][string]$Agent='both', [ValidateSet('user','project')][string]$Scope='user', [string]$ProjectPath=(Get-Location).Path, [switch]$Force)
$ErrorActionPreference='Stop'
$root=(Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$source=Join-Path $root 'skills'
if (!(Test-Path (Join-Path $root 'knowledge/OPERATING_CONTRACT.md'))) { throw 'Incomplete suite. Extract the entire ZIP first.' }
$base=if ($Scope -eq 'user') {$HOME} else {(Resolve-Path $ProjectPath).Path}
$agents=if ($Agent -eq 'both') {@('codex','claude')} else {@($Agent)}
$destinations=@()
foreach($a in $agents){
  $folder=if($a -eq 'codex'){'.agents/skills'}else{'.claude/skills'}
  $destinations+=Join-Path $base $folder
}
$skills=@(Get-ChildItem -LiteralPath $source -Directory)
# Preflight all collisions before writing. Never overwrite an unrelated skill, even with Force.
foreach($dest in $destinations){foreach($skill in $skills){
  $target=Join-Path $dest $skill.Name
  if(Test-Path -LiteralPath $target){
    $marker=Join-Path $target '.umpha-owned'
    if(!(Test-Path -LiteralPath $marker)){throw "Unrelated existing skill: $target. Rename or move it manually."}
    if((Get-Content -LiteralPath $marker -Raw).Trim() -ne 'umpha-creative-intelligence'){throw "Invalid ownership marker: $target"}
    if(!$Force){throw "Existing Umpha skill: $target. Use -Force to update owned copies."}
  }
}}
foreach($dest in $destinations){
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  foreach($skill in $skills){
    $target=Join-Path $dest $skill.Name
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    Copy-Item -Path (Join-Path $skill.FullName '*') -Destination $target -Recurse -Force
    Set-Content -LiteralPath (Join-Path $target '.umpha-owned') -Value 'umpha-creative-intelligence' -Encoding UTF8
    $note="Shared suite root (absolute path):`n`n$root`n`nRead knowledge/OPERATING_CONTRACT.md at this root. All suite-relative references resolve here. Keep this directory available; rerun installer if it moves."
    Set-Content -LiteralPath (Join-Path $target 'references/workspace.md') -Value $note -Encoding UTF8
  }
  Write-Host "Registered $($skills.Count) skills at $dest"
}
Write-Host 'Restart/open a new agent session. The shared suite stays at its current extracted location.'
