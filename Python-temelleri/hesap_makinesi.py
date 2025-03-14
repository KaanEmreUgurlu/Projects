print('Lütfen 2 sayı giriniz')
sayi1 = float(input('Lütfen 1. sayıyı girin:'))
sayi2 = float(input('Lütfen 2. sayıyı giriniz:'))
islem = input('Lütfen bir işlem seçiniz [+,-,*,/]: ')

if islem == "+":
    sonuc = sayi1 + sayi2
    print(sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print(sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print(sonuc)
elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print(sonuc)
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
else:
    print('Geçerli bir işlem seçmediniz, tekrar deneyiniz.')
