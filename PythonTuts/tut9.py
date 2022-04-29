grocery = ["dog", "soap", "potty", "toilet"]
#print(grocery[2])
number= [4 , 9 ,11 , 1, 15]
#number.sort()
#number.reverse()
#print(number)
#print(number[1:4])
#print(number[::-1])
#print(number[1:5:2])
#number.append(34)
#number.insert(2,50)
#number.remove(11)
#number.pop()
#print(number)
#number[2]= 12
#print(number)

#Mutable   ------ Can change(list)
#Immutable   ------- cannot change(tuple)

#tp = (1,2,3)
#tp[1] = 5   cannot change

#tp =(1)   this is not tuple
#tp =(1,)  this is tuple
#print(tp)


# Swapping
#traditional method
"""a=1
b= 10
temp= a
a=b
b=temp
print(a,b)"""

#easy way
a= 1
b= 11
a,b = b,a
print(a,b)