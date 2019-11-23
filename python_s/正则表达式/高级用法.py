import re
a=re.search(r"\d+","阅读次数=99999").group()
print(a)

b=re.findall(r"\d+","我=111，他=222，他们=333")
print(b)

#sub将匹配到的字符串替换

c=re.sub(r"\d+","333333","python=2222")
print(c)