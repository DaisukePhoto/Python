#kadai11a 16D8101021C 野口大輔　2017-12-11
import numpy as np

s=[[55,66,77,15,16,17],
   [35,79,13,10,87,11],
   [14,30,20,99,19,12],
   [25,18,85,63,23,73],
   [21,91,31,61,22,44]]
#print(s.shape[0],s.shape[1])
f=np.zeros((5,6))
f[0][0]=s[0][0]
for q in range(5):
 f[0][q+1]=f[0][q]+s[0][q+1]

for p in range(4):
 f[p+1][0]=f[p][0]+s[p+1][0]

#print(f)
for q in range(1,6):
 for p in range(1,5):
  f[p][q]=min(f[p-1][q]+s[p][q],f[p][q-1]+s[p][q])

#print(f)
print("最短距離の総和は",int(f[4][5]))


"""
(py361) [16D8101021C@ise31c ~]$ python kadai11a.py
最短距離の総和は 361
"""
