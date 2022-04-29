# a=9
# b=6
# c= sum((a,b))
# print(c)


def function1(a,b):
    print("This is a function",a+b )
#print(function1())   shows none

def function2(a,b):
    """This is a doctstring of function who gives average"""
    average= (a+b)/2
 #   print(average)
    return average

v =function2(4,5)
#print(v)
print(function2.__doc__)