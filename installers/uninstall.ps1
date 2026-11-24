[CmdletBinding(SupportsShouldProcess)]
param([ValidateSet('codex','claude','both')][string]$Agent='both',[ValidateSet('user','project')][string]$Scope='user',[string]$ProjectPath=(Get-Location).Path)
$ErrorActionPreference='Stop'
$base=if($Scope -eq 'user'){$HOME}else{(Resolve-Path $ProjectPath).Path}
$agents=if($Agent -eq 'both'){@('codex','claude')}else{@($Agent)}
$index=Get-Content -Raw (Join-Path $PSScriptRoot '../skills-index.json') | ConvertFrom-Json
foreach($a in $agents){$folder=if($a -eq 'codex'){'.agents/skills'}else{'.claude/skills'};foreach($s in $index){$target=Join-Path (Join-Path $base $folder) $s.name;$marker=Join-Path $target '.umpha-owned';if((Test-Path -LiteralPath $marker) -and ((Get-Content -LiteralPath $marker -Raw).Trim() -eq 'umpha-creative-intelligence')){if($PSCmdlet.ShouldProcess($target,'Remove Umpha skill')){Remove-Item -LiteralPath $target -Recurse -Force}}}}
