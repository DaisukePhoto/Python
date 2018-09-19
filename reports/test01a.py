#test01a 16D8101021C  野口大輔　2017-11-20

n=int(input("正の整数を入力してください:"))

if n<0:
 print("プログラムを終了します")
 exit(1)
elif n==1:
 print("1 は素数ではありません")
 exit(1)

check=0
for i in range(2,n):
 if n%i==0:
  check=1

if check==0:
 print(n,"は素数です")
else:
 print(n,"は素数ではありません")
  

"""

(py361) [isetest41@ise31c ~]$ python test01a.py
正の整数を入力してください:111
111 は素数ではありません
(py361) [isetest41@ise31c ~]$ python test01a.py
正の整数を入力してください:11
11 は素数です
(py361) [isetest41@ise31c ~]$ python test01a.py
正の整数を入力してください:1
1 は素数ではありません
(py361) [isetest41@ise31c ~]$ python test01a.py
正の整数を入力してください:-1
プログラムを終了します

"""
