x,y,z=2,5,107

numbers=1,5,7,10,6

#1 kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkı
a=input('sayi giriniz:')
b=input('sayi giriniz:')
carpim=int(a)*int(b)
sum=x+y+z
fark=carpim-sum
print(fark)

#2 ynin xe kalansız bölümünü hesaplayınız
print(y//x)

#3 (x,y,z) toplamının mod3 ü nedir
sum=x+y+z
print(sum%3)

#4 ynin x. kuvveti
print(y**x)

#5 x,*y,z=numbers işlemine göre znin küpü nedir
x,*y,z=numbers
print(z**3)

#6 x,*y,z=numbers işlemine göre ynin değerleri toplamı
print(y[0]+y[1]+y[2]) 





