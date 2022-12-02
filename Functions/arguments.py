def changeName(n):
    n='ada'

name='yiğit' 
changeName(name)
print(name)


def change(n):
    n[0]="istanbul"
sehirler=["ankara","izmir"]
change(sehirler)
print(sehirler)

# def add(*params):
#     return sum((params))

# print(add(10,20))
# print(add(10,20,50,90))
# print(add(10,20,36,78,90,8,78))
def displayUser(**params):
    for key,value in params.items():
        print("my {} is {}".format(key,value))

displayUser(name="çınar",age=2,city="istanbul")
displayUser(name="Ada",age=6,city="istanbul",phone="32442")


def myFunc(a,b,*args,**kwargs):
        print(a)
        print(b)
        print(args)
        print(kwargs)


myFunc(10,34,56,54,51,key1="value1",key2="value2")

