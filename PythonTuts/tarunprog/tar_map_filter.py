# num  = ["3","4","5","6","7"]
# num = list(map(int,num))
# print(num)
num = [3, 4, 5, 6, 7, 8, 9]


def square(a):
    return a * a


def cube(a):
    return a * a * a


func = [square, cube]
for i in range(8):
    num = list(map(lambda x: x(i), func))
    print(num)

# ------------------------------------filter-------------------------------------------------------------
number = [3, 4, 5, 6, 7, 8, 9]


def greater_than_5(num):
    return num > 5


number_greater_5 = list(filter(greater_than_5, number))
print(number_greater_5)

# ------------------------------------reduce-------------------------------------------------------------
from functools import reduce

list = [3, 4, 5, 6, 7, 8, 9]
num = reduce(lambda x, y: x + y, list)
print(num)
