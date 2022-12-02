#1 'course="Python kursu: Baştan sona python programlama rehberiniz (40 saat)" karakter dizisinde kaç tane karakter bulunmaktadır.'



course="Python kursu: Baştan sona python programlama rehberiniz (40 saat)"
length=len(course)
print(length)

#2- website="http:/wwww.sadikturan.com" www karakterlerini alın

website="http:/wwww.sadikturan.com"
print(website[6:9])

#3- website içinden com karakterini alın
lenth2=len(website)
print(lenth2)
print(website[lenth2-3:lenth2])

#4 course içinden ilk 15 ve son 15 karakterlerini alın

print(course[:15])
print(course[-15:])


#5 course tersten yazdırın
result=course[::-1]
print(result)

#6 hello world ifadesindeki w harfini W ile değiştiin
x="hello world"
# x=x[0:6] + 'W'+ x[-4:]
x=x.replace("w","W")
print(x)
#7 "abc" ifadesini yanyana 3 kere yazdırın
string="abc "
print(string*3)