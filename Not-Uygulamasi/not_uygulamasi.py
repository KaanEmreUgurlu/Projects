def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(":")
 

    ogrenciBilgi = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama =(not1+not2+not3)/3

    if ortalama >=85 and ortalama <=100 :
        harf="AA"
    elif ortalama >=80 and ortalama <=85 :
        harf="BA"
    elif ortalama >=75 and ortalama <=80 :
        harf="BB"
    elif ortalama >=70 and ortalama <=75 :
        harf="CB"    
    elif ortalama >=60 and ortalama <=70 :
        harf="CC"
    elif ortalama >=55 and ortalama <=60 :
        harf="DC"
    elif ortalama >=50 and ortalama <=55 :
        harf="DD"
    elif ortalama >=40 and ortalama <=50 :
        harf="FD"
    else :
        harf='FF'

    return f"Öğrenci: {ogrenciBilgi} \nOrtalama: {str(ortalama)} \nHarf Notu:   {harf}  \n"
    

    
def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satır in file:
            print(not_hesapla(satır))


def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    no = input("Öğrenci Numarası: ")

    while True:
        try:
            not1 = int(input("1.Not: "))
            not2 = int(input("2.Not: "))
            not3 = int(input("3.Not: "))
            if not(0<= not1 <=100 and 0<= not2 <=100 and 0<= not3 <=100 ):
                raise ValueError("Notlar 0-100 arasında olmalıdır.")
            break
        except ValueError as e :
            print(f"Hatalı giriş: {e}, lütfen tekrar girin.")


    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(f"{ad} {soyad} {no}:{not1},{not2},{not3}\n" )

    print("Notlar başarıyla girildi.\n")


def not_guncelle():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        satirlar=file.readlines()

    if not satirlar:
        print("\n kayıtlı öğrenci bulunmamaktadır")
        return
    

    print("\n Kayıtlı Öğrenciler:")
    for satir in satirlar:
        print("-", satir.split(":"[0]))

    ogrenci_bilgi = input("Notunu değiştirmek istediğiniz öğrencinin adını,soyadını ve numarasını giriniz.\n")

    yeni_satirlar =[]
    bulundu = False

    for i in satirlar:
        ogrenci_kaydi = i.split(":")[0].strip()
        if ogrenci_kaydi == ogrenci_bilgi:
            print(f"\nMevcut Kayıt: {i.strip()}")

            try:
                not1 = int(input("Yeni 1.Not:"))
                not2 = int(input("Yeni 2.Not:"))
                not3 = int(input("Yeni 3.Not:"))


                if not(0<= not1 <=100 and 0<= not2 <=100 and 0<= not3 <=100 ):
                    raise ValueError("Notlar 0-100 arasında olmalıdır.")
                
                yeni_satir = f"{ogrenci_bilgi}:{not1},{not2},{not3}\n"
                yeni_satirlar.append(yeni_satir)
                bulundu = True
            except ValueError as e :
                print(f"Hata {e}. Güncelleme iptal edildi.")
                return
        else:
            yeni_satirlar.append(i)

    if not bulundu:
        print("Öğrenci bulunamadı veya bilgiler yanlış girildi.")
        return
    
    
    with open("sinav_notlari.txt","w",encoding="utf-8") as file:
        file.writelines(yeni_satirlar)

    print("\n Notlar başarıyla güncellendi.")


def not_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []
        
        for i in file:
            liste.append(not_hesapla(i))
        
    with open("sonuclar.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)


def menu():
    while True:
        islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Not Güncelle\n5- Çıkış\n\n")
        if islem == "1":
            ortalamalari_oku()
        elif islem =="2":
            not_gir()
        elif islem =="3":
            not_kaydet()
            print("Notlar başarıyla kaydedildi.\n")
        elif islem =="4":
            not_guncelle()
        elif islem =="5":
            print("Sistemden çıkış yapılıyor.")
            break
        else :
            print("Hatalı tuşlama yaptınız lütfen 1 ve 5 arasında bir tuşlama yapınız.")
            input("Devam etmek için herhangi bir tuşa basın")

menu()