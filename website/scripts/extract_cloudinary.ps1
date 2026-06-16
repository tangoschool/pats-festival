$pattern = 'https?://res.cloudinary.com[^"\s<>)]+'
$hash = @{}
Get-ChildItem -Path . -Recurse -Include *.html | ForEach-Object {
    try {
        $text = Get-Content -Raw -Encoding UTF8 $_.FullName
        [regex]::Matches($text, $pattern) | ForEach-Object { $hash[$_.Value] = $true }
    } catch {
        Write-Error ("Failed to read {0}: {1}" -f $_.FullName, $_)
    }
}
$urls = $hash.Keys | Sort-Object
$urls | Out-File -FilePath "cloudinary_urls.txt" -Encoding utf8
$urls | ForEach-Object { Write-Output $_ }
