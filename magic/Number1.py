#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#处理自定义对象类型处理 ,来验证魔术函数
class Number1(object):
    def __init__(self, value):
            self.value = value

    def __eq__(self, other):
        print('__eq__')
        return self.value == other.value

    def __ne__(self, other):
        print('__ne__')
        return self.value != other.value

    def __lt__(self, other):
        print('__lt__')
        return self.value < other.value

    def __gt__(self, other):
        print('__gt__')
        return self.value > other.value

    def __le__(self, other):
        print('__le__')
        return self.value <= other.value

    def __ge__(self, other):
        print('__ge__')
        return self.value >= other.value


if __name__ == '__main__':
    num1 = Number1(2)
    num2 = Number1(3)
    print('num1 == num2 ? --------> {} \n'.format(num1 == num2))
    print('num1 != num2 ? --------> {} \n'.format(num1 == num2))
    print('num1 < num2 ? --------> {} \n'.format(num1 < num2))
    print('num1 > num2 ? --------> {} \n'.format(num1 > num2))
    print('num1 <= num2 ? --------> {} \n'.format(num1 <= num2))
    print('num1 >= num2 ? --------> {} \n'.format(num1 >= num2))