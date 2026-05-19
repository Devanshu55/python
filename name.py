# foodlist=("samosa","kachori","dabeli")
# for i in foodlist:
#     print(i)
# print(type(foodlist))
# n = input("enter the name: ")
# for j in range(1,6):
#     print(n.upper())

str = input("enter the String: ")
rev=""
for ch in str:
    rev = ch+rev
print(rev)
    

if(rev==str):
    print("Palindrome")
else:
    print("not Palindrome")
        
        