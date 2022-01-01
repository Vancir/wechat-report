import json

with open("result.json") as f:
    result = json.load(f)

unwant = ["表情", "图片", "就是", "这个", "没有", "不是", "然后", "什么", "可以", '一个', "觉得", "但是", "还是",
          "自己", "哈哈哈哈", "因为", "时候", "现在", "这样", "怎么", "那个", "一下", "所以", "不会", "可能", "的话", ]

# words = []
# for d in result['word'][400:]:
#     word = d["word"]
#     count = d["count"]
#     if len(word) == 1:
#         continue
    
#     if word in unwant:
#         continue
#     words.append(word)
#     print(word)
#     if len(words) > 100:
#         break

for d in result['word']:
    word = d["word"]
    count = d["count"]
    if len(word) == 1:
        continue
    if "喜欢" in word:
        print(word, count)