$ErrorActionPreference='Stop'
$root=Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
Set-ExecutionPolicy -Scope Process Bypass
& (Join-Path $root 'build.ps1')
$server = Start-Process powershell -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-Command',"Set-Location '$root'; python -m http.server 5500" -PassThru
Start-Sleep -Seconds 2
Start-Process 'http://localhost:5500/preview.html'
Write-Host 'Preview opened at http://localhost:5500/preview.html' -ForegroundColor Green
