# F strings
import math
import time
me="tanya"
she="san"
dop="sap"
dip="nope"
#a = "this is %s %s %s %s"%(me , she, dop , dip) #It leads to problem in readability
# a= "This is {1} {0}"  #Readability problem
# b=a.format(me,she)
# print(b)


#F strinf concept
a=f"this is {me} {she} {4*4} {math.cos(2)}" # F means fast
print("This is printed immediately.")
print(a)
time.sleep(2.4)
print("This is printed after 2.4 seconds.",a)  #Time module test