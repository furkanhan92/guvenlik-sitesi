@echo off
cd /d "D:\guvenlik-sitesi\images"
for %%f in (*.jpg *.png) do (
    cwebp -q 80 "%%f" -o "D:\guvenlik-sitesi\webp\%%~nf.webp"
)
echo Dönüştürme tamamlandı!
