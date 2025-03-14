liste = ["1","2","5a","10b","abc","10","50"]

# liste elemenları içindeki sadece sayısal değerleri bulma

# for eleman in liste :
#     try:
#         result=int(eleman)
#         print(result)
#     except ValueError:
#         continue


# Kullanıcıdan 'q' değeri girmedikçe aldığınız her inputun sayı olduğundan emin olun eğer değilse hata mesajı yazdırın


# while True:
#     deger=input("sayi: ")
#     if deger =='q' :
#         break
#     try:
#         result=float(deger)
#         print('girdiğiniz sayi : ',deger)
#     except:
#         print('geçersiz sayı')
#         continue

# Girilen parola için türkçe karakter hatası


# def checkPassword(parola):
#     turkce_karakterler ='şçğüöıİ'
#     for i in parola :
#         if i in turkce_karakterler:
#             raise ('Parolanız türkçe karakter içeremez.')
#         else:
#             pass

#     print('geçerli parola')


# parola=input('parola giriniz:')
# try:
#     checkPassword(parola)
# except TypeError:
#     print('Türkçe karakter girdiniz hatalı parola.')







def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer.')
    
    result = 1 

    for i in range(1, x+1):
        result*=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)