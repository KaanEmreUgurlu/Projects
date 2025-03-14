# Inheritance (Kalıtım):Miras alma

#Person => name, lastname, age , eat(), run (), drink() Her seferinde tek tek student ve teachera tanımlamaktansa miras almasını sağlıyoruz
#Student(Persondan) , Teacher(Person)

#Animal => Dog(Animal),   Cat(Animal) #Animale daa önceden eklediğimiz özellikleri daha sonra tekrar eklememie gerek kalmadan miras olarak aktarıyoz.


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print('Student Created')

Name1=input('Bir isim giriniz: ')
Surname1= input('Bir soyisim giriniz: ')
Name2=input('Bir isim giriniz: ')
Surname2= input('Bir soyisim giriniz: ')


p1 = Person(Name1,Surname1)
s1 = Student(Name2, Surname2)
print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)