# f = open("tanya.txt", "rt" )
# f.read(10)
# f.close()
with open("tanya.txt") as f:
    a = f.readlines()
    print(a)


