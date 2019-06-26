# -*- coding: UTF-8 -*-

def printHello(self, name='Py'):
    # 定义一个打印 Hello 的函数
    print('Hello,', name)



if __name__ == '__main__':

    # type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
    # 创建一个 Hello 类
    Hello = type('Hello', (object,), dict(hello=printHello))

    # 实例化 Hello 类
    h = Hello()
    # 调用 Hello 类的方法
    h.hello()
    # 查看 Hello class 的类型
    print(type(Hello))
    # 查看实例 h 的类型
    print(type(h))
