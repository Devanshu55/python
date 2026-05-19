# array >> list in python.
# list >> mutable
# list is a class
# list is collection of different types of data
# list is indexed

friends = ["dev","dipak",5,22.5,True,False,None]
print(friends[-1])
print(friends)
friends[0] = "devanshu"
print(friends)
print(friends[1:6])
friends.append(15.525) #insert value at the end of the list
print(friends)
l1 = [32,13,1,4,2,56,12,2]
l1.sort()
l1.reverse() 
l1.insert(4,"dev") # insert at the middle of the list
l1.pop(3)
l1.remove(32)
print(l1)

l1 = [1,2,3,4,5]
l1.append(30)
print(l1)
