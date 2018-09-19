#kadai09b 16D8101021C 野口大輔　2017-11-27

import numpy as np

def f(x):
 print("関数の引数",x)
 if x==0:
  print("戻値： 0")
  return x
 elif x==1:
  print("戻値: 1")
  return x
 else:
  re=f(x-1)+f(x-2)
  print("戻値:",re)
  return re

n=int(input("input n:"))
fib=f(n)

print("f(",n,")=",fib)


