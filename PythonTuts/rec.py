# # def print2(str1):
# #    # print2(str1)#recurssion --- cuz it never stop
# #     print("This is "+ str1)
# # print2("Tanya")
# def factorial_iterative(n):
#     fac=1
#     for i in range(n):
#         fac = fac *(i+1)
#     return fac
#     # """
#     # :param n:  INteger
#     # :return:  n * n-1 * n-2 * n-3-----------1
#     # """
#
#
#
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# # 5* factorial_recursive(4)
# # 5* 4 * factorial_recursive(3)
# # 5* 4 * 3 *factorial_recursive(2)
# # 5* 4 * 3 * 2*1=120
#
# num= int(input("Enter the number"))
# print("Factorial using iterative method",factorial_iterative(num))
# print("Factorial using iterative method",factorial_recursive(num))



#FIBONNACI SERIES
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)

num = int(input("Enter Your  fibonnaci number"))
print(fibo(num))