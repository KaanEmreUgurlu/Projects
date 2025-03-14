# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya mevcut değil")
# finally:
#     print("dosya kapandı.")
#     file.close()


# file = open("newfile.txt","r",encoding="utf-8")

# # for döngüsü

# # for i in file:
# #     print(i, end="")

# # read() fonkisyonu

# content1 =file.read()

# print("içerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding="utf-8")

# content2 =file.read()

# print("içerik 2")
# print(content2)

file = open("newfile.txt","r",encoding="utf-8")


# content= file.read(5)
# content= file.read(3)
# content= file.read(4)


# print(content)

# ***readline() fonksiyonu
# her seferinde bir satırı okur

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

# ****readlines fonkisyonu

liste = file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])



 
file.close()
