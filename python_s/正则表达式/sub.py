import re
import urllib
with open("index.html","r",encoding="utf-8") as f:
     c=f.read()
print(c)
a=list()
for i in range(10):
    a.append(i)


name=""

connt=re.sub(r"\{%c%\}","ssdfsf",c)
print(connt)