#kadai02a 16D8101021C 野口大輔　2017-10-02

a=int(input("整数xを入力してください"))

sum=0

for i in range(3,a,3):
 sum=sum+i
for j in range(5,a,5):
 sum=sum+j
for k in range(15,a,15):
 sum=sum-k

print("求める合計値は",sum,)

"""
(py361) [16D8101021C@ise31c ~]$ python kadai02a.py
整数xを入力してください20
求める合計値は 78
(py361) [16D8101021C@ise31c ~]$ python kadai02a.py
整数xを入力してください1234567
求める合計値は 355636612814
"""
