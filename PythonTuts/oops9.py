class Dad:
    basketball=1
class Son(Dad):
    dance = 1
    basketball = 4
    def dancing(self):
        return f"I can dance only {self.dance} times"
class Grandson(Son):
    dance=6
    def dancing(self):
        return f"I can dance only{self.dance} times , very awakwardly"


gopi = Dad()
sopi = Son()
lopi = Grandson()

# print(gopi.dancing())
# print(lopi.basketball)


#Quiz
class electronic:
    tv_types= 20
    laptops_types = 30
    phones = 50
    pens = 10

    def printing(self):
        return f"Tvs unit are {self.tv_types} and laptops units are {self.laptops_types} " \
               f"Phone units are {self.phones} and we have {self.pens} pens"

class pocket_gadget(electronic):
    small_size = 10
    medium_size = 10

    def sizing(self):
        return f"small size unit are {self.small_size} , medium units are {self.medium_size}"

class phone( pocket_gadget):
    samsung = 5
    iphone = 40
    nokia =1
    def printing(self):
        return  f"samsung unit are {self.samsung} and iphone units are {self.iphone} " \
               f"Nokia units are {self.nokia} "
    def totalphones(self):
        return self.samsung+ self.iphone + self.nokia



gada = electronic()
bagha = pocket_gadget()
dopi = phone()

# print(bagha.sizing())
# print(electronic.phones)
print(dopi.phones)
print(dopi.totalphones())
print(dopi.laptops_types)
damn =dopi.printing()
print(damn)