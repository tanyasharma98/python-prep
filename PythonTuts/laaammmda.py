#Lambda Function  or anonymous function
# def add(a,b):
#     return a+b
#
# # def minus(x,y):
# #     return x-y
#
# #Lambda funcyion
# minus = lambda x,y: x-y
# print(minus(10,5))


def first_fun(a):
    return a[1]

a=[[1,29],[5,12],[20,4]]
#a.sort(key=first_fun)
a.sort(key=lambda x:x[1]) #lambda function

print(a)