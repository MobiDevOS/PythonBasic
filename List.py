#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 集合生成器 注意关键字yield
#生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据
#生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，
# 但是，不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，
# 这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器
if __name__=='__main__':

    list1 = list(range(1,30))
    print(list1)


    #直接打印99乘法表
    print('\n'.join([' '.join ('%dx%d=%2d'% (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))

    # 1x1= 1
    # 1x2= 2 2x2= 4
    # 1x3= 3 2x3= 6 3x3= 9
    # 1x4= 4 2x4= 8 3x4=12 4x4=16
    # 1x5= 5 2x5=10 3x5=15 4x5=20 5x5=25
    # 1x6= 6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36
    # 1x7= 7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49
    # 1x8= 8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64
    # 1x9= 9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81


    #分解以上生成器操作
    #[expr for iter_var in iterable]
    #[expr for iter_var in iterable if cond_expr]

    #前面这个表达式用作为匿名函数 通过后面x迭代获取值以后执行
    lsit1=[x * x for x in range(1, 11)]
    print(lsit1)

    #按照条件迭代
    lsit1= [x * x for x in range(1, 11) if x % 2 == 0]
    print(lsit1)


    #嵌套打印，这里两个for生成器实现了一个嵌套
    lsit1= [(x+1,y+1) for x in range(3) for y in range(5)]
    print(lsit1)
    #打印结果
    #[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]




    #测试生成器
    gen = (x * x for x in range(10))

    for num  in  gen :

        print(num,end=' ')





    #斐波那契数列
    def fibon(n):
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b
        #相当于 t = a+b a=b b=t 这里yield a 相当于每次保存了上一次a的值 并挂起当第二次循环执行到的时候 继续处理下面的任务
    print('\n 测试函数作为生成器')
    # 引用函数
    for x in fibon(10):
      print(x , end = ' ')


    # 集合生成器 yield 相当于挂起，只有执行到的时候 只有执行到的时候 才会处理 变向的介申乐内存 。