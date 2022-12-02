from datetime import datetime



def sayHello(name="user"):
   return "hello "+name

msg=sayHello("emre")

print(msg)

def total(num1,num2):
    return num1+num2

result=total(10,20)
print(result)

def yasHesapla(birthday):
    return datetime.now().year-birthday
myAge=yasHesapla(2000)
print(myAge)