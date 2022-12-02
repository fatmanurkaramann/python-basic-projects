#elimizde liste yoksa whil döngüsü


# x=0
# while x<10:
#     if(x%2==0):
#        print(x)
#     x+=1

# name='' #false
# while not name.strip():
#     name=input('isminizi giriniz')  
#     print(f'merhaba,{name}')



from logging import lastResort
from unicodedata import name


numbers=[1,3,5,7,9,12,19,21]

#1 syıları while ile yazdır
# i=0
# while (i<len(numbers)):
#     print(numbers[i])
#     i+=1

#2 başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tek sayıları ekrana yazdır

# first=int(input('first: '))
# last=int(input('last: '))

# i=first
# while i<last:
#     i+=1
#     if(i%2!=0):
#      print(i)

#3 1-100 arasındaki sayıları azalan şekilde yazdır

# x=100
# while x>=1:
#     print(x)
#     x-=1

#4kullanıcıdan alınıan 5 sayıyı sıralı olarak ekrana yazdır
# numbers=[]
# i=0
# while i<5:
#    num= int(input('sayi '))
#    numbers.append(num)
#    i+=1
#    numbers.sort()
#    print(numbers)

#5 kullanıcıdan alınan ürün bilgisini liste içinde sakla
# name price seklinde olsun
products=[]
adet=int(input('adet: '))
i=0
while i<adet:
     name=input('name: ')
     price=input('price: ')
     products.append(
        {
            'name':name,
            'price':price
        }
     )
     i+=1

     for urun in products:
        print(urun)