#kadai03c 16D8101021C 野口大輔　2017-10-9
def gcd(a,b):
 r=a%b
 while( r!=0):
  a=b
  b=r
  r=a%b
 return b

a=int(input("a"))
b=int(input("b"))
if a<b:
 tmp=a
 a=b
 b=tmp

gcd=gcd(a,b)

print("最大公約数は",gcd)
 

"""
(py361) [16D8101021C@ise31c ~]$ python kadai03c.py
a12
b20
最大公約数は 4
(py361) [16D8101021C@ise31c ~]$ python kadai03c.py
a188870
b165438
最大公約数は 202
"""
