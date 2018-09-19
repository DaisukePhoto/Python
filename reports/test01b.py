#test01b 16D8101021C 野口大輔　2017-11-20

import numpy as np
import random

a=int(input("input a:"))
b=int(input("input b:"))

count=0

f=open("small.csv","r")
data=f.readline().split()
for i in range(len(data)):
 if data[i]>=a and data[i]<=b:
  count=count+1
f.close()

print(a,"以上",b,"以下の要素は",count,"個あります")
