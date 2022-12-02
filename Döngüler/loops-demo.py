#1-100 arasında rastgele üretilece sayıyı aşağı yukarı ifadelerle buldurun
#100 üzerinden puanlama yapın her soru 20 puan

import random;
num=random.randint(1,10)
can=int(input('kaç hak kullanmak istersiniz: '))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmin: '))

    if num==tahmin:
        print(f"tebrikler {sayac}.defada bildiniz.Puanınız:{100-(20)*(sayac-1)}")
        break
    elif num>tahmin and hak>0:
        print('yukarı')
    elif num<tahmin and hak>0:
        print('aşağı')
    elif hak==0:
        print(f"hakkınız bitti. sayı: {num}")