#kadai01b 16D8101021C 野口大輔　2017-09-25

a=int(input("整数aを入力してください"))
b=int(input("整数bを入力してください"))
c=int(input("整数cを入力してください"))

x=[a,b,c]
sum=0
for j in range(a,b):
  if j%c==0:
   sum=sum+j

print(a,"以上",b,"未満で",c,"で割りきれる数の総和は",sum,"です")
