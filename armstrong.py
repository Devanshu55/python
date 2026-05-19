n = int(input("Enter the Numer:"))
num = n
nod = len(str(n))
total = 0
while(n>0):
    lastsigit = n%10
    total=total+(lastsigit**nod)
    n//=10
if total==num:
    print("Armstrong number")
else:
    print("not Armstrong")
