import re

# 查找
s1 = '<a href="https://www.baidu.com">Baidu</a>'
l = re.findall('href=\".*\"',s1)
print(l[0])


# 替换
s2 = '<a href="https://www.baidu.com">辛亥革命</a>'
s = re.sub('(?=>).*?(?=<)','戊戌变法',s2)
print(s)
