# def square(num):return num**2

numbers=[1,3,5,9,10]

result=list(map(lambda num:num**2,numbers))
print(result)

# def check_even(num):
#     return num%2==0
r=list(filter(lambda num:num%2==0,numbers))
print(r)
