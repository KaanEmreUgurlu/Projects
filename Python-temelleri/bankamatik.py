# bankamatik uygulaması

KaanHesap = {
    "ad":"Kaan Emre Uğurlu",    
    "hesapNo": "4205312",
    "bakiye": 5000 ,
    "ekHesap": 3000
}

HarunHesap = {
    "ad":"Harun Uğurlu",
    "hesapNo": "3124205",
    "bakiye": 7000,
    "ekHesap": 2000
}

def paraCekme(hesap,miktar) :
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz")
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]
        if toplam >= miktar :
            
            ekHesapkullanımı=input("bakiyeniz yetmediği için ek hesaptan para alınması gerekiyor ek hesaptan para alınsın mı? e/h\n")
            if (ekHesapkullanımı == 'e'):
                ekHesaptanKullanılcakmiktar= miktar - hesap['bakiye']
                hesap["bakiye"]=0
                hesap["ekHesap"] -= ekHesaptanKullanılcakmiktar

                print("ek hesaptan para kullanıldı paranızı alabilirsiniz")
            elif (ekHesapkullanımı == 'h'):
                print("ek hesaptan harcamadığınız için istediğiniz miktarı çekemiyorsunuz.")
            else:
                print("yanlış tuşlama yaptınız")
        elif toplam < miktar :
            print("hesap bakiyeniz ve ek hesap limitinizin üstünde bir para istediğinizi için veremiyoruz")
    

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesaptan kullanılabilecek miktar ise {hesap['ekHesap']} TL kadardır.")


paraCekme(KaanHesap,3000)
bakiyeSorgula(KaanHesap)

print("----------------")
paraCekme(KaanHesap,4000)
bakiyeSorgula(KaanHesap)

