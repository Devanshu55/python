# dictionary >>
marks = {
   "devanshu" : 56,
   "deva": 60,
"savan" : 70,
"dipak": 80

}
print(marks,type(marks))

print(marks.values())
print(marks.keys())
print(marks.items())
print(marks["deva"]) # this method give error
print(marks.get("dipak")) # this method give none value if wrong key enter
marks.update({"savan" : 79})
marks.pop("devanshu")
print(marks)



