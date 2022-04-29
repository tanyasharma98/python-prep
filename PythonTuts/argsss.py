# def funct(a,b,c,d,e):
#     print(a,b,c,d,e)


# normal argument , *args ,*kwargs
def funargs(normal,*args,**kwargsdumm): #if pass ----(*args , normal) #throug error
    print(normal)
    for items in args:
        print("\nThese are no heroes except Tanya legendary",items)
    for keys , value in kwargsdumm.items():
        print(f"{keys} is a {value}")
    # print(type(args))
    # print(args[0])
normal="This is a normal text test"
tan=["yoka","doka","loka","puka","Goku programmer"]

kt={"tanya":"pro","unia":"noob","sopi":"less than tobi","Madira":"Uchiha"}
funargs(normal ,*tan, **kt) #through error --- (*args , normal)
# funct("tanya","panya","hoka","soke","coke")