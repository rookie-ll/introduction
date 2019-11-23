import re
a=re.match(r"[1-9]?","22").group()
print(a)
b=re.match(r"1{1,2}","111").group()
print(b)
