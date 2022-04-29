#Integer
while(True):
    n=int(input("Enter value of n\n"))
    choose=int(input("Enter a boolean value 0/1"))
    flag=bool(choose)
    if flag==True:
        for x in range(1,n+1):  #range(start , stop , steps)
            print(x*"*")
    else:
        for i in range(n,0,-1):
            print(i*"*")
    again= input("If you wnt to continue press Y")
    if again=="y" or again=="Y":
        continue
    else:
        print("Bye Bye")
        break