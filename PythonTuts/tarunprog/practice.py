# num=int(input())
# st =input()
# if num>=0 and num<=10:
#     print(num*2)
# print(st[:15])
# -----------------------------------------next------------------------------------------------##
# dna =input()
# if dna== "G"or dna=="C" or dna=="T" or dna=="A":
#     if dna=="G":
#         print(dna.replace("G","C"))
#     elif dna=="C":
#         print(dna.replace("C","G"))
#     elif dna=="T":
#         print(dna.replace("T","A"))
#     elif dna=="A":
#         print(dna.replace("A","T"))
# else:
#     print("Invalid Input as a string")

# ------------------------------------------------------------------------------------------------------------
# # c = ord("Q")
# # print(c)
# for i in range(ord("F"),ord("Q")):
#     print(i)
###-----------------------------------------------------------------------------------------------------------
# dna =str(input().upper())
# dict={"G":"C","C":"G","T":"A","A":"U"}
# # x=""
# try:
#     for i in dna:
#         print(dict[i] , end= "")
#     #     x=x+dict[i]
#     # print(x)
# except:
#     print("Invalid Input")
# ---------------------------------------------------------------------------------------------------------------
# c = ord("z")+ ord("z")+ord("n")+ord("B")
# print(c)
# -------------------------------------------------------------------------------------------------------------
# a=input()
# [a,b,c]= a.split(" ")
# a,b=b,a
# a= int(a)* int(c)
# b= int(b) + int(c)
# print(a,b)
# print(captcha)

# numArray = map(int, input().split())
# type(numArray)
# N = int(input())

# Get the array
# numArray1 = list(map(int, input().split()))
# numArray2 = list(map(int, input().split()))
#
# sumArray = []

# Write the logic here:
# for i in range(N):
#     sumArray.append(numArray1[i] + numArray2[i])

# Print the sumArray
# for element in sumArray:
#     print(element, end=" ")
#
# print("")
# ---------------------------------------------------------------------------------------------------------------
'''Check vowels in a word'''
# t = int(input())
# lw = ["a","e","i","o","u"]
# up = ["A","E","I","O","U"]
# for i in range(0,t):
#     st = input()
#     count_l = 0
#     count_up = 0
#     for j in range(0,len(lw)):
#         if lw[j] in st:
#             count_l = count_l+ 1
#     for n in range(0,len(up)):
#         if up[n] in st:
#             count_up = count_up + 1
#     if (count_up == 5) or (count_l == 5):
#         print("lovely string")
#
#     else:
#         print("ugly string")
# ---------------------------------------------------------------------------------------------------------------
# '''To make a number equal to another number '''
# t = int(input())
# for i in range(0,t):
#     count = 0
#     flag = 0
#     k,m,n = map(int,input().split())
#     if flag == 0:
#         while(k <= m):
#             k = k*n
#             count += 1
#             if k == m:
#                flag = 1
#                break
#
#     if flag == 0:
#         while(k-2 >= m):
#             k = k-2
#             count += 1
#             if k == m:
#                 flag = 1
#                 break
#     if flag == 0:
#          while(k-1 >= m):
#              k = k-1
#              count+=1
#              if k==m:
#                 flag = 1
#                 break
#     print(count)
# ----------------------------------------------------------------------------------------------------------
# from time import time
# init = time()
# t = int(input())
# for i in range(0,t-1):
#     k,m,n =map(int,input().split())
#     count = 0
#     while(k!=m):
#         if k < m:
#             k = k * n
#             count += 1
#         elif k-2 >= m:
#             k = k- 2
#             count +=1
#         else:
#             k = k-1
#             count +=  1
#
#     print(count)
#     print(time() - init)
# ========================================================================================
#
# from time import time
# init = time()
#
# def small(k,m,n):
#     count = 0
#     while k != m :
#         if k < m:
#             k = k * n
#             count += 1
#         elif  k-2 >=m:
#             k -= 2
#             count +=1
#         elif k-1 >= m:
#             k -= 1
#             count += 1
#         else:
#             break
#     return count
# def big(k,m):
#     count = 0
#     while k != m:
#         if (k != m) and (k-2 >=m):
#             k -= 2
#             count +=1
#         elif (k != m) and (k-1 >=1):
#             k -= 1
#             count +=1
#         else:
#             break
#
#     return count
#
#
# t = int(input())
# for i in range(0,t):
#     k,m,n =map(int,input().split())
# #     if (k< m):
#         a = small(k,m,n)
#         print(a)
#         # print(time() - init)
#     else:
#         b= big(k,m)
#         print(b)
#         # print(time() - init)
# =======================================================================
"""a,b,c  -2,-1, *n"""
# def rec(a, b, c):
#     if a >= b:
#         return ((a-b)//2+(a-b)%2)
#     if b%c==0:
#         return (1 + rec(a,b//c,c))
#     else:
#         x=(b//c+1)*c
#         return ((x-b)//2 + (x-b)%2 + rec(a,x,c))
#
# t = int(input())
# while t > 0:
#     a, b, c = map(int, input().split())
#     print(rec(a, b, c))
#     t -= 1
# ===============================================================================================================
# num = int(input("Enter number of element you want "))
#
# ls =[]
# for i in range(0,num):
#     element = input("element")
#     ls.append(element)
# to_do = int(input("press 1 :- list compre \nPress 2 :- dictionary compre\n Press 3:- set compre"))
# if to_do == 1:
#     list = [i for i in ls]
#     print(list)
#     print(type(list))
#
# elif to_do == 2:
#     dict = {i:f"Item{i}" for i in ls}
#     print(dict)
#     print(type(dict))
#
# elif to_do ==3:
#     st = {i for i in ls}
#     print(st)
#     print(type(st))
# ----------------------------------------------------------------------------------------------------------------
# t = int(input())
#
# while t:
#     a,b,c = list(map(int, input().strip().split()))
#     x = abs(2 * b - (a + c))
#
#     if x % 2 == 0:
#
#         print(int(x / 2))
#
#     else:
#
#         print(int((x / 2) + 1))
#
#         t = t - 1
# ------------------------------------------------------------------------------------------------------------
# n= int(input())
#
# for i in range(n):
#
#     a,b,c = list(map(int, input().strip().split()))
#
#     print((abs((b-a)-(c-b))+1)//2)
# --------------------------------------------------------------------------------------------------------------
n = int(input())
a = [i for i in sorted(map(int, input().strip().split()))]
c = [a.count(x) for x in a]
num=a[c.index(max(c))]
print(num)
#Can use dict to implem
# N=int(raw_input())
# a=sorted(map(int,raw_input().split(' ')))
# c = [a.count(x) for x in a]
# num=a[c.index(max(c))]
# print(num)