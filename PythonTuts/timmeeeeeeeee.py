import time
# i=0
# initial = time.time()
#
# while(i<10000000000000):
#     print("Runniing this  while loop program")
#     i=i+1
# print("while loop time ",time.time()-initial)
#
# intial2= time.time()
# for i in range(20):
#     print("This is a for loop program")
# print("This is a  for loop time",time.time()-intial2)


localtime= time.asctime(time.localtime(time.time()))
print(localtime)
#time.sleep()-------used  in fstringsssss.py