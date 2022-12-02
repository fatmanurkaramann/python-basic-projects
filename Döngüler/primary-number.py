sayi=int(input("sayi giriniz: "))

if sayi==1:
    print("asal değildir")
if sayi==2:
    print("asal")

for i in range(2,sayi):
    if sayi%i==0:
        print("asal değildir")
        break
    else:
        print("asaldır")
        break