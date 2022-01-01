import pymysql
import re

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='test',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

with open(r"/Users/vancir/Documents/wx/Vancir/fish.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.+[\u4E00-\u9FFF]\s\(.+\):"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        if (line.startswith('Vancir') or line.startswith('鱼宝')):
            filter_lines.append(line.strip())

for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = line[s1 + 2:s2]
    content = line[s2 + 2:]
    print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{pymysql.converters.escape_string(content)}')"
    cur.execute(insert_sql)
conn.commit()
