# # class
# class Person:
#     address ='İstanbul'

# # boş class tanımlamak için classın içerisine pass keywordunu yazmak gerekiyor.
#     #contsructor (yapıcı metod)
#     def __init__(self, name, year):

#         # object attributes
#         self.name=name
#         self.year=year
#     # methods
#     def intro(self):
#         print('Hello There I am ' + self.name)

#     def calculateAge(self):
#         return 2024 - self.year


# p1= Person('kaan', year=2005)
# p2= Person('Harun', year=2000)

# p1.intro()

# print(f'My name is: {p1.name} I am {p1.calculateAge()} old')
# print(f'My name is: {p2.name} I am {p2.calculateAge()} old')


class Circle:
    # Class Object Attribute
    pi=3.14 
    

    def __init__(self, yaricap=1):  
        self.yaricap=yaricap

    # methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
x=int(input())
c1= Circle()
c2= Circle(x)

print(f'c1 : Alan= {c1.alan_hesapla()} cevre {c1.cevre_hesapla()}')
print(f'c2 : Alan= {c2.alan_hesapla()} cevre {c2.cevre_hesapla()}')