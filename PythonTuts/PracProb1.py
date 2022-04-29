# Your age Checker
class AgeCheck:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def YearCheck(self, value):
        year = value + 0
        year_count = 0
        for item in range(0, 100):
            year = year + 1
        for item in range(inp, 2021):
            year_count = year_count + 1
        print(f"{self.name} your age is: {year_count}")
        print(f"{self.name}You will turn 100yr old in : {year}")

    def ageVal(self, num):
        cur_yr = 2021
        age = 100 - self.value
        if num >= 100:
            num = self.value + 100
            for item in range(0, 100):
                cur_yr = cur_yr + 1
            print(f"{self.name} , to get more 100 , you age should be {num}")
            print(f"{self.name} , The oldest person alive ,you will get one more 100 in year {cur_yr} ")
        else:
            for item in range(0, age):
                cur_yr = cur_yr + 1
            print(f"{self.name} you have left {age}yrs to turn 100")
            print(f"{self.name} ,You will turn 100 in year {cur_yr}")


inp = int(input("Enter your Age or Year to check your age after 100 years"))
if inp == 0:
    raise Exception("You are newely born")
name = input("Enter your Name")
if name.isnumeric():
    raise Exception("Enter Valid name")

name = AgeCheck(name, inp)
if inp >= 1900 and inp < 2021:
    name.YearCheck(inp)
elif inp <= 200 and inp >= 0:
    name.ageVal(inp)

elif inp < 1900 and inp > 1000:
    raise ValueError("You Probably be Dead till now")
elif inp > 200 and inp < 1000:
    raise Exception("Wow Wow , Enter Valid age ,Dead Person!!!!!!!")
else:
    print("Hello WOmb Person")
