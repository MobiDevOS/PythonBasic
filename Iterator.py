#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#迭代器的使用
if __name__=='__main__':
    # 1、字符创创建迭代器对象
    str1 = 'liangdianshui'
    iter1 = iter ( str1 )

    # 2、list对象创建迭代器
    list1 = [1,2,3,4]
    iter2 = iter ( list1 )

    # 3、tuple(元祖) 对象创建迭代器
    tuple1 = ( 1,2,3,4 )
    iter3 = iter ( tuple1 )

    # for 循环遍历迭代器对象
    for x in iter1 :
        print ( x , end = ' ' )

    print('\n------------------------')

    # next() 函数遍历迭代器
    while True :
        try :
            print ( next ( iter3 ) )
        except StopIteration :
            break



    str = 'zhujiuleisbestman'
    iterstr = iter( str );

    tableTest = {"name":"zhujiule","age":"23"}
    tableIter = iter ( tableTest )
    while True :
        try :
            key = next ( tableIter )
            value = tableTest.get(key)
            print ( value , end = '')
        except StopIteration:
            break
        else:
            print("over")
