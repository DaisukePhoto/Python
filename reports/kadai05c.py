#kadai05c 16D8101021C 野口大輔　2017-10-23
import numpy as np
import time
 
n=int(input("n:"))
np.random.seed(1)
A=np.random.randint(0,2,(n,n))
b=np.random.rand(0,2*n,n)
x=np.ones(n)


for i in range(n):
 for j in range(n):
  if(i==j):
   A[i][j]=A[i][j]+n

D=np.zeros((0,0))
L=np.zeros((0,0))
U=np.zeros((0.0))
for i in range(n):
 for j in range(n):
  if(i==j):
   D[i][j]=A[i][j]
  elif(i>j):
   L[i][j]=A[i][j]
  else:
   U[i][j]=A[i][j]



cnt=0
t1=time.time()
while(cnt<100 or np.linalg.norm(Ax-b>1e-6)):
 N=-(L+U)
 
 for j in range(n):
   x[j]=(np.dot(N[j],x)+b[j]/D[j][j]
 cnt=cnt+1

t2=time.time()

print("反復回数：",cnt,"回,計算時間：",t2-t1)
print("x=[")
print(x)
