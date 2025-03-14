maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# Değiken Tanımlama Kuralları

# rakam ile başlayamaz

# Büyük küçük harf duyarlılığı vardır.

age = 20 
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanılmayalım

x = 1               #int
y = 2.3             #float
name = "Çınar"      #string
isStudent = True    #bool

# x, y, name, isStudent = (1, 2, "Çınar", True)

a = 10
b = 20
print(a+b) # ==> 30

a = '10'
b = '20'
print(a+b) # ==> 1020

firstName = 'Kaan'
lastName = ' Uğurlu'

print(firstName+lastName)