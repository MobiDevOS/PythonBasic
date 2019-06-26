#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

## 枚举类型的比较


import enum


#集成Enum不能比较但是集成IntEnum则可进行大小比较
class User(enum.IntEnum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 12



if __name__ == '__main__':
    try:
        print('\n'.join(s.name for s in sorted(User)))
    except TypeError as err:
        print(' Error : {}'.format(err))
