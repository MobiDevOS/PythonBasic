#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# 测试类的继承
class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


class UserExtend (UserInfo):
    def __init__(self, name, age, account, sex):
        super(UserExtend, self).__init__(name, age, account)
        self.sex = sex


if __name__ == '__main__':
    userExtend = UserExtend(name='两点水',age= 23,account= 347073565,sex='男')
    print(dir(userExtend))
    print(userExtend.get_account())
    # 测试类属性是否一致
    print(isinstance(userExtend,UserInfo))
    print(isinstance('str',str))

