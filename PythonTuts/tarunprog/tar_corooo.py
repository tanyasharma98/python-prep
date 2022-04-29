# def searcher():
#     import time
#     book = "There was a wise king name tarun"
#     time .sleep(3)
#
#     while True:
#         txt = (yield)
#         if txt in book:
#             print("Here you go")
#         else:
#             print("Not present")
#
#
# search = searcher()
# print("search Started")
# next(search)  #starting corutine
# search.send("There")
# input("Enter")
# search.send("wise")
# search.send("hello")
# search.send("tarun")
#
# search.close()


#===================================================================================================================
def reader():
    import time
    with open("harry_food.txt") as f:
     f1 = f.read()
    # content = "Tarun chintu js yo taru jois kns"
    time.sleep(3)

    while True:
        txt = (yield)
        if txt in f1:
            print("Present")
        else:
            print("not present")

read = reader()
print("Reader Started")
next(read)
read.send(input("Enter your name"))
read.send(input("Enter your name"))
read.send(input("Enter your name"))