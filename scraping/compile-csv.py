import csv

result=[]

f = open('article_tags_in.csv')
reader = csv.reader(f,delimiter=",")
#header = next(reader)  # ヘッダーを読み飛ばしたい時

for row in reader:
   print(row)
   result.append(row)

outname = "article_tags.csv"

with open(outname, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    writer.writerows(result)

f.close()