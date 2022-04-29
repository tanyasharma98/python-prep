"""
Author :- Tarun sharma
Date :- 1 june 2021
Purpose :- Learning
"""


def palindrome(num):
    """
    function to get next palindrome
    """
    while str(num) != str(num)[::-1]:
        num += 1
    return num


if __name__ == '__main__':
    # Number of test case
    n = int(input("Enter number of test case\n"))
    lst = []

    for i in range(n):
        # Take numbers input from user and Append number in list of number
        number = int(input("Enter numbers\n"))
        lst.append(number)

    for j in range(n):
        if lst[j] > 10:
            print(f"Next palindrome of {lst[j]} is {palindrome(lst[j])}")
        else:
            print(f"your number {lst[j]} is like you cheap Product")
