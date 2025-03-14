# sayilar=[1,3,5,7,9,12,19,21]
# a=0
# while (a<len(sayilar)):
#     print (sayilar[a])
#     a+=1




# baslangic= int(input("başlangıç sayısını yazınız:"))
# bitis = int(input("bitis sayısını yazınız: "))
# x= baslangic
# while (x<=bitis):
#     if x%2==1:
#         print(x)
#     x+=1

# x=100
# while(x>=0):
#     print(x)
#     x = x-1



# import random
# a= random.randint(0,100)
# hak = 5
# x = int(input("Sayıyı tahmin ediniz:"))
# while hak >=0:
#     hak-=1


#     if x==a:
#         print("Doğru tahmin ettiniz tebrikler")
#         break
#     elif x>a:
#         print("Tahminininiz sayıdan büyük tekrar deneyiniz:")
#         x = int(input("Sayıyı tekrar tahmin ediniz:"))
#     else:
#         print("Tahmininiz sayıdan küçük tekrar deneyiniz:")
#         x = int(input("Sayıyı tekrar tahmin ediniz:"))


#     if hak==0:
#         print(f"Hakkınız bitti sayınız:{a}")


# dogumyili= int(input("Doğum yılınızı giriniz:"))
# isim = str(input("İsminizi girin="))
# yas = (2023-dogumyili)

# print(f"İsminiz:{isim}")
# print(f"Yaşınız:{yas}")


# def change(n):
#     n[0] = "istanbul"

# sehirler =["ankara","izmir"]
# n= sehirler[:] #slicing işlemi listeyi kopyalayıp yeni bir liste oluşturdu ve bu yeni listeyi n değişkeni içerisine tanımladı

# n[0] ="istanbul"
# print(sehirler)
# print(n)

# def add(a,b):
#     return sum((a,b))

# print(add(10,20))




square = lambda num: num**2
numbers = [1,3,5,9]
x = int(input("bir x değeri giriniz:"))
result = square(x)
print(result)
