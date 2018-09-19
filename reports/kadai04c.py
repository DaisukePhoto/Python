#kadai04c 16D8101021C 野口大輔　2017ー10ー16

import numpy as np
import time 
n=int(input("n:"))
A=np.random.randint(0,2,(n,n))
b=np.random.rand(0,n,n)
print("生成終了")
t1=time.time()
ai=np.linalg.inv(A)

x1=np.dot(ai,b)
t2=time.time()


t3=time.time()
x=np.linalg.solve(A,b)
t4=time.time()
print("手法１：",t2-t1,"秒")
print("手法２：",t4-t3,"秒")

"""
(py361) [16D8101021C@ise31c ~]$ python kadai04c.py
n:1000
生成終了
手法１： 0.07979631423950195 秒
手法２： 0.0037047863006591797 秒
(py361) [16D8101021C@ise31c ~]$ python kadai04c.py
n:3000
生成終了
手法１： 1.1541671752929688 秒
手法２： 0.02501964569091797 秒
(py361) [16D8101021C@ise31c ~]$ python kadai04c.py
n:5000
生成終了
手法１： 4.099584341049194 秒
手法２： 0.07086873054504395 秒
"""
