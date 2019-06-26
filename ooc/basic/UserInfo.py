#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 测试类
class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


class UserInfo2(object):
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
    userInfo = UserInfo('两点水', 23, 347073565)
    # 打印所有属性
    print(dir(userInfo))
    # 打印构造函数中的属性
    print(userInfo.__dict__)
    print(userInfo.get_account())
    # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)

    userInfo2 = UserInfo2('两点水', 23, 347073565)
    # 测试读取方法按照属性类型
    print(userInfo2.get_age)
    # 测试类名读取方法
    print(UserInfo2.get_name())

else:
    print("it's not main enter")
