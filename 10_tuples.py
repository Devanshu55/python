#tuples >> immutable 
# never change original tuple
# tuple is a class

#declaration
a = (2,3,1,4,4,3,5)

# print(type(a))
# print(a)
b = (1,) #only one element in tuple
c = (1,23.5,"deva",True)
print(c)
no = a.count(4) #count the element in tuple
print(no)
i = a.index(4)
print(i)
multiply = c*3 #same tuple print multiple times
print(multiply)
check = ("deva" in c) #check the element present in tuples
print(check)
