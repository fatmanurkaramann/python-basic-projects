numbers=[1,2,3,4]

for num in numbers:
    print(num)

# tuple=[(1,2),(3,4),(5,6)]

# for a,b in tuple:
#     print(a,b)


# numbers=[1,3,5,7,9,12,19,21]
#1 sayılar listesinde hangi sayılar 3ün katıdır
# for num in numbers:
#     if(num%3==0):
#      print(num)


#2 sayıların toplamı

# sum=0
# for num in numbers:
#     sum+=num
# print(sum)

#3 tek sayıların karesi
# for num in numbers:
#     if(num%2!=0):
#      print(num**2)


sehirler=['kocaeli','istanbul','ankara','izmir']
#4 kaç tanesi en fazla 5 karakterlidir

for sehir in sehirler:
   if(len(sehir)<=5):
      print(sehir)



products=[
    {'name':'samsyng s6','price':'3000'},
    {'name':'samsyng s7','price':'4000'},
    {'name':'samsyng s8','price':'5000'},
    {'name':'samsyng s9','price':'6000'},


]
#5 ürünlerin fiyat toplamı
# sum=0
# for product in products:
#   price= int(product['price'])
#   sum+=price
# print(sum)
    


#6 fiyatı en fazla 5000 olan ürünler
for product in products:
  price= int(product['price'])
  if(price<=5000):
    print(product['name'])