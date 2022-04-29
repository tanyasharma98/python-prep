# ls = []
#
#
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
# print(ls)

""" List comprehension"""
ls = [i for i in range(100) if i % 3 == 0]
print(ls)

"""Dictionary comprehension"""
# dict_1 = {0 : "Item0" , 1: "Item1"}
dict_1 = {i: f"Item {i}" for i in range(5)}

# dict_1 = {value:key for key,value in dict_1.items()}
dict_2 = {value: key for key, value in dict_1.items()}
print(dict_1)
print(dict_2)

"""Set comprehensions"""
dresses = {dress for dress in ["dress1", "dress2", "dress2", "dress1", "dress2"]}
print(dresses)

"""Generator comprehensions"""

even = (i for i in range(100) if i % 2 == 0)
print(even.__next__())
print(even.__next__())
