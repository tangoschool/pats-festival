# Replace occurrences of src="images/..." and src='images/...' with root-relative /images/ across HTML files
$htmlFiles = Get-ChildItem -Path . -Recurse -Include *.html
$changed = @()
foreach ($f in $htmlFiles) {
    $text = Get-Content -Raw -Encoding UTF8 $f.FullName
    $orig = $text
    $text = $text -replace 'src=\"images/','src="/images/'
    $text = $text -replace "src='images/","src='/images/"
    $text = $text -replace "src=images/","src=/images/"
    # also replace img src within srcset or data-src patterns
    $text = $text -replace 'data-src=\"images/','data-src="/images/'
    $text = $text -replace "data-src='images/","data-src='/images/"

    if ($text -ne $orig) { Set-Content -Path $f.FullName -Value $text -Encoding UTF8; $changed += $f.FullName; Write-Output "Fixed: $($f.FullName)" }
}
Write-Output "Done. Files changed: $($changed.Count)"
