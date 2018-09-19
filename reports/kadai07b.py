#kadai07b 16D8101021C　野口大輔　2017-11-13

import numpy as np
import random

itr=int(input("itr:"))
Base=[0.6,0.3,0.1] #晴れ
weather=0
c=[0,0,0]
P=[[0.6,0.3,0.1],[0.3,0.6,0.1],[0.2,0.3,0.5]]
count=0

for i in range(itr+1):
 seed=np.random.rand()
 
 if int(i*10)%int(itr)==0:
  print(i,":",c)

 if weather==0:#晴れのとき
  if seed<0.6:
   c[0]=c[0]+1
   weather=0
  elif seed<0.9:
   c[1]=c[1]+1
   weather=1
  else:
   c[2]=c[2]+1
   weather=2
 

 elif weather==1:#曇りのとき
  if seed<0.3:
   c[0]=c[0]+1
   weather=0
  elif seed<0.9:
   c[1]=c[1]+1
   weather=1
  else:
   c[2]=c[2]+1
   weather=2
 
 elif weather==2:#雨の時
  if seed<0.2:
   c[0]=c[0]+1
   weather=0
  elif seed<0.5:
   c[1]=c[1]+1
   weather=1
  else:
   c[2]=c[2]+1
   weather=2

 
"""
(py361) [16D8101021C@ise31c ~]$ python kadai07b.py
itr:100
0 : [0, 0, 0]
10 : [4, 4, 2]
20 : [11, 7, 2]
30 : [17, 8, 5]
40 : [20, 15, 5]
50 : [25, 19, 6]
60 : [30, 22, 8]
70 : [34, 27, 9]
80 : [39, 32, 9]
90 : [43, 36, 11]
100 : [45, 40, 15]
"""
