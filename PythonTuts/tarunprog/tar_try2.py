f = open("tarun.txt", "r")

try:
    f2 = open("js.txt", "r")

except Exception as e:
    print(e)

else:
    print("try wala execute hua ha ")

finally:
    f.close()
