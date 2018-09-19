#kadai09a 16D8101021C 野口大輔　2017-11-27

import numpy as np

def fx(x):
 print("関数の引数:",x)
 if x!=1:
  answer=x*fx(x-1)
  print("戻値:",answer)
  return answer
 else:
  return 1

n=int(input("input n:"))

answer=fx(n)
print(n,"の階乗は",answer,"です")


"""
(py361) [16D8101021C@ise31c ~]$ python kadai09a.py
input n:10
関数の引数: 10
関数の引数: 9
関数の引数: 8
関数の引数: 7
関数の引数: 6
関数の引数: 5
関数の引数: 4
関数の引数: 3
関数の引数: 2
関数の引数: 1
戻値: 2
戻値: 6
戻値: 24
戻値: 120
戻値: 720
戻値: 5040
戻値: 40320
戻値: 362880
戻値: 3628800
10の階乗は 3628800 です
"""
