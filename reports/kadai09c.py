#kadai09c 16D8101021C 野口大輔　2017-11-27

import numpy as np
import random

def quick(a):
 length=len(a)
 print(length,a)
 
 if length==0 or length==1:
  return a
 else:
  pivot=a[0]
  left=[]
  right=[]
  
  for i in range(0,length):
   if a[i]<pivot:
    left.append(a[i])
   else:
    right.append(a[i])
  #left=quick(left)
  #right=quick(right)
  return quick(left) + quick(right)

b=[7,3,10,1,7,6,3,9,4,2]


print("input:",b)

print("output:",quick(b))

