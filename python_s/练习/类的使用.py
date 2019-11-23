class Tool():
    toosun = 0

    def __init__(self, name):
        self.name = name
        Tool.toosun += 1

    @staticmethod
    def sayhello():
        print("hello")

    @classmethod
    def toolclass(cls):
        print(cls.toosun)


tooo1 = Tool("斧头")
tooo1=Tool("榔头")
sun = Tool.toolclass()
