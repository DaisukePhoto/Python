#kadai06a 16D8101021C 野口大輔　2017-10-30
import numpy as np
import time
import random
x=int(input("input x:"))
y=int(input("input y:"))
z=int(input("input z:"))
A=[]
for i in range(y):
 A.append(random.randint(1,x))

print("集合の生成完了")

A.sort()
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

time3=time.time()
for i in range(y):
 if z==A[i]:
  time4=time.time()
  print("手法２：要素",z,"を発見")
  print("計算時間：",time4-time3)
  check2=1
  break
if check2==0:
 print("手法２：要素はありません")
  
"""
(py361) [16D8101021C@ise31c ~]$ python kadai06a.py
input x:1000
input y:500
input z:300
集合の生成完了
手法１：要素 300 を発見
計算時間： 1.71661376953125e-05
手法２：要素 300 を発見
計算時間： 0.00011849403381347656

(py361) [16D8101021C@ise31c ~]$ python kadai06a.py
input x:100000000
input y:50000000
input z:23456789
集合の生成完了
手法１：要素 23456789 を発見
計算時間： 0.7542459964752197
手法２：要素 23456789 を発見
計算時間： 2.9877638816833496

"""
