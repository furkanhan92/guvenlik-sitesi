from PIL import Image
import os

# Resimlerin bulunduğu klasör
input_folder = "D:/images"
output_folder = "D:/images/webp"

# Çıktı klasörünü oluştur
os.makedirs(output_folder, exist_ok=True)

# Klasördeki tüm dosyaları al
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)
    
    # Sadece resim dosyalarını işleyelim
    if file_name.lower().endswith(("png", "jpg", "jpeg")):
        img = Image.open(file_path)
        
        # Yeni dosya adı
        new_file_name = os.path.splitext(file_name)[0] + ".webp"
        new_file_path = os.path.join(output_folder, new_file_name)
        
        # WebP olarak kaydet
        img.save(new_file_path, "WEBP", quality=80)
        print(f"✅ {file_name} → {new_file_name}")

print("\n🎉 Tüm resimler WebP formatına dönüştürüldü!")
