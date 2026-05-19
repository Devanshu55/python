n = int(input("Enter the number:"))
temp = n
lastdigit = 0
while(n>0):
    lastdigit = n%10
    n//=10

   
if temp == lastdigit:
        print("Palindrome")
else:
        print("Not Palindrome")
    
    