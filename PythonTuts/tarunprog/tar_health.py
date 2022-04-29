print("Health Management System")


def getdate():
    import datetime
    return datetime.datetime.now()


def name(a):
    if a == 1:
        print("Rohan is selected")
        task = int(input("press\n 1:- Exercise \n 2:- Food"))
        if task == 1:
            value = input("Enter text")
            with open("rohan_ex.txt", "a") as f:
                f.write(str([str(getdate())]) + " :  " + value + "\n")
                print("Added successfully")
        elif task == 2:
            value = input("Enter text")
            with open("rohan_food.txt", "a") as f:
                f.write(str([str(getdate())]) + " :  " + value + "\n")
                print("Added successfully")
    elif a == 2:
        print("Harry is selected")
        task = int(input("press\n 1:- Exercise\n 2:- Food"))
        if task == 1:
            value = input("Enter text")
            with open("harry_ex.txt", "a") as f:
                f.write(str([str(getdate())]) + " :  " + value + "\n")
                print("Added successfully")
        elif task == 2:
            value = input("Enter text")
            with open("harry_food.txt", "a") as f:
                f.write(str([str(getdate())]) + " :  " + value + "\n")
                print("Added successfully")
    elif a == 3:
        print("Harry is selected")
        task = int(input("press\n 1:- Exercise\n 2:- Food"))
        if task == 1:
            value = input("Enter text")
            with open("hammad_ex.txt", "a") as f:
                f.write(str([str(getdate())]) + " :  " + value + "\n")
                print("Added successfully")
        elif task == 2:
            value = input("Enter text")
            with open("hammad_food.txt", "a") as f:
                f.write(str([str(getdate())]) + " :  " + value + "\n")
                print("Added successfully")


def retrieve(a):
    if a == 1:
        print("Rohan is selected")
        task = int(input("press\n 1:- Exercise\n 2:- Food"))
        if task == 1:
            with open("rohan_ex.txt", "r") as f:
                y = f.read()
                print(y)
        elif task == 2:
            with open("rohan_food.txt", "r") as f:
                y = f.read()
                print(y)
    elif a == 2:
        print("Harry is selected")
        task = int(input("press\n 1:- Exercise\n 2:- Food"))
        if task == 1:
            with open("harry_ex.txt", "r") as f:
                y = f.read()
                print(y)
        elif task == 2:
            with open("harry_food.txt", "r") as f:
                y = f.read()
                print(y)
    elif a == 3:
        print("Harry is selected")
        task = int(input("press\n 1:- Exercise\n 2:- Food"))
        if task == 1:
            with open("hammad_ex.txt", "r") as f:
                y = f.read()
                print(y)
        elif task == 2:
            with open("hammad_food.txt", "a") as f:
                y = f.read()
                print(y)
    print("You want to do more")
    # rep = input("y or n")
    # if rep=="y" or rep=="Y":


data = int(input("press \n 1:- Log \n 2:- Retrieve"))
print("Select person")
a = int(input("1:-Rohan\n2:-Harry\n3:-Hammad"))

if data == 1:
    name(a)
else:
    retrieve(a)
