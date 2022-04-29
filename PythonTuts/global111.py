# l=50#global
# def gol():
#     n=5 #local
#     global l
#     l=10
#     print(l)
#     print(n,"This is local for now")
# gol()
# print(l)
x=40
def tanya():
    x=100
    def fog():
       # global x
        x=20
    print("before calling function",x)
    fog()
    print("after calling function",x)
tanya()
print(x)#20 ,as global waS dfined