import re
file="test.txt"
with open(file,"r",encoding="utf-8") as f:
    files=f.read()
    print(files)


ff=re.findall(r'<div.*>(\w)</div>',files)
print(ff)

