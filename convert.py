import os
from PIL import Image

# Resimlerin bulunduğu klasör
input_folder = r"D:\guvenlik-sitesi\images"
output_folder = r"D:\guvenlik-sitesi\images\webp"

# Eğer output klasörü yoksa, oluşturuluyor
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# input klasöründeki dosyaları kontrol et
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Dosya yolunu al
        file_path = os.path.join(input_folder, filename)
        
        # Görseli aç ve WebP formatına dönüştür
        with Image.open(file_path) as img:
            # Çıktı dosyasının yolu
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            # WebP olarak kaydet
            img.save(output_path, "WEBP")

print("Tüm resimler WebP formatına dönüştürüldü!")
