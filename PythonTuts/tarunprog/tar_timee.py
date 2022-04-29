
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("Enter 1 for excercise 2 for food"))
        if c == 1:
            data = input("enter text")
            with open("harry.txt", 'a') as f:
                f.write(str(gettime()) + data)
            print("data enter sucessfully")
        elif c == 2:
            data = input("enter food")
            with open("harry.txt", 'a') as f:
                f.write(str(gettime()) + data)
            print("data enter sucessfully")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for excercise 2 for food"))
        if c == 1:
            with open("harry.txt") as f:
                f.read()
            print("data enter sucessfully")
        elif c == 2:
            data = input("enter food")
            with open("harry.txt", 'a') as f:
                f.write(str(gettime()) + data)
            print("data enter sucessfully")


s = int(input("what you wnat to do 1:- type\n 2:-see\n"))
k = int(input("please press 1:- harry \n 2:- rohan\n,3:-hammad\n"))

if s == 1:
    take(k)
elif s == 2:
    retrieve(k)
else:
    print("invalid")
a = 6
b = 9
a = a+b
b = a-b
a = a-b
dict = {"sir": " jii ", 420: "ydg"}
dict.update({23: 84})
del dict[420]
# dict["sir"]
# print(dict)
d = dict.copy()
d.update({"harrry": " yo yo", "js": "code"})
# del dict
print(dict.values())
print(d)
print(a, b)
