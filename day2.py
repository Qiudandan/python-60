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

        
     #   class Book(object):
     #     def __init__(self,name,sale):
     #         self.__name = name
     #         self.__sale = sale
     #     @property
     #     def name(self):
     #         return self.__name
     #     @name.setter
     #     def name(self,new_name):
     #         self.__name = new_name
     # 注意这种装饰器写法：name.setter，name 已经被包装为 property 实例，调用实例上的 setter 函数再包装 name 后就会可写。
