import csv

csv_file = open("out.csv", "r", encoding="utf-8", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

ans = []
for row in f:
    if len(row) >= 5:
        del row[5:]
        ans.append(row)
        
with open("5row.csv", "w") as f:
    write = csv.writer(f)
    write.writerows(ans)