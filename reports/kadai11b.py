#kadai11b 16D8101021C 野口大輔　2017-12-11

import numpy as np

A=np.loadtxt("matrix.csv",delimiter=",",dtype=int)

print("行数：",A.shape[0])
print("列数：",A.shape[1])

f=np.zeros((A.shape[0],A.shape[1]))

f[0][0]=A[0][0]
for q in range(A.shape[1]-1):
 f[0][q+1]=f[0][q]+A[0][q+1]

for p in range(A.shape[0]-1):
 f[p+1][0]=f[p][0]+A[p+1][0]

#print(f)
for q in range(1,A.shape[1]):
 for p in range(1,A.shape[0]):
  f[p][q]=min(f[p-1][q]+A[p][q],f[p][q-1]+A[p][q])
 
#print("\n",f)
print("最短距離の総和は",int(f[A.shape[0]-1][A.shape[1]-1]))

"""
(py361) [16D8101021C@ise31c ~]$ python kadai11b.py
行数： 79
列数： 80
最短距離の総和は 421739
"""
