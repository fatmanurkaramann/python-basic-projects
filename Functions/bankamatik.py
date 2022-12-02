#Bankamatik uygulaması

SadikHesap={
    'ad':'Sadık',
    'hesap no':'124343',
    'bakiye':3000,
    'ekhesap':2000
}
AliHesap={
    'ad':'Ali',
    'hesap no':'124343',
    'bakiye':2000,
    'ekhesap':2000
}
def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        print("paranızı alabilrisiniz")
    else:
        toplam=hesap['bakiye']+hesap['ekhesap']
        if toplam>=miktar:
            ekHesapKullanımı=input("ek hesap kullanılsın mı(e/h)")
            if ekHesapKullanımı=="e":
                ekHesapMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap']-=ekHesapMiktar
                print("paranızı alın")
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")

        else:
            print("bakiye yetersiz")

paraCek(SadikHesap,3000)
paraCek(SadikHesap,2000)
paraCek(SadikHesap,2000)

