file=open("certificate.txt","r")
data=file.read()

data=data.lower()
if "live" in data:
    print("live word present in file")
else:
    print("no live word is not present in file")
file.close()
