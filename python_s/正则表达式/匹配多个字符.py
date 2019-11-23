import re

print(re.match(r"我要匹配的数据[0-9]","我要匹配的数据1").group())
print(re.match(r"我要匹配的数据[\d{1,2}]","我要匹配的数据2"))
print(re.match(r"\d{11}","111155555555511114411111").group())#大括号里面的一个属表示必须有多少位，俩个数表示一个范围

#问号前面的东西可有可无
print(re.match(r"1231_？23","123123"))

strr='''owowwoowowowosdfslkfjaslf
sdfsaf
sfsdf
saf
sadf
sdf
'''
print(re.match(r".*",strr,re.S).group())