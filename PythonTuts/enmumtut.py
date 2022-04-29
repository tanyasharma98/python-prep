l1 = ["Noodles", "Soup", "Gwakamoli", "kimchi"]
# i=1
# for items in l1: #starts from 1
#     if i%2 is not 0:
#         print(f"This is {items}")
#     i=i+1

for index, items in enumerate(l1):  # start from 0
    if index % 2 == 0:
        print(f"This is {items}")
