#1 girilen sayının 0-100 arasında olup olmadığını kontrol ediniz
number=float(input("number: "))
# result=(number>0) and (number<=100)
# print(result)

#2girilen sayı pozitif çift satı mıdır

if((number%2==0) and (number>0)):
    print(str(number)+" çift sayı")
else:
    print("tek sayıdır")
