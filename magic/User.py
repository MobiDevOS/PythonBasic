#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# __getattribute__ 定义了你的属性被访问时的行为，
# 相比较，__getattr__ 只有该属性不存在时才会起作用。
# 因此，在支持 __getattribute__ 的 Python 版本,
# 调用__getattr__ 前必定会调用 __getattribute__``
# __getattribute__ 同样要避免"无限递归"的错误。


class User(object):
    # 只有属性不存在的时候才会被调用
    def __getattr__(self, name):
        print('调用了 __getattr__ 方法')
        return super(User, self).__getattr__(name)

    def __setattr__(self, name, value):
        print('调用了 __setattr__ 方法')
        return super(User, self).__setattr__(name, value)

    def __delattr__(self, name):
        print('调用了 __delattr__ 方法')
        return super(User, self).__delattr__(name)

    def __getattribute__(self, name):
        print('调用了 __getattribute__ 方法')
        return super(User, self).__getattribute__(name)


if __name__ == '__main__':
    user = User()
    # 设置属性值，会调用 __setattr__
    user.attr1 = True
    # 属性存在,只有__getattribute__调用
    user.attr1
    try:
        # 属性不存在, 先调用__getattribute__, 后调用__getattr__
        user.attr2
    except AttributeError:
        print('获取attr2属性异常')
    # __delattr__调用
    del user.attr1