food_lst = list(map(int, input("Enter food name separated by coma").split(",")))

rv_lst = food_lst.copy()
rv_lst.reverse()
print(f"{food_lst} and after reversing by inbuilt method {rv_lst}")


rv = food_lst[::-1]
print(f"{food_lst} and after reversing by slicing {rv}")


new_lst = food_lst.copy()
for i in range(len(food_lst) // 2):
    new_lst[i], new_lst[len(new_lst) - i - 1] = new_lst[len(new_lst) - i - 1], new_lst[i]
print(f"{food_lst} and after reversing by logic {new_lst}")

if new_lst == rv_lst and rv_lst == rv:
    print("all list are same")
