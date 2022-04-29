# Map Function -------------------------------------------------------------------------------
# numbers=["3","40","44"]
# numbers=list(map(int,numbers))
#
# # for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])
#
# numbers[2]=numbers[2]+1
# # print(numbers[2])
# #
# # def sqa(a):
# #     return a*a
#
#
# num=[2,3,4,5,6,7,8,9]
# # square=list(map(sqa ,num))
# square= list(map(lambda x:x*x, num))
# print(square)


# def square(a):
#     return a * a
# def cube(a):
#     return a*a*a
#
# func=[square , cube]
#
# for i in range(5):
#     kop = list(map(lambda x:x(i) , func))
#     print(kop)



#Filter Function ----------------------------------------------------------------
# list_lop=[ 2, 5,6, 9,1,15,14,11]

# def greater_than(num):
    # return num>5
# gr_than_5 = list(filter(greater_than ,list_lop))
# print(gr_than_5)


#Reduce Function-------------------------------------------------------------------

from functools import reduce
list1= [1,2,3,4]

num = reduce(lambda x,y:x*y, list1)
# num=0
# for i in list1:
#     num = num + i
print(num)
