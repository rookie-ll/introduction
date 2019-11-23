import re

names=["_name","name","2name","name2","name!","n#123","_______"]

for i in names:
    a=re.match(r"^[a-zA-Z_][a-zA-Z_1-9]*$",i)
    if a:
        print("变量名%s可用,通过正则取出来的字符为：%s"%(i,a.group()))

    else:
        print("变量名%s不可用"%(i))