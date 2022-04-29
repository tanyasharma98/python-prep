"""
Iterable = __iter__() or  __getitem()

Iterator = __next__()

Iteration =

"""
import math


def gen(n):
    for i in range(n):
        yield i

# for i in range(40000000):
#     print(i)

# g =  gen(3000000000000000000)
# print(g)

g=gen(4)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())------ It Will show error
# print(g.__next__())


# for i in g: # Generator can iterate only one time
    # print(i)

# t=123453 #Iteration cannot be define on integer
t = "tanya"
# print(t[2])
# print(iter(t))
ier = iter(t)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

# for ih in t:
#     print(ih)



#---------------------------------Quiz------------------------------------
def fac(n):
    fact =1
    for item in range(1,n+1):
        fact = fact * item
    yield (fact)



def fibo(n):
    a=0
    b=1
    sum=0
    count=1
    while(count<n):
        count+=1
        a=b
        b=sum
        sum=a+b
        print(sum , end=" ")






inp=int(input("Enter Your number"))
fac(inp)
# print(math.factorial(inp))
print(fibo(inp))

#fibonnaci Another program ###Copied Online


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
