#1 gönderilen kelimeyi belirtilen kez ekranda yaz

def myWords(name,adet):
    print(name*adet)

# myWords("merhaba \n",10)

#2 kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonk
def listFunc(*args):
    print(list(args))

listFunc(4343,545,55,4,32,"12",434,"fato")
#3 gönderilen 2 sayı arasındaki tüm asal sayılar


# def primeNum(sayi1,sayi2):
 
#     for sayi in range(sayi1,sayi2+1):
#      if sayi1>1:
#         for i in range(2,sayi):
#             if sayi%i==0:
#                 break
#         else:
#             print(sayi)
# sayi1=int(input("sayi giriniz: "))
# sayi2=int(input("sayi giriniz: "))

# primeNum(sayi1,sayi2)

#4 kendisine gönderilen bir sayının tam bölenlerini liste şeklinde döndürün

sayi=int(input("sayi giriniz: "))

def tamBolen(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if sayi%i==0:
            tamBolenler.append(i)
    return tamBolenler
print(tamBolen(sayi))
