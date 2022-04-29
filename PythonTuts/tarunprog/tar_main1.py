def tar(js):
    return f"here it is {js}"


def add(num1, num2):
    return num1 + num2 + 5


print(__name__)
# o= add(int(input("ask")),int(input("ask")))
# print(o)
if __name__ == '__main__':
    print(tar("tarunjii"))
    o = add(int(input("ask")), int(input("ask")))
    print(o)
