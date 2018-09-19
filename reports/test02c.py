#test02c 16D8101021C 野口大輔　2018-1-22
import numpy as np

V=np.loadtxt("subsum.txt",dtype="int")

print("V=",V)
sum=0
print("要素数：",len(V))
len=len(V)
for i in range(len):
 sum=sum+V[i]
print("要素の総和：",sum )

t=int(input("input t:"))

subsum=0
for i in range(len):
 for j in range(i,len):
  subsum=V[i]
  if V[i]>t:
   continue
  else:
   if subsum==t:
    break
   else:
    subsum=subsum+V[j]
