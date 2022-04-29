# ==============================================Jumbled Funny Names===========================
import random

if __name__ == '__main__':
    friend = int(input("Enter number of your friends"))
    list1 = []
    for i in range(friend):
        list1.append(input("Enter"))
    print(list1)
    first_name = []
    last_name = []
    # Splitting items in list1 individually
    for i in list1:
        name = i.split()
        # For only first & last name
        if len(name) == 2:
            first_name.append(name[0])
            last_name.append(name[1])
        # who has middle name too
        else:
            first_name.append(name[0].__add__(" ").__add__(name[1]))
            last_name.append(name[len(name) - 1])
    for i in range(friend):
        # randomly choosing last name
        a = random.choice(last_name)
        # print(a,"a")
        print(f"{first_name[i]} {a}")
        # removing last name as selected
        last_name.remove(a)
