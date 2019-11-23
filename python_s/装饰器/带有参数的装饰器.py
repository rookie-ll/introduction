def func(fun):
    def func(*args,**kwargs):
        lv=args[0]
        if lv==1:
            print("俺是权限验证一级")
        elif lv==2:
            print("俺是权限验证二级")
        return fun()
    return func

@func
def text1():
    print("权限验证一通过")

@func
def text2():
    print("权限验证二通过")

text1(1)
text2(2)
