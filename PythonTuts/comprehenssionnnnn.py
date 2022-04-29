# lst=[]
# for i in range(100):
#     if i%3==0:
#         lst.append(i)
# print(lst)

#-----------Comprehension------

# lst =[i for i in range(100) if i%3==0]
# print(lst)4


# dict1={i:f"Item{i}" for i in range(10 ,101) if i%10==0}
# dict1={i:f"Item{i}" for i in range(5)}
# dict2={value:key for key , value in dict1.items()}
# print(dict1,"\n",dict2)

# dress1 ={dress for dress in ["dress1","dress2","dresss1","dress2","dresssss1","dress1"]}
# print(dress1)
# print(type(dress1))


#for genetor we use PARANTHESIS
# evens =( i for i in range(50) if i%2==0)
# print(type(evens))
# print(evens.__next__())

# for i in evens: # For generator we can use this
#     print(i)


#--------------------------------------Question--------------------

inp =int(input("enter"))
listt =[]
for i in range(0,inp):
    hop =input()
    listt.append(hop)
    inp = inp -1
print(listt)
print("What You Want")
jop =input("Enter D/d:Dictionary Comprhenssion\n"
           "Enter S/s:Set Comprhenssion\n"
           "Enter L/l:List Comprhenssion\n")

if jop=="D" or jop=="d":
    dict1={i:f"{index}" for i ,index in enumerate(listt) }
    print(dict1)
elif jop=="S" or jop=="s":
    seet = {i for i in listt}
    print(f"Your set:{seet}")
elif jop=="L" or jop=="l":
    print(listt)

