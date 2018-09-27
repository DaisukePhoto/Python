#スプレッドシートからエクスポートした時の改行コードを変換するコード
import csv

result=[]

f = open('input.csv')
reader = csv.reader(f,delimiter=",")
#header = next(reader)  # ヘッダーを読み飛ばしたい時

for row in reader:
   print(row)
   result.append(row)

outname = "output.csv"

with open(outname, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    writer.writerows(result)

f.close()