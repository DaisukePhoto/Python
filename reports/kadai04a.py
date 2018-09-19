#kadai04a 16D8101021C 野口大輔　2017ー10ー16

import numpy as np
import time

n=int(input("n:"))

A=np.random.randint(5,10,(n,n))
B=np.empty((n,n))
C=np.empty((n,n))
for i in range (0,n):
 for j in range (0,n):
  B[i][j]=int((i+j)%10)
  

for i in range (0,n):
 for j in range (0,n):
  C[i][j]=A[i][j]+B[i][j]

print("A=")
for i in range (0,n):
 print(A[i])

print("B=")
for i in range (0,n):
 print(B[i])
print("C=")
for i in range (0,n):
 print(C[i])


"""(py361) [16D8101021C@ise31c ~]$ python kadai04a.py
n:6
A=
[8 9 9 7 6 7]
[9 6 9 8 9 9]
[6 9 6 7 6 7]
[6 9 5 7 5 6]
[6 9 6 7 6 8]
[5 5 8 7 8 9]
B=
[ 0.  1.  2.  3.  4.  5.]
[ 1.  2.  3.  4.  5.  6.]
[ 2.  3.  4.  5.  6.  7.]
[ 3.  4.  5.  6.  7.  8.]
[ 4.  5.  6.  7.  8.  9.]
[ 5.  6.  7.  8.  9.  0.]
C=
[  8.  10.  11.  10.  10.  12.]
[ 10.   8.  12.  12.  14.  15.]
[  8.  12.  10.  12.  12.  14.]
[  9.  13.  10.  13.  12.  14.]
[ 10.  14.  12.  14.  14.  17.]
[ 10.  11.  15.  15.  17.   9.]
"""
