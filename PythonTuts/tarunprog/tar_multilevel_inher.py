class Dad:
    basketball = 1


class Son(Dad):
    dance = 3

    def isdance(self):
        return f"this is js dance style{self.dance}"


class Grandson(Son):

    def isdance(self):
        return f"this is yoyo guru syle{self.dance}"


harry = Grandson()
print(harry.isdance())
