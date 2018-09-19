#kadai04b 16D8101021C 野口大輔　2017ー10ー16

import numpy as np
import time 

n=int(input("n:"))
A=np.random.randint(0,2,(n,n))
B=np.random.randint(0,2,(n,n))

c=np.random.randint(0,2,n)

print("生成終了")
t1=time.time()
D=np.dot(A,B)

e=np.dot(D,c)
t2=time.time()


t3=time.time()
f=np.dot(B,c)
g=np.dot(A,f)
t4=time.time()

print("手法１：",t2-t1,"秒")
print("手法２：",t4-t3,"秒")

check=0
for i in range (0,n):
  if e[i]!=g[i]:
   check=check+1

if check==0:
 print("結果が一致しました")
else:
 print("結果が一致しません")


"""
(py361) [16D8101021C@ise31c ~]$ python kadai04b.py
n:1000
生成終了
手法１： 1.2150561809539795 秒
手法２： 0.0016450881958007812 秒
結果が一致しました

手法１ O(n**3)　
手法２ O(n**2)
"""
