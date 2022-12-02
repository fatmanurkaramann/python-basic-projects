numbers=[x for x in range(10)]
print(numbers)

for x in range(10):
   print(x**2)

numbers=[x**2 for x in range(10) if x%3==0]
print(numbers)


myString= 'Hello'
myList=[]

for letter in myString:
    myList.append(letter)
print(myList)

myList=[letter for letter in myString]
print(myList)

