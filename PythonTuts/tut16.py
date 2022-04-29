# list1 =[ ["Tanya",100],["Uniya",20],["Yuniya",40],["Funiya",30]]
#
# dict1 = dict(list1)
# #print(dict1)
# for item in dict1:
#     print(item)
# for item, marks in dict1.items():
#     print(item,"marks is", marks)



#Quiz
list1= [20, 4,"dop", 12, 8,1,"tanya",  12, 6,"spring", 2,70,80,54]
for item in list1:
    if str(item).isnumeric() and item>=6:
        print(item)