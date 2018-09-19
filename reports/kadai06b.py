#kadai06b 16D8101021C 野口大輔　2017-10-30
import numpy as np
import time
import random
x=int(input("input x:"))
y=int(input("input y:"))
z=int(input("input z:"))
A=[]
t1=time.time()
for i in range(y):
 A.append(random.randint(1,x))
t2=time.time()
print("集合の生成時間：",t2-t1)

t3=time.time()
A.sort()
t4=time.time()
print("並べ替え時間：",t4-t3)

check1=0
check2=0
time1=time.time()
if z in A:
 time2=time.time()
 print("手法１：要素",z,"を発見")
 print("計算時間：",time2-time1)
 check1=1
if check1==0:
 print("手法１：要素はありません")


left=A[0]
right=A[y-1]
center=int(left+right)
count=0
time3=time.time()
while z!=center:
  if center>z:
   right=center
   center=int(left+right)
   count=count+1
   if count>y:
    break
  elif center<z:
   left=center
   center=int(left+right)
   count=count+1
   if count>y:
    break
  elif center==z:
   time4=time.time()
   print("手法２：要素",z,"を発見")
   print("計算時間：",time4-time3)
   check2=1

if check2==0:
 print("手法２：要素はありません")
  
