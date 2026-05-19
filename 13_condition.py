#  if/elif/else  >>

# a = int(input("enter your age : "))
# if(a>18):
#     print("your age is above 18.")
# elif(a==18):print("your age is 18.")
# else:
#     print("yor age is below 18.")

# n1 = int(input("enter the number1 :"))
# n2 = int(input("enter the number2 :"))
# if(n1>n2):print(n1," is greater.")
# elif(n1==n2):print("both are equal")
# else:print(n2,"is greater")

# s1 = int(input("enter the side1 :"))
# s2 = int(input("enter the side2 :"))
# s3 = int(input("enter the side3 :"))

# sum = s1+s2
# if(sum>s3):print("valid triengle")
# else:print("invalid triengle!")


n2 = float(input("enter any number : "))
n1 = float(input("enter any number : "))
op = input("enter operetor (+,-,*,/) : ")

if(op == '+'):
    result = n1 + n2
    print("Result : ",result)

elif(op == '-'):
    result = n1 - n2
    print("Result : ",result)

elif(op == '*'):
    result = n1 * n2
    print("Result : ",result)

elif(op == '/' and n2!=0):
    result = n1 / n2
    print("Result : ",result)

    
    



