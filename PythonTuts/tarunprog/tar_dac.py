# def function():
#     print("yo yo")
# func2=function
# del function
# func2()
# del func2
# def function():
#     print("tanik")
# func2 =function
# def function(fun):
#     fun()
# function(sum)
def dec1(funct):
    def noexe():
        print("executing")
        funct()
        print("Executed")
    return noexe
@dec1 ###decorator
def who_is_harry():
    print("yo yoyo oyh")
# who_is_harry =dec1(who_is_harry)
who_is_harry()