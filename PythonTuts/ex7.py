#Healty Programmer
import datetime
from playsound import playsound
import time
def getdate():
 import datetime
 return datetime.datetime.now()

i=0
j=0
z=0
while (i<8 and j<16 and z<10):
 i=i+1
 j=j+1
 z=z+1
 if i<8 and j<16 and z<10 :
  time.sleep(5)
  print("Healty Healthy ,Drink Water") # from pygame import mixer
  ### this line should be written once on  the top
  playsound('water.mp3')
  yop = int(input("Press:1 , After drink "))
  if yop == 1:
   with open("water.txt", "a") as f:
    f.write(str(getdate()))
    f.write("Water Drank \n")
    f.write("Next\n")
    # time.sleep(5)
  time.sleep(5)
  playsound('eyes.mp3')
  hop = int(input("Press : 2 , After Relaxing your eyes"))
  if hop == 2:
   with open("eyes.txt", "a") as f:
    f.write(str(getdate()))
    f.write("Relaxing Done\n")
  time.sleep(10)
  playsound('physical.mp3')
  lop = int(input("Press : 3 , After Relaxing your eyes"))
  if lop == 3:
    with open("physical.txt", "a") as f:
     f.write(str(getdate()))
     f.write("Excercise Done\n")
    continue
 else:
  print("You have Drank all water\ Press W for check schedule\n")
  print("You have comleted your  Eyes Rotation\ Press E for check schedule\n")
  print("You have done your physcial excercise\ Press P for check schedule\n")
  jopi=input("Type here")
  if jopi=="W" and jopi=="w":
   with open("water.txt","r") as f:
    f.readlines()
  elif jopi == "E" and jopi == "e":
    with open("eyes.txt", "r") as f:
     f.readlines()
  elif jopi == "P" and jopi == "p":
     with open("physical.txt", "r") as f:
      f.readlines()
  else:
   break
