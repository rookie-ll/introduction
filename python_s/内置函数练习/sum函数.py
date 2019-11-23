"""
sum(iterable[, start])
参数
iterable -- 可迭代对象，如：列表、元组、集合。
start -- 指定相加的参数，如果没有设置这个值，默认为0。
返回值
返回计算结果。

"""
s = sum(range(1, 101))
print(s)

s2 = sum([1, 2, 3, 4, 5], 200)
print(s2)
