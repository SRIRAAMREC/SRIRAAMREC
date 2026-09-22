$ErrorActionPreference='Stop'
$root=Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
$py=Get-Command python -ErrorAction SilentlyContinue
if(-not $py){ throw 'Python 3 is required. Install Python 3.10+ and rerun.' }
python -m pip install --disable-pip-version-check --quiet pillow requests beautifulsoup4

$avatar=Join-Path $root 'assets\sriraam-avatar.png'
$prep=Join-Path $root 'assets\source-prepped.png'
$ascii=Join-Path $root 'assets\sriraam-ascii.svg'
$wordmark=Join-Path $root 'assets\wordmark.svg'
$contrib=Join-Path $root 'assets\contrib-heatmap.svg'

Write-Host '[1/4] Downloading your current GitHub avatar...' -ForegroundColor Cyan
Invoke-WebRequest -Uri 'https://avatars.githubusercontent.com/u/148420865?s=460&v=4' -OutFile $avatar -UseBasicParsing

Write-Host '[2/4] Building animated ASCII portrait...' -ForegroundColor Cyan
python (Join-Path $root 'scripts\prep_avatar.py') $avatar $prep
python (Join-Path $root 'scripts\make_ascii_svg.py') $prep $ascii

Write-Host '[3/4] Building 3D ASCII wordmark...' -ForegroundColor Cyan
python (Join-Path $root 'scripts\make_wordmark_svg.py') SRIRAAM $wordmark

Write-Host '[4/4] Fetching your real GitHub contributions...' -ForegroundColor Cyan
$env:GH_PROFILE_USER='SRIRAAMREC'
python (Join-Path $root 'scripts\fetch_contributions.py')
python (Join-Path $root 'scripts\render_heatmap_svg.py')

Write-Host ''
Write-Host 'BUILD COMPLETE.' -ForegroundColor Green
Write-Host 'README.md + ASCII portrait + wordmark + real contribution heatmap are ready.' -ForegroundColor Green
Write-Host ''
