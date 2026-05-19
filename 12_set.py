f = {"apple" , "banana" , "grapes"}
print(type(f))
print(len(f))

s = {True,"deva",False} # 1 and true && 0 and false are same in  set
print(s)
#set accept only int, str, and boolean datatype
#methods
s.add("apple")
print(s)
s.remove("deva")

# s.discard("apple")
# print(s)
s.add(12)
s.add(34)
s.add(35)
s.add(32)
print(s)
print(s.union(f)) # combine two sets elemnets
print(s.intersection(f)) # give commen elements between two sets



