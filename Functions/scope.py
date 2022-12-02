# x= 'global x'
# def function():
#     x="local x"
    
# function()
# print(x)

# name="çınar"

# def changeName(newName):
#     name= newName
#     print(name)
# changeName("Ada")

name="global string"

def greeting(): 
    name="Çınar"
    print(name)
    def hello():
        name="ada"
        print("hello "+name)

    hello()

greeting()


##########3

x=50
def test(x):
    print(f"x+{x}")

    x=100
    print(f"x+{x}")

test(x)
print(x)

