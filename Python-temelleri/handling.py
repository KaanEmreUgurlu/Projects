# error handling => hata yönetimi

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError)as e :
#     print('yanlış bir değer girdiniz.')
#     print(e)


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except :
#     print('yanlış bir değer girdiniz.')
# else :
#     print('Herşey yolunda')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bir değer girdiniz.', ex )
    else :
        break
    finally:
        print('try except sonlandı.')

