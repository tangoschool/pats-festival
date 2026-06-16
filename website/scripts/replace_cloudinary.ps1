# Backup HTML files
$backupDir = "_backup_html"
if (-not (Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir | Out-Null }
$htmlFiles = Get-ChildItem -Path . -Recurse -Include *.html
foreach ($f in $htmlFiles) { $dest = Join-Path $backupDir ($f.FullName.Replace((Get-Location).Path,'').TrimStart('\') -replace '[\\/]','_'); Copy-Item -Path $f.FullName -Destination $dest -Force }

# Read URLs and create mapping to filenames
$urls = @()
if (-not (Test-Path "cloudinary_urls.txt")) { Write-Error "cloudinary_urls.txt not found in current directory."; exit 1 }
$urls = Get-Content cloudinary_urls.txt | Where-Object { $_ -and $_ -ne '' }
$map = @{}
foreach ($u in $urls) {
    try {
        $uri = [System.Uri]::new($u)
        $fname = [System.IO.Path]::GetFileName($uri.LocalPath)
        if (-not [string]::IsNullOrEmpty($fname)) { $map[$u] = "images/$fname" }
    } catch {
        # fallback: take substring after last '/'
        $parts = $u -split '/' ; $fname = $parts[-1] ; $fname = $fname -split "[\?]" | Select-Object -First 1 ; $map[$u] = "images/$fname"
    }
}

# Replace occurrences in HTML files
$changedFiles = @()
foreach ($f in $htmlFiles) {
    $text = Get-Content -Raw -Encoding UTF8 $f.FullName
    $orig = $text
    foreach ($k in $map.Keys) {
        $escaped = [regex]::Escape($k)
        $text = [regex]::Replace($text, $escaped, $map[$k])
    }
    if ($text -ne $orig) {
        Set-Content -Path $f.FullName -Value $text -Encoding UTF8
        $changedFiles += $f.FullName
        Write-Output "Updated: $($f.FullName)"
    }
}
Write-Output "Done. Files updated: $($changedFiles.Count)"
if ($changedFiles.Count -gt 0) { Write-Output "Backups stored in: $backupDir" }
