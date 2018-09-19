#kadai05b 16D8101021C 野口大輔　2017-10-23

import csv
import numpy as np
A=np.loadtxt("matrixA.csv",delimiter=",",dtype=int)
B=np.loadtxt("matrixB.csv",delimiter=",",dtype=int)
na=A.shape[0]
ma=A.shape[1]

nb=B.shape[0]
mb=B.shape[1]

count_A=0
count_B=0

for i in range(0,na):
 for j in range(0,ma):
  if(A[i][j]!=0):
   count_A=count_A+1

for i in range(0,nb):
 for j in range(0,mb):
  if(B[i][j]!=0):
   count_B=count_B+1

print("Aの非ゼロ要素数：",count_A)
print("Bの非ゼロ要素数：",count_B)

check_A=0
check_B=0
if(na!=ma):
 print("Aは非対称行列")
else:
 for i in range(na):
  for j in range(ma):
   if(A[i][j]!=A[j][i]):
    check_A=check_A+1


if(nb!=mb):
 print("Bは非対称行列")
else:
 for i in range(nb):
  for j in range(mb):
   if(B[i][j]!=B[j][i]):
    check_B=check_B+1

if(check_A!=0):
  print("Aは非対称行列")
else:
  print("Aは対称行列")

if(check_B!=0):
  print("Bは非対称行列")
else:
  print("Bは対称行列")

"""
(py361) [16D8101021C@ise31c ~]$ python kadai05b.py
Aの非ゼロ要素数： 2468
Bの非ゼロ要素数： 2574
Aは対称行列
Bは非対称行列
"""
