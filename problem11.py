n = int(input("enter the number : "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

l = ["savann","sachin","deva","savri"]
for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")

n = int(input("enter the number : "))
i =1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1