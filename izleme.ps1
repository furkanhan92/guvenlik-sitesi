$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "D:\guvenlik-sitesi\images"
$watcher.Filter = "*.*"
$watcher.IncludeSubdirectories = $false
$watcher.EnableRaisingEvents = $true

$action = {
    Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList "/c D:\guvenlik-sitesi\donustur.bat"
}

Register-ObjectEvent $watcher "Created" -Action $action

while ($true) { Start-Sleep 1 }
