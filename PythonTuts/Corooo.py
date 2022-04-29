# def searcher():
#     import time
#     #Some Delay in reading
#     book = "This is the book written by tanya and checl this out"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Text Present")
#         else:
#             print("Text is not present")
#
# search = searcher()
# print("search started")
# next(search)
# input("Next search")
# search.send("tanya")
# input("press")
# search.send("and")
# search.close()
# search.send("tanya")




#_------------------________________-------QUiz
def curo():
    import time
    alpha = "tanya kipo dijo jojo kilp sd fhrt qwwe we rnl fool start end pongi"
    time.sleep(4)

    while True:
        text = (yield)
        if text in alpha:
            print("Your Text present")
        else:
            print("Not present")


lipo = curo()
print("Lets Start Loading")
next(lipo)
gip=input("Enter")
lipo.send(gip)
print("Lets do again without taking time")
kip=input("enter")
lipo.send(kip)
print("Closed here .Check yourself")
lipo.close()
gp=input("Check")
lipo.send(gp)