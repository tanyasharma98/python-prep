#Health Management System
print("Health Management System")
while(True):
    print("If You want to Lock: Press 1\n")
    print("Tf you want to Retrieve : press 2\n")
    yop = int(input("Enter your value here"))   
    def getdate():
        import datetime
        return datetime.datetime.now()
    if yop==1:
        name= input("Enter the name you want to Lock")
        if name=="tanya":
            fil=int(input("Press: 1 for excercise and 2 for Food"))
            if fil==1:
                with open("tan_ex.txt","a") as f:
                    f.write(str(getdate()))
                    f.write(input("Enter your  Excercise schedule")+ "\n")
                    print()
            elif fil==2:
                with open("tan_fo.txt","a") as f:
                    f.write(str(getdate()))
                    f.write(input("Enter your  Food schedule") + "\n")
                    print()
        elif name=="panya":
            hip=int(input("Press: 1 for Excercise and 2 for Food"))
            if hip==1:
                with open("pan_ex.txt","a") as f:
                    f.write(str(getdate()))
                    f.write(input("Enter your Excercise schedule") + "\n")
                    print()
            elif hip==2:
                with open("pan_fo.txt","a") as f:
                    f.write(str(getdate()))
                    f.write(input("Enter your Food schedule") + "\n")
                    print()
        elif name=="fonya":
            dip=int(input("Press: 1 for Excercise and 2 for food"))
            if dip==1:
                with open("fon_ex.txt","a") as f:
                    f.write(str(getdate()))
                    f.write(input("Enter your Excersice schedule") + "\n")
                    print()
            elif dip==2:
                with open("fon_fo.txt","a") as f:
                    f.write(str(getdate()))
                    f.write(input("Enter your Food schedule")+ "\n")
                    print()
    elif yop==2:
        loop= input("Enter the name you want to retrieve\n")
        if loop=="tanya":
            fil = int(input("Press: 1 for excercise and 2 for Food"))
            if fil == 1:
                with open("tan_ex.txt", "r") as f:
                    no=f.readlines()
                    print(no)
            elif fil == 2:
                with open("tan_fo.txt", "r") as f:
                    dp=f.readlines()
                    print(dp)
        elif loop=="panya":
            hip = int(input("Press: 1 for Excercise and 2 for Food"))
            if hip == 1:
                with open("pan_ex.txt", "r") as f:
                    fo=f.readlines()
                    print(fo)
            elif hip == 2:
                with open("pan_fo.txt", "r") as f:
                    nip=f.readlines()
                    print(nip)
        elif loop=="fonya":
            dip = int(input("Press: 1 for Excercise and 2 for food"))
            if dip == 1:
                with open("fon_ex.txt", "r") as f:
                    sip= f.readlines()
                    print(sip)
            elif dip == 2:
                with open("fon_fo.txt", "r") as f:
                    al=f.readlines()
                    print(al)
    print("IF you want to add more press Y")
    so=input()
    if so=="Y" or so=="y":
        continue
    else:
        break








