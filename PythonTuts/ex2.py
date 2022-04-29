#Faulty Calculator For Cheaters
print("Use This python Calculator")
a= int(input("Enter first value:\n"))
b= int(input("enter second value:\n"))
print("If you want to ADD Enter : 1 ")
print("If you want to SUBTRACT Enter : 2 ")
print("If you want to Multiply Enter : 3 ")
print("If you want to Divide Enter : 4 ")
c= int(input("Enter your choice\n"))
if c==1:
    if a==12 and b==44:
        print("12+ 44 = 58")
    else:
        print(a,"+",b,"=",a+b)
elif c==2:
    if a==453 and b==120:
        print("453-120 = 303 ")
    else:
        print(a,"-",b,"=",a-b)
elif c==3:
    if a==45 and b==3:
        print("45*3= 255")
    else:
        print(a,"*",b ,"=",a*b)
elif c==4:
    if a==36 and b==6:
        print("36/6= 4")
    else:
        print(a,"/",b,"=",a/b)
