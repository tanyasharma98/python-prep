f1=open("tanya.txt")

try:
 f = open("does.txt")
 # f = open("fon_ex.txt") #This file exist i.e except will not run else will run

# except Exception as e:
#     print(e)
except EOFError as e:
    print("EOFerror occur",e)
except IOError as e:
    print("IOerror occur",e)

# Only one can run between EXCEPT or ELSE
else:
    print("HAHAHA , Except Fail")

#This will run anyway or in any condition
#Finally is CODE CLEANUP
finally:
    print("This will alwaYs Run")
    # f.close()
    f1.close()

print("THIs Not include")
