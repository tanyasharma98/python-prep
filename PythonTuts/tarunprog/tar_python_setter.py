class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}{self.lname}@guru.com"

    def printdetail(self):
        return f"Name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == "None" or self.lname == "None":
            return f"Email not present.  please set it using setter"
        return f"{self.fname}{self.lname}@guru.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = "None"
        self.lname = "None"


tarun_sir = Employee("Tarun", "Sir")
rohan_paji = Employee("Rohan", "paji")

print(tarun_sir.email)
tarun_sir.fname = "Dollar"

print(tarun_sir.email)
tarun_sir.email = "this.that@guru.com"

print(tarun_sir.fname)
print(tarun_sir.lname)
print(tarun_sir.email)
del tarun_sir.email
print(tarun_sir.email)
tarun_sir.email = "this.tarun@guru.com"
print(tarun_sir.email)
