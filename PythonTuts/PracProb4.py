# ======================================The Next Palindrome
def nextPalindrome(num):
    num = int(num) + 1
    while not IsPalindrome(num):
        num = num + 1
    return num


def IsPalindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    le = int(input("Enter how many no. you want to check"))
    jo = []

    for i in range(le):
        inp = (input("Enter Number To Get Next palindrome"))
        jo.append(inp)
    for i in range(le):
        print(f"Next Palindrome for{jo[i]} is: {nextPalindrome(jo[i])}")



#-----------------------------------------------------------------------Own--------------------------------

# le = int(input("enter"))
# lo = 0
# while lo < le:
#     inp = (input("Enter Number To Get Next palindrome"))
#     jo = inp[:]
#     c = True
#
#     while c == True:
#         inp = int(inp) + 1
#         st = str(inp)
#         j = st[::-1]
#
#         if st == j:
#             print(f"Next palindrome for {jo}is:{st}")
#             c = False
#             lo = lo + 1