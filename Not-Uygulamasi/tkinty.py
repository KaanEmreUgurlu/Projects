import tkinter as tk
from tkinter import messagebox

# Not hesaplama fonksiyonu
def not_hesapla(satır):
    satır = satır.strip()
    liste = satır.split(":")
    ogrenciBilgi = liste[0]
    notlar = list(map(int, liste[1].split(",")))
    ortalama = sum(notlar) / len(notlar)
    
    if 85 <= ortalama <= 100:
        harf = "AA"
    elif 80 <= ortalama < 85:
        harf = "BA"
    elif 75 <= ortalama < 80:
        harf = "BB"
    elif 70 <= ortalama < 75:
        harf = "CB"
    elif 60 <= ortalama < 70:
        harf = "CC"
    elif 55 <= ortalama < 60:
        harf = "DC"
    elif 50 <= ortalama < 55:
        harf = "DD"
    elif 40 <= ortalama < 50:
        harf = "FD"
    else:
        harf = "FF"
    
    return f"Öğrenci: {ogrenciBilgi}\nOrtalama: {ortalama:.2f}\nHarf Notu: {harf}\n"

# Notları dosyadan oku ve ekrana yazdır
def ortalamalari_oku():
    try:
        with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            for satır in file:
                text_area.insert(tk.END, not_hesapla(satır) + "\n")
    except FileNotFoundError:
        messagebox.showerror("Hata", "Dosya bulunamadı!")

# Yeni öğrenci notu ekle
def not_gir():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    no = no_entry.get()
    
    try:
        not1, not2, not3 = int(not1_entry.get()), int(not2_entry.get()), int(not3_entry.get())
        if not (0 <= not1 <= 100 and 0 <= not2 <= 100 and 0 <= not3 <= 100):
            raise ValueError("Notlar 0-100 arasında olmalıdır.")
        
        with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
            file.write(f"{ad} {soyad} {no}:{not1},{not2},{not3}\n")
        
        messagebox.showinfo("Başarılı", "Notlar başarıyla kaydedildi.")
    except ValueError as e:
        messagebox.showerror("Hata", str(e))

# Öğrenci notunu güncelle
def not_guncelle():
    ogrenci_bilgi = f"{ad_entry.get()} {soyad_entry.get()} {no_entry.get()}"
    
    try:
        with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
            satirlar = file.readlines()
        
        yeni_satirlar = []
        bulundu = False
        for satır in satirlar:
            if satır.startswith(ogrenci_bilgi):
                not1, not2, not3 = int(not1_entry.get()), int(not2_entry.get()), int(not3_entry.get())
                if not (0 <= not1 <= 100 and 0 <= not2 <= 100 and 0 <= not3 <= 100):
                    raise ValueError("Notlar 0-100 arasında olmalıdır.")
                yeni_satirlar.append(f"{ogrenci_bilgi}:{not1},{not2},{not3}\n")
                bulundu = True
            else:
                yeni_satirlar.append(satır)
        
        if not bulundu:
            messagebox.showerror("Hata", "Öğrenci bulunamadı!")
            return
        
        with open("sinav_notlari.txt", "w", encoding="utf-8") as file:
            file.writelines(yeni_satirlar)
        
        messagebox.showinfo("Başarılı", "Not başarıyla güncellendi.")
    except FileNotFoundError:
        messagebox.showerror("Hata", "Dosya bulunamadı!")
    except ValueError as e:
        messagebox.showerror("Hata", str(e))

# Arayüz oluştur
root = tk.Tk()
root.title("Öğrenci Not Sistemi")
root.geometry("500x500")

# Öğrenci bilgileri giriş alanları
tk.Label(root, text="Ad:").pack()
ad_entry = tk.Entry(root)
ad_entry.pack()

tk.Label(root, text="Soyad:").pack()
soyad_entry = tk.Entry(root)
soyad_entry.pack()

tk.Label(root, text="Numara:").pack()
no_entry = tk.Entry(root)
no_entry.pack()

# Not giriş alanları
tk.Label(root, text="1. Not:").pack()
not1_entry = tk.Entry(root)
not1_entry.pack()

tk.Label(root, text="2. Not:").pack()
not2_entry = tk.Entry(root)
not2_entry.pack()

tk.Label(root, text="3. Not:").pack()
not3_entry = tk.Entry(root)
not3_entry.pack()

# İşlem butonları
tk.Button(root, text="Notları Oku", command=ortalamalari_oku).pack()
tk.Button(root, text="Not Ekle", command=not_gir).pack()
tk.Button(root, text="Not Güncelle", command=not_guncelle).pack()

# Sonuçları gösteren alan
text_area = tk.Text(root, height=10, width=50)
text_area.pack()

# Arayüzü başlat
root.mainloop()
