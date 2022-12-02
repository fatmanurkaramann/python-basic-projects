#1 ' Hello World ' baş ve sondaki boşlukları siliniz.

x=" Hello World "
x=x.strip()
x=x.rstrip()
print(x)

#2 'www.sadikturan.com' sadikturan dışındakileri sil
website="www.sadikturan.com"
website =website.strip('w.com')
print(website)

#3 'course' küçük yapın
course="Python kursu: Baştan sona python programlama rehberiniz (40 saat)"
course=course.lower()
print(course)

#4 'website' içinde kaç tane a vardır?
website="www.sadikturan.com"
website=website.count("a")
print(website)
#5 'www' ile başlayıp com ile bitiyor mu
website="www.sadikturan.com"
isFound=website.startswith("www")
print(isFound)
isFound2=website.endswith("com")
print(isFound)
#6 website içinde .com var mı
isContain=website.__contains__(".com")
print(isContain)

#7 course içindeki karakterler alfabetik mi
result=course.isalpha()
print(result)
#8 'Contents' ifadesini 50 karakter içine yerleştirip sağına soluna * ekleyiniz.
content="Contents".center(50,"*")
content="Contents".ljust(50,"*") ##sola yaslar
print(content)

#9 course kararter dizisindeki boşluk yerine - ekleyiniz
result=course.replace('','-')
print(result)

#10 "Hello World" karakter dizisinin World ifadesini there ile değiştirin
result='Hello World'.replace('World','There')
print(result)

#11 course karakter dizisini boşluk karakterlerinden ayrın.
result=course.split(" ")
print(result)
