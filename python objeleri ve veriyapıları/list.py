 #1 "Bmw,mercedes,opel,mazda" elemanlarına sahip liste oluşturunuz
cars=["Bmw","mercedes","opel","mazda"]

 #2 liste kaç elemanlıdır
len=len(cars)
print(len)

 #3 listenin ilk ve son elemanı
print(cars[0])
print(cars[len-1])

 # 4 mazda değerini toyota ile değiştrin
cars[-1]="toyota"
result=cars
print(result)

 # 5 mercedes listenin bir elemanı mıdır
result= "mercedes" in cars
print(result)

 # 6 listenin -2 indeksindeki değer nedir
print(cars[-2])

 # 7 listenin ilk 3 elemanını alın.
print(cars[:3])

 # 8 listenin son iki elemanı yerine toyota ve renault ekleyin
cars[3]="renault"
cars[2]="toyota"
print(cars)
 # 9 listenin üzerine audi ve nissan değerlerini ekleyin
r=cars+["audi","nissan"]
print(r)

 # 10 listenin son elemanını silin
del cars[-1]
result=cars
print(result)

 # 11 liste elemanlarını tersten yazdırın
result=cars[::-1]
print(result)

 # 12 Aaşağıdaki verileri liste içinde saklayınız
 # studentA:Yiğit Bilgi 2010,(70,60,70)
 # studentB:Sena Bilgi 1999,(80,80,70)
 #  studentC:Ahmet turan 1998,(80,70,90)
studentA=["Yiğit Bilgi",2010,[70,60,70]]
studentB=["Sena Bilgi", 1999,[80,80,70]]
studentC=["Ahmet turan", 1998,[80,70,90]]

 #liste elemanlarını ekrana yazdırınız
result=studentA[0]
result=studentB[0]
print(result)