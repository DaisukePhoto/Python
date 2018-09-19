#test01c 16D8101021C 野口大輔　2017-11-20

import random
import numpy as np 
stat=1
seed=np.random.rand()
stat_list=[0]*4
for i in range(100):
 if stat==1:
   stat_list[0]=stat_list[0]+0.3
   stat_list[1]=stat_list[1]+0.7

 elif stat==2:
   stat_list[2]=stat_list[2]+0.5
   stat_list[3]=stat_list[3]+0.5
 
 elif stat==3:
   stat_list[2]=stat_list[2]+0.6
   stat_list[3]=stat_list[3]+0.4

 elif stat==4:
  stat_list=stat_list[0]+1
 
 if stat==1:
  if seed<=0.3:
   stat=1
  else:
   stat=2
 elif stat==2:
  if seed<=0.5:
   stat=3
  else:
   stat=4
 elif stat==3:
  if seed<=0.6:
   stat=3
  else:
   stat=4
 elif stat==4:
  stat=1


 if i==0:
  print("1step:",stat_list)
 if i==9:
  a=stat_list[0]
  b=stat_list[1]
  c=stat_list[2]
  d=stat_list[3]
  print("10step",a,b,c,d)
 if i==99:
  a=stat_list[0]
  b=stat_list[1]
  c=stat_list[2]
  d=stat_list[3]
  print("100step",a,b,c,d)
