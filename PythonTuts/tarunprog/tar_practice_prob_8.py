import random

table = []
correct_table = []


def rohanMultiplication(n):
    for i in range(1, 11):
        table.append(n * i)
    # print(table)
    a = random.randint(1, (len(table)))
    table[a] += 4
    # print(table)
    return table


def isCorrect(r_table, number):
    # correct_table = [i * number for i in range(1, 11)] """This is more python_ic"""
    for i in range(1, 11):
        correct_table.append(number * i)
    for j in range(len(correct_table)):
        if r_table[j] != correct_table[j]:
            print(f"Rohan table is faulty\nFaulty result is {number} * {j+1} = {r_table[j]}")
            print(f"Correct result:- {number} * {j+1} = {number*(j+1)}")
    # if ct_table[i] != r_table[i]:
    #         print("Rohan table is faulty at {table.index(table[i])}\n")
    #         continue
        else:
            continue


if __name__ == '__main__':
    user_input = int(input("Enter number"))
    rohan_table = rohanMultiplication(user_input)
    print(rohan_table)
    isCorrect(rohan_table, user_input)
