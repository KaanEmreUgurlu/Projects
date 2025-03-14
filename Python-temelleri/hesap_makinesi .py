print('Lütfen 2 sayı giriniz:')
sayi1= float(input('Lütfen 1.sayıyı girin:'))
sayi2= float(input('Lütfen 2.sayıyı giriniz:'))
islem=input('Lütfen bir işlem seçiniz[+,-,*,/]')

if islem == "+":
    sonuc = sayi1 + sayi2
    print(sonuc)
if islem == "-":
    sonuc = sayi1 - sayi2
    print(sonuc)
if islem == "*":
    sonuc = sayi1 * sayi2
    print(sonuc)
if islem == "/":
    sonuc = sayi1 / sayi2
    print(sonuc)
else :
    print('olmayan bir işlem seçtiniz tekrar deneyiniz.')

    
