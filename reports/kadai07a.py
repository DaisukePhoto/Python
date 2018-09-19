#kadai07a 16D8101021C　野口大輔　2017-11-13

import numpy as np

kk=int(input("kk:"))
P=[[0.6,0.3,0.1],[0.3,0.6,0.1],[0.2,0.3,0.5]]
A=[[[0 for j in range(3)] for i in range(3)]for k in range(kk+1)]

for j in range(3):
 for i in range(3):
  A[0][i][j]=P[i][j]
for l in range(1,kk+1):
  A[l]=np.dot(A[l-1],P)


print("k=0:")
print(np.round(P,6))

for i in range(1,kk+1):
 print("k=",i)
 print(np.round(A[i],6))

"""
kk:10
k=0:
[[ 0.6  0.3  0.1]
 [ 0.3  0.6  0.1]
 [ 0.2  0.3  0.5]]
k= 1
[[ 0.47  0.39  0.14]
 [ 0.38  0.48  0.14]
 [ 0.31  0.39  0.3 ]]
k= 2
[[ 0.427  0.417  0.156]
 [ 0.4    0.444  0.156]
 [ 0.363  0.417  0.22 ]]
k= 3
[[ 0.4125  0.4251  0.1624]
 [ 0.4044  0.4332  0.1624]
 [ 0.3869  0.4251  0.188 ]]
k= 4
[[ 0.40751  0.42753  0.16496]
 [ 0.40508  0.42996  0.16496]
 [ 0.39727  0.42753  0.1752 ]]
k= 5
[[ 0.405757  0.428259  0.165984]
 [ 0.405028  0.428988  0.165984]
 [ 0.401661  0.428259  0.17008 ]]
k= 6
[[ 0.405129  0.428478  0.166394]
 [ 0.40491   0.428696  0.166394]
 [ 0.40349   0.428478  0.168032]]
k= 7
[[ 0.404899  0.428543  0.166557]
 [ 0.404834  0.428609  0.166557]
 [ 0.404244  0.428543  0.167213]]
k= 8
[[ 0.404814  0.428563  0.166623]
 [ 0.404794  0.428583  0.166623]
 [ 0.404552  0.428563  0.166885]]
k= 9
[[ 0.404782  0.428569  0.166649]
 [ 0.404776  0.428575  0.166649]
 [ 0.404677  0.428569  0.166754]]
k= 10
[[ 0.40477   0.428571  0.16666 ]
 [ 0.404768  0.428572  0.16666 ]
 [ 0.404728  0.428571  0.166702]]
"""
