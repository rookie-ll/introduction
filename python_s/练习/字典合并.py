dict1=dict(name="w1",age=1,sex="男")
print(dict1)
dict2=dict(name1="w2",age1=2,sex1="男")
print(dict2)

dict3=dict1.update(dict2)
print(dict3,"该方法没有返回值")
print(dict1)    