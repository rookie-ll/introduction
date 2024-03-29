"""
描述
bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。

bool 是 int 的子类。

语法
以下是 bool() 方法的语法:

class bool([x])
参数
x -- 要进行转换的参数。
返回值
返回 True 或 False。

实例
以下展示了使用 bool 函数的实例：

#>>>bool()
False
#>>> bool(0)
False
#>>> bool(1)
True
#>>> bool(2)
True
#>>> issubclass(bool, int)  # bool 是 int 子类
True
"""
print(bool(1))