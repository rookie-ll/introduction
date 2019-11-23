def set_lv(lv):
    def func(fun):
        def funn(*args,**kwargs):
            if lv==1:
                print("俺是权限验证一级")
            elif lv==2:
                print("俺是权限验证二级")
            return fun()
        return funn
    return func

@set_lv(1)
def text1():
    print("权限验证一通过")

@set_lv(2)
def text2():
    print("权限验证二通过")

text1()
text2()
