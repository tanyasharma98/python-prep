mystr= "saikik is a phyco in the world"
#print(len(mystr))
#print(mystr[0:6:3])
#print(mystr[::10])
#print(mystr[-5:-1])
#print(mystr[25:29])
#print(mystr[::-2])
print(mystr.isalnum()) #if we remove spaces then it will show true
print(mystr.isalpha())
print(mystr.endswith("world"))
print(mystr.count("i"))
print(mystr.capitalize())#First letter in string
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is", "are"))
print(mystr.center(100))