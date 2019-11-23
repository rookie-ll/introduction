#match从头匹配
#search不会从头匹配，只要符合要求就匹配到了,且只能匹配一个，findall可以匹配多个，sum可以将匹配到的数据进行替换
#split切割字符串

import re

print(re.search(r"\d+","wo司搭街坊拉萨解放撒6656 sfsdsdf6 sdf 6").group())
print(re.findall(r"\d+","wo司搭街坊拉萨解放撒6656 sfsdsdf6 sdf 6"))#findall直接返回数据，不需要group
print(re.sub(r"\d+","0000","wo司搭街坊拉萨解放撒6656 sfsdsdf6 sdf 6"))

print(re.split(r":| ","ww:sdfk j sfj lsdf lj:s a"))