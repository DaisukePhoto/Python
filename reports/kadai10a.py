#kadai10a 16D8101021C 野口大輔　2017-12-4

n=int(input("input n:"))

fib=[0]*101
fib[1]=1

for i in range(2,101):
 fib[i]=fib[i-1]+fib[i-2]

print("f(",n,")=",fib[n])

"""
(py361) [16D8101021C@ise31c ~]$ python kadai10a.py
input n:10
f( 10 )= 55
(py361) [16D8101021C@ise31c ~]$ python kadai10a.py
input n:100
f( 100 )= 354224848179261915075
"""
