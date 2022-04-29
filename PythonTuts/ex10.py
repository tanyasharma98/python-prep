# Pickle project
import requests
import pickle

req = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
fog = req.text
# print(type(fog))
gop = fog.split("\n")
print(type(gop))
length = len(gop)
low = [[i] for i in gop]
jup = int(input("Press:1 to write::Press:2 to read"))
file = "ex10.pkl"
if jup == 1:
    fileobj = open(file, "wb")
    pickle.dump(low, fileobj)
    fileobj.close()
elif jup == 2:
    fileobj = open(file, "rb")
    data = pickle.load(fileobj)
    print(data)
    fileobj.close()
