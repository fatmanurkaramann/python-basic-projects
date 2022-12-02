#inheritance(kslıtım)

class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("person created")
    def who_am_i(self):
        print("I am a person")
    def eat(self):
        print("I am eating")
        
class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch=branch
    def who_am_i(self):
        print(f"ı am {self.branch} teacher")

class Student(Person):
     def __init__(self,fname,lname,number):
        super().__init__(fname, lname)
        self.number=number
        print("Student created")
    #override
     def who_am_i(self):
        print("ı am student")


p1=Person("ali","yılmaz")
s2=Student("ayşe","turan",2232)
t1=Teacher("Fatma","Karaman","Matematik")
t1.who_am_i()

print(f"{s2.firstname}  {s2.lastname} {s2.number}")
print(t1.firstname)
s2.eat()
p1.who_am_i()
s2.who_am_i()