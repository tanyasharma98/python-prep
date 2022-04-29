"""------------------------------Palindromify the List-------------------------"""
"""
    Author: Tanya Sharma
    Date: 31st May,2021
    Purpose: Practice Problem 5 #CWH
    
"""


def palindrome(n):
    j = int(n)
    if j < 10:
        return j
    else:
        c = True
        j = j + 1
        while c:
            if str(j) == str(j)[::-1]:
                c = False
                return j
            else:
                j = j + 1


if __name__ == '__main__':
    # list1 = [12, 2, 34, 54, 35, 9, 35, 325, 353, 32, 0, 5]
    list1 = []
    inp = int(input("Enter the range of the List"))
    # Taking Input from user
    for i in range(inp):
        list1.append(input("Enter The Number"))
    list2 = []
    for i in range(inp):
        # Appending Palindrome elements into another list
        pali = palindrome(list1[i])
        list2.append(pali)
        # print(palindrome(i))
    print(f"Given List is :{list1}\n"
          f"Palindromify List is :{list2}")
