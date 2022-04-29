# def function(a,b):
#     print("hello",a+b)
# function(10,20)

def function1(a, b):
    """"this function calculate average of two number"""

    average = (a+b)/2
    return average


v = function1(100, 200)
print(v)
print(function1.__doc__)
