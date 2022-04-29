f= open("tanya.txt")
f.seek(8)
#print(f.tell()) Tell position
print(f.readline())
#if want to read it again , use seek wherever you want
f.seek(4)
#print(f.tell())
print(f.readline())
#print(f.tell())
f.close()