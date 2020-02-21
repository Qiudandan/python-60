class Dog(object):
    def __init__(self, name, dtype):
        # 定义类的属性
        # self.name = name 公有属性
        # self.__name = name 私有属性

        self.name = name
        self.dtype = dtype

        # 定义类的方法
    def shout(self):
        print('I\'m %s, type: %s' % (self.name, self.dtype))
