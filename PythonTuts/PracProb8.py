# =========================================== Pil Fraud!!!Multiplication Table=======================================
import random


def pilMultiplication(n):
    random_number = random.randint(1, 10)
    list1 = []

    for i in range(1, 10):
        if i == random_number:
            fraud = i * n
            fraud += 2
            list1.append(fraud)
        else:
            i = i * n
            list1.append(i)
    return list1


def isCorrect(output, n):
    list2 = []
    for i in range(1, 11):
        i = i * n
        list2.append(i)
    print(f"Fraud output:{output}\n")
    print(f"Correct output:{list2}\n")
    for i in range(len(list2)):
        if int(list2[i]) != int(output[i]):
            print("Fraud caught")
            print(f"At position {i + 1}:{output[i]}")
            return f"It should be:{list2[i]}"


if __name__ == '__main__':
    num = int(input("Enter the number to get Multiplication Table\n"))
    mul = pilMultiplication(num)
    print(mul)
    inp = print(isCorrect(mul, num)) if input("Enter any key to check") else print("It's up to You")
    # print(isCorrect(mul, num))
