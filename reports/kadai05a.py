#kadai05a 16D8101021C 野口大輔　2017-10-23

import numpy as np
import time 

n=int(input("n:"))
A=np.random.randint(0,2,(n,n))
B=np.random.randint(0,2,(n,n))
C=np.empty((n,n))
D=np.empty((n,n))

print("生成完了")
t1=time.time()
C=A+B
t2=time.time()

C=np.zeros((n,n))
t3=time.time()
for i in range(0,n):
 for j in range(0,n):
  C[i][j]=A[i][j]+B[i][j]
t4=time.time()

t5=time.time()
D=np.dot(A,B)
t6=time.time()

D=np.zeros((n,n))
t7=time.time()
for i in range(0,n):
 for j in range(0,n):
  for k in range(0,n):
   D[i][j]=A[i][k]*B[k][j]
t8=time.time()

print("手法1",t2-t1)
print("手法2",t4-t3)
print("手法3",t6-t5)
print("手法4",t8-t7)


"""
(py361) [16D8101021C@ise31c ~]$ python kadai05a.py
n:300
生成完了
手法1 0.0007412433624267578
手法2 0.11752629280090332
手法3 0.026491165161132812
手法4 30.809123754501343
"""
