import pymysql
from rich.progress import track
from collections import defaultdict

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='test',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

cur.execute("select * from log")

r = cur.fetchall()
result = {}

pics = 0
max_date = ""
max_content = ""
month = defaultdict(int)
for item in r:
    date = item[1]
    # date = date[:date.find(":", len("021-09-20 10:32:22"))]
    # print(item[0])
    content = item[2]
    # if not date[-1].isnumeric():
    #     continue 
    if len(date) != len("2021-12-29 06:13:14 PM"):
        continue
    # print(date)

    mon = date[11:13]
    if "PM" in date:
        
        mon = str(int(mon) + 12)
    month[mon] += 1
print(month)
