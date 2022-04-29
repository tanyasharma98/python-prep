# def funct1():
#     print("Printing Now")
# funt2= funct1
# del funct1
# funt2()

# def  funct1(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
#
# a= funct1(1)
# print(a)

# def executer(func):
#     func("this")
#
# executer(print)


def dec1(func1):
    def nowexe():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexe()
@dec1
def wh0_is_dip():
    print("Tanya Panya")

# wh0_is_dip = dec1(wh0_is_dip)
wh0_is_dip()
