# a = input("Enter your name")
# b = input("Enter your aukat")
#
# if int(b) == 0:
#     raise ZeroDivisionError("Your aukat is zero can't proceed further")
#
# if a.isnumeric():
#     raise Exception("Number's not allowed")
# print(f"Hello {a}")
c = input("Enter your name")
try:
    print(int(c))

except Exception as e:
    if c == "Harry":
        raise ValueError("Haryy is criminal")
    print(e)