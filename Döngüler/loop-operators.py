# list=[1,2,3]

# for item in range(3,10,2):
#     print(item)

# enumerate

# greeting='hello'
# for i,letter in enumerate(greeting) :
#     print(f'i: {i} {letter}' )

#zip
list1=[1,2,3,4]
list2=['a','b','c']

print(list(zip(list1,list2)))

for i1,i2 in zip(list1,list2):
    print(i1,i2)