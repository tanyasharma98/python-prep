#Guess the number
n=18
print("Total Number of Moves are 5")
i=0
j=5
while(True):
  inp=int(input("Guess the number\n"))
  if inp>18 and j>=0:
    print("Your number is greater")
    i=i+1
    j=j-1
    if j>0:
     print("Moves used",i)
     print("Total",j,"moves left .TRY AGAIN")
     continue
    else:
       print("Zero Moves left")
  elif inp<18 and j>0:
   print("Your Number is smaller")
   i=i+1
   j=j-1
   if j>0:
    print("Moves are used",i)
    print("Total", j, "moves left .TRY AGAIN")
    continue
   else:
      print("Zero Moves left game over")
      break
  elif inp==18 and j>0:
    print("You have Guess the same number ")
    i=i+1
    j=j-1
    if j>0:
     print("Only in",i,"moves")
     print("You saved", j,"moves. WOW")
     print("Game Over")
    break