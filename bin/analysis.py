import functools

import pymysql
import jieba
import json
from rich.progress import track

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

# 获得最长的一句话
max_item = None
for item in r:
    try:
        content = item[2]
        if (max_item is None or len(content) > len(max_item[2])) and content.find('http') == -1 and "耿元" not in content and "合拍" not in content and "破坏" not in content:
            max_item = item
    except:
        print("[x]", item)
print(max_item)

# # 进行分词
word_arr = []
for item in track(r):
    try:
        content = item[2]
        seg_list = jieba.cut(content)
        word_arr = word_arr + list(seg_list)
    except:
        print("[xx]", item)
word_count_map = {}
for word in word_arr:
    if word in word_count_map:
        word_count_map[word] = word_count_map[word] + 1
    else:
        word_count_map[word] = 1
word_count_arr = []
for word in word_count_map:
    o = {
        'word': word,
        'count': word_count_map[word]
    }
    word_count_arr.append(o)


def custom_sort(x, y):
    if x['count'] > y['count']:
        return -1
    if x['count'] < y['count']:
        return 1
    return 0


result['word'] = sorted(word_count_arr, key=functools.cmp_to_key(custom_sort))

with open("result.json", "w", encoding="utf-8") as f:
    f.write(
        json.dumps(result, ensure_ascii=False)
    )
