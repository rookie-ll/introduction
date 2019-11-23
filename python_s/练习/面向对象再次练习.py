class Class(object):
    names="我是类属性"
    def __init__(self):
        self.name="hahahaha"

    def get_name(self):
        print(self.name)

    @classmethod
    def class_method(cls):
        print(cls.names)
        print(cls.name)

class Student(Class):
    def __init__(self):
        super(Student, self).__init__()
    def get_f_name(self):
        print(self.name)
        super().get_name()

#class1=Class()
#class1.get_name()
student=Student()
student.get_f_name()
