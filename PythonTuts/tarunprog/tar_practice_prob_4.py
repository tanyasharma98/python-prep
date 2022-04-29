"""
author :- Tarun
purpose :- learning
Date :- 31 may 2021
"""
n = int(input("Enter number of test cases"))

for i in range(n):
    number = int(input("Enter no you want to check"))
    nt_number = str(number)

    if nt_number != nt_number[::-1]:
        print(f"Number {number} is not palindrome")

        while nt_number != nt_number[::-1]:
            number = number + 1
            nt_number = str(number)
        print(f"closest palindrome {nt_number}")

    else:
        print(f"Number {number} is palindrome")


#===================================================================================================================
'''Ya Harry ka code he'''
# def nxt_palindrome(n):
#     # n += 1
#     while not is_palindrome(n):
#         n += 1
#     return n
#
#
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
#
# if __name__ == '__main__':
#     n = int(input("Enter number of test case"))
#     numbers = []
#
#     for i in range(n):
#         number = int(input("Enter Number:- "))
#         numbers.append(number)
#
#     for i in range(n):
#         print(f"Next palindrome for {numbers[i]} is {nxt_palindrome(numbers[i])}")
