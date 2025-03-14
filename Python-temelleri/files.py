# dosya açmak veya oluşturmak için open() fonksiyonu kullanılır
# kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hanagi amaçla açtığımızı belirtir

# "w" write (yazma) modu. Dosyayı konumda oluşturur.
# *dosyayı konumda oluşturur
# * dosyanın içeriğini siler ve yeniden ekleme yapar


# file.close()

file = open("newfile.txt","w",encoding="utf-8")
file.write("Kaan Emre Uğurlu\nRamazan Uğurlu\nFatma Uğurlu\nHarun Uğurlu")

file.close()






# "a" append ekleme dosya konumda yoksa oluşturur

# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nKaan Uğurlu")
# file.close()



# "x" create oluşturma dosya zaten varsa hata verir

# file = open("updating.py","x", encoding="utf-8")
# print(file)

# "r" read okuma varsayılan dosya konumda yoksa hata verir.