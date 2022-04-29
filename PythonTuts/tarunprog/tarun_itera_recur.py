# def factorial(n):
#     fact=1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact
# n=(int(input("enter num")))
# print(factorial(n))
#logic n* (n-1)!
# def recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n * recursive(n-1)
# n=(int(input("enter num")))
# print(recursive(n))
def febonacci(n):
    if n==1:
         return 1
    elif n==2:
        return 2
    else:
        return febonacci(n-1)+ febonacci(n-2)
n=(int(input("enter num")))
print(febonacci(n))
