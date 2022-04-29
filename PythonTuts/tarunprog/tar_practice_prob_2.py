n = int(input("Enter the number of apples harry has got"))
mn = int(input("What is the minimum number"))
mx = int(input("What is the maximum number"))

if mn == mx:
    print("This is not a range\nmn is equal to mn")
else:
    for i in range(mn, mx+1):
        if n % i == 0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")
