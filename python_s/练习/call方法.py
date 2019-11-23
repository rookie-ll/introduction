class TestCall():
    def __init__(self):
        self.name = "俺的名"

    def __call__(self, *args, **kwargs):
        print("hello")


calls = TestCall()

calls()
