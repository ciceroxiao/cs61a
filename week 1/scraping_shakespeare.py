"""此程序是 1.1 节中的示例代码，用于获取 shakespeare 的诗句
"""
from urllib.request import urlopen

# 此 URL 是一个文本链接，里面包含莎士比亚的 37 部戏剧的完整文本
url = "http://composingprograms.com/shakespeare.txt"

shakespeare = urlopen(url=url)

words = set(shakespeare.read().decode().split())

# 找到单词长度为 6，且正序、倒序都在文本中的单词
words_to_find = {w for w in words if len(w) == 6 and w[::-1] in words}

print(words_to_find)
