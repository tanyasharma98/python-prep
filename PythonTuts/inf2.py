if __name__ == '__main__':
    list1 = []
    value = int(input())
    for i in range(1, value + 1):
        list1.append(i)
    length = int(input())
    list2 = []
    for i in range(1, length + 1):
        list2.append(i)
    if length==1:
        count1 =0
        for i in list1:
            count1 +=1
            print(f"[{i}]")
        print(count1)
    else:
        count2=0
        for i in list1:
            for j in list1:
                if j%i==0:
                    count2 +=1
                    print(f"[{i},{j}]")
        print(count2)
