#kadai01a 16D8101021C 野口大輔　2017-9-25
a=int(input("整数aを入力してください"))
b=int(input("整数bを入力してください"))
c=int(input("整数cを入力してください"))
max=a
if b>max:
 max=b
if c>max:
 max=c

sum=a+b+c
ave=sum/c

print("最大値は",max,"です")
print("平均値は",ave,"です")
