$folder = "D:\images"  # Takip edilecek klasör
$filter = "*.jpg"  # Takip edilecek dosya türü (PNG için "*.png" ekleyebilirsin)

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $folder
$watcher.Filter = $filter
$watcher.EnableRaisingEvents = $true

Write-Host "Yeni dosya izleniyor: $folder" -ForegroundColor Green

while ($true) {
    $change = $watcher.WaitForChanged("Created")
    Write-Host "Yeni dosya algılandı: $($change.Name)" -ForegroundColor Yellow
    Start-Process -NoNewWindow -FilePath "python" -ArgumentList "D:\convert.py"
}
