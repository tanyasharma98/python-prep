#Snake , Water , Gun Game
import random
print("S/s for snake")
print("W/w for Water")
print("G/g for gun")
i=0
j=0
turn=0
while(True):
    if(turn<=10):
        list1=["Snake" , "Water" ,"Gun" ]
        player=input("Enter Here")
        lip=random.choice(list1)
        if(player=="S" or player=="s" and lip=="Water"):
            print("Player = Snake and Computer = Water")
            print("Player won")
            i=i+1
            print("Player Point:",i,"\n ")
            print("Computer Point:",j,"\n")
        elif(player == "W" or player == "w" and lip == "Snake"):
            print("Player = Water and Computer = Snake")
            print("Computer won")
            j = j + 1
            print("Player Point:", i, "\n ")
            print("Computer Point:", j,"\n")
        elif(player=="G" or player=="g" and lip=="Snake"):
            print("Player = Gun and Computer = Snake")
            print("Player won")
            i=i+1
            print("Player Point:",i,"\n ")
            print("Computer Point:",j,"\n")
        elif(player == "S" or player == "s" and lip == "Gun"):
            print("Player = Snake and Computer = Gun")
            print("Computer won")
            j =j + 1
            print("Player Point:", i,"\n ")
            print("Computer Point:", j,"\n")
        elif(player=="S" or player=="s" and lip=="Snake"):
            print("Player = Snake and Computer = Snake")
            print("Tie Tie ")
            print("Player Point:",i,"\n ")
            print("Computer Point:",j,"\n")
        elif(player=="W" or player=="w" and lip=="Gun"):
            print("Player = Water and Computer = Gun")
            print("Player won")
            i=i+1
            print("Player Point:",i,"\n ")
            print("Computer Point:",j,"\n")
        elif(player=="W" or player=="w" and lip=="Water"):
            print("Player = Water and Computer = Water")
            print("Tie")
            print("Player Point:",i,"\n ")
            print("Computer Point:",j,"\n")
        elif(player=="G" or player=="g" and lip=="Water"):
            print("Player = Gun and Computer = Water")
            print("Computer won")
            j=j+1
            print("Player Point:",i,"\n ")
            print("Computer Point:",j,"\n")
        elif(player == "G" or player == "g" and lip == "Gun"):
            print("Player = Gun and Computer = Gun")
            print("Tie Tie")
            print("Player Point:", i, "\n ")
            print("Computer Point:", j,"\n")
        turn= turn +1
        continue
    else:
        if(i>j):
            print("Player Won by ",i,"points\n")
            print("Computer got",j,"points\n")
            print("Run Again to play  ")
            break
        else:
            print("Computer won by",j,"points\n")
            print("Player got",i,"points\n")
            print("Run Agian to play\n")
            break

