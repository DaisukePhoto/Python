#kadai10b 16D8101021C 野口大輔　2017-12-4
import numpy  as np
v=[5,3,7,8,5,5,9,6,4,7]
s=[6,4,8,10,7,5,8,8,5,9]

n=10
C=30
a=[100][100]
for i in range(0,n-1):
 a[i][0]=0
for j in range(0,C-1):
 a[0][j]=0

for i in range(1,n):
 for j in range(1,C):
  if s[i]<=i:
   if s[i]+a[i-1][j-v[i]]>a[i-1][j]:
    a[i][j]=s[i]+a[i-1][j-v[i]]
   else:
    a[i][j]=a[i-1][j]

  else:
   a[i][j]=a[i-1][j]
  

for j in range(C-1):
 print("\n")
 for i in range(n-1):
  print(a[i][j])
