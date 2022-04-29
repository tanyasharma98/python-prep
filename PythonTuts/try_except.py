num1= input("Enter first value\n")
num2= input("Enter second value\n")
try:
    print("This is the sum of two values", int(num1)+int(num2))

except Exception as e:
    print(e)

print("Important line alert")