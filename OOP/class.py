#class

# class Person:
#     #class attributes
#     print("hello")
#     address="ist"
#     #constructor(yapıcı method)
#     def __init__(self,name,year):
#     #object attributes
#         self.name=name
#         self.year=year
#         print("init metod calısti")
#     #instance methods
#     def intro(self):
#         print("hellooo "+self.name)
#     #instance methods
#     def calculateAge(self):
#         return 2021-self.year
# #object(instance)
# p1 = Person("ali",12)
# p2=Person("fato",21)
# p1.intro()
# p2.intro()
# print(p1.calculateAge())
# #updating
# p1.name="ahmet"

# print(p1.name)
# print(p1.address)

#objeler üzerinden bütün attributelere ulaşılabilir class veya method seviyesinde olması fark etmez




class Circle():
    #class object attribute
    pi=3.14
    #constructur
    def __init__(self,yaricap=1) :
        self.yaricap=yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)


c1=Circle()
c2=Circle(5)

print(c1.alan_hesapla())
print(c2.alan_hesapla())


