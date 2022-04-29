# # i=1
# # while(True):
# drop= input()
# if drop=="G":
#     print(drop.replace('G','C'))
# elif drop=="C":
#     print(drop.replace('C','G'))
# elif drop=="T":
#     print(drop.replace('T','A'))
# elif drop=="A":
#     print(drop.replace('A','U'))
DNA = str(input())

x = " "

for i in DNA :

 if i == 'G' :
    x += 'C'
 elif i == 'C':
    x += 'G'
 elif i == 'T':
    x += 'A'
 elif i == 'A':
    x += 'U'
 else :
    x = "Invalid Input"
    break
print (x)