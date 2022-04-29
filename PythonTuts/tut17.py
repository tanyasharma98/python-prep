# i=0
#
# while(i<30):
#     print(i+1, end=" ")
#     i=i+1


# i=0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1, end=" ")
#     if i==20:
#         break #stop the loop
#     i=i+1

# Quiz
while True:
    i = int(input("Enter the digit\n"))
    if i > 1000:
        print("You have successfully type greater than 1000\n")
        break
    else:
        print("your number is ", i, "Try again\n")
        continue
