


names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#1 cenk ismini listenin sonuna ekleyin
names.append('Csenk')
print(names)
#2 sena değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)

#3 deniz isimini siliniz
# names.remove('Deniz')
# print(names)

#4 deniz isminin indeksi
i=names.index("Deniz")
print(i)

#5 ali listenin elemanı mıdır
result= "Ali" in names
print(result)

#6 liste elemanlarını ters çevirin
names.reverse()
print(names)
#7 liste elemanlarını alfabetik sırala
names.sort()
print(names)

#8 years istesini rakamsal büyüklüğe göre sırala 
years.sort()
print(years)

#9 str="chevrolet,dacia" listeye çevir
str="chevrolet,dacia"
result=str.split(',')
print(result)
#10 years min max eleamanı
val=min(years)
val=max(years)

print(val)
#11 years dizisinde kaç tane 1998 elemanı vardır
y=years.count(1998)
print(y)
#12 years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)
#13 kullanıcıdan alacağınız 3 tane markayı listede saklayınız
a=input("1.marka:")
b=input("2.marka:")
c=input("3.marka:")
list=[a,b,c]
print(list)
