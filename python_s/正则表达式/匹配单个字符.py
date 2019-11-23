import re
#re.match(r"我要匹配的数据","用户输入的数据")
print(re.match(r"我要匹配的数据[0-9]","我要匹配的数据1").group())
print(re.match(r"我要匹配的数据[0-9a-z]","我要匹配的数据s").group())
print(re.match(r"我要匹配的数据[\d]","我要匹配的数据2"))
print(re.match(r"我要匹配的数据[\w]","我要匹配的数据_"))#小写字母，大写字母，下划线，支持各种语言
print(re.match(r"我要匹配的数据[ \d]","我要匹配的数据 2"))#空格
print(re.match(r"我要匹配的数据[\s]","我要匹配的数据 2"))#空白字符
#大写字母正好与小写字母相反\d,\s,\w

# . 的范围是最宽广的