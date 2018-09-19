#kadai02c 16D8101021C 野口大輔　2017-10-02

ent_price=int(input("大人料金はいくらですか？"))

sum=0
sum_child=0
sum_old=0
cnt=0
ent_price_child=ent_price/2
ent_price_old=ent_price*0.8

while 1:
 age=int(input("入場者の年齢は？"))

 if age>12 and age<60:
  sum=sum+ent_price
  cnt=cnt+1
 elif age>=0 and age<=12:
  sum_child=sum_child+ent_price_child
  cnt=cnt+1
 elif age>=60:
  sum_old=sum_old+ent_price_old
  cnt=cnt+1
 else: break

if cnt>=5:
 sum=sum*0.9
 sum_child=sum_child*0.9
 sum_old=sum_old*0.9

sum_all=sum+sum_child+sum_old

print("6名の入場料合計は",sum_all,"円です")

"""
(py361) [16D8101021C@ise31c ~]$ python kadai02c.py
大人料金はいくらですか？1500
入場者の年齢は？60
入場者の年齢は？20
入場者の年齢は？10
入場者の年齢は？10
入場者の年齢は？40
入場者の年齢は？50
入場者の年齢は？-1
6名の入場料合計は 6480.0 円です


(py361) [16D8101021C@ise31c ~]$ python kadai02c.py
大人料金はいくらですか？1500
入場者の年齢は？10
入場者の年齢は？50
入場者の年齢は？70
入場者の年齢は？-1
6名の入場料合計は 3450.0 円です

"""

