# =========================================Divide the apples=========================================
potter = int(input("Enter Number of apples you got from your friends"))
mn = int(input("Enter minimum range of apples"))
mx = int(input("Enter maximum range of apples"))
if potter == int or mn == int or mx == int:
    print("Enter Number Value")
if mn < mx:
    for i in range(mn, mx+1):
        if potter % i == 0:
            print(f"{i} is divisor of {potter}")
        else:
            print(f"{i} is not a divisor of {potter}")
elif mn == mx:
    print("This is not the range")
else:
    print("Minimum Value is Greater than Maximum Value!!!Try Again")