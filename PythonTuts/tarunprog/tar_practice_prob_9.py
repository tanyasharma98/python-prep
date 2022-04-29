import random

num = int(input("Enter number of your friend\n"))
lst1 = []
lst2 = []
sur_name = []
for i in range(num):
    names = list(input("Enter your name\n").split(" "))
    lst1.append(names[0])
    lst2.append(names[1:])


# print(lst2)
# for i in range(len(lst1)):
# for name in lst2:
#     # print(name[0:])
#     print(f"{lst1[random.randint(0,len(lst1))]} {name[0:]}")
    #     print(f"{lst1[i]} {lst2[random.randint(0,len(lst2))]}")

for i in lst2:
    # ''.join(i for i in i.split(','))

    # var = str(i)
    # print(var)
    # print(f"i {str(i)}")
    # sur = str(i).replace('',"").replace(",", "")
    # print(f"i {sur}")

    for j in i:
        # print(f"j {j}")
        sur = j.replace(",", "")
        # print(sur)
        print(f"{lst1[random.randint(0,len(lst1))]} {sur}")
    # sub = [j.replace(",", "") for j in i]

    # print(sur_name)
#     for j in i:
#         # sur_name.append(" ".join())
#     # print(sur_name)
# for i in range(len(lst1)):
    # print(f"{lst1[random.randint(0,len(lst1))]} {sur_name[0:]}")
    # print(f"{lst1[i]} {sur_name[random.randint(0,len(sur_name))]} {sur_name[random.randint(0,len(sur_name))]}")
