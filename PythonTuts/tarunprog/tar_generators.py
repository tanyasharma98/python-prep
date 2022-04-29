"""
iterable  - __iter__() or __getitem__()
iterator - __next__()
iterfateiodn -

"""


# def gen(n):
#     for i in range(n):
#         yield i
#
# g = gen(3)
# a = g.__iter__()
# print(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# for i in g:
#     print(i)
#     print('hr')

# t = "tarun"
# iter = t.__iter__()
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
def factorial(fac):
    for i in range(1 , fac):
        print(fac)
        fac = fac *i
    yield fac
g = factorial(int(input()))

print(g.__next__())
# print(g.__next__())
def fabo():
    pass
