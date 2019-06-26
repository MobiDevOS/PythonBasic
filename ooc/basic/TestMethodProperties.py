#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def testPass():
    a = 100
    if a > 100:
        pass
    else:
        print('pass')


class UserInfoProperties(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self._age


if __name__ == '__main__':
    userInfo = UserInfoProperties('两点水', 23, 347073565);
    # 打印所有属性
    print(dir(userInfo))
    # 打印构造函数中的属性
    print(userInfo.__dict__)
    # 直接使用类名类调用，而不是某个对象
    print(UserInfoProperties.lv)
    # 像访问属性一样调用方法（注意看get_age是没有括号的）
    print(userInfo.get_age)

# type(obj)：来获取对象的相应类型；
# isinstance(obj, type)：判断对象是否为指定的 type 类型的实例；
# hasattr(obj, attr)：判断对象是否具有指定属性/方法；
# getattr(obj, attr[, default]) 获取属性/方法的值, 要是没有对应的属性则返回 default 值（前提是设置了 default），否则会抛出 AttributeError 异常；
# setattr(obj, attr, value)：设定该属性/方法的值，类似于 obj.attr=value；
# dir(obj)：可以获取相应对象的所有属性和方法名的列表：
