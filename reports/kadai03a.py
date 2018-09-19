#kadai03a 16D8101021C 野口大輔　2017-10-9

import math as mt

a=int(input("整数aを入力してください"))
b=int(input("整数bを入力してください"))
c=int(input("整数cを入力してください"))


def ans1(a,b,c):
 if b*b-4*a*c>=0:
  x1=(mt.sqrt(b*b-4*a*c)-b)/(2*a)
  return x1
 else:
  return False


def ans2(a,b,c):
 if b*b-4*a*c>=0:
  x2=(-mt.sqrt(b*b-4*a*c)-b)/(2*a)
  return x2

x1=ans1(a,b,c)
x2=ans2(a,b,c)

if x1==x2:
 print("解は",x1)
elif x1==False:
 print("解はありません")
else:
 print("解は",x1,"",x2)

"""
(py361) [16D8101021C@ise31c ~]$ python kadai03a.py
整数aを入力してください2
整数bを入力してください5
整数cを入力してください3
解は -1.0  -1.5
(py361) [16D8101021C@ise31c ~]$ python kadai03a.py
整数aを入力してください2
整数bを入力してください4
整数cを入力してください2
解は -1.0
(py361) [16D8101021C@ise31c ~]$ python kadai03a.py
整数aを入力してください1
整数bを入力してください2
整数cを入力してください3
解はありません

"""
