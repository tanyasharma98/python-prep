print(f"Food Restaurant")
first = int(input("enter Number of item you want in list"))
inp = [input(f"Food Item{i + 1}") for i in range(first)]
listt1 = []
# ======================In-Build Method
for item in reversed(inp):
    listt1.append(item)
print(f"Reversed Ib-Built {inp} :{listt1}")
# ====================== Slicing Trick
listtt = inp[::-1]
print(f"Slicing Method for {inp} :{listtt}")
# =========================logic
reversedLogic = inp[:]
for i in range(len(inp)):
    if i != len(inp) - i:
        inp[i], inp[len(inp) - i - 1] = inp[len(inp) - i - 1], inp[i]
    else:
        print(f"Logic Reversed of {reversedLogic} : {inp}")

if listt1 == listtt and listtt == inp:
    print("All Method Provide same Result")
