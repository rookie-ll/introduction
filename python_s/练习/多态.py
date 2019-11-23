class Dog(object):
    def __init__(self,name):
        self.name=name

    def plays(self):
        print("%s在奔奔跳跳的玩耍"%self.name)

class Xiaotian(Dog):

    def plays(self):
        print("%s 飞天玩耍"%self.name)

class Per():
    def __init__(self,name):
        self.name=name

    def plays(self,dog):
        print("%s和%s玩耍啊"%(self.name,dog.name))

#wangcai=Dog("旺财")

wangcai=Xiaotian("飞天旺财")

xiaomin=Per("小明")

xiaomin.plays(wangcai)