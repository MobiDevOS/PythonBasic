
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""测试main函数入门"""
if __name__=='__main__':

    #基础层级测试
    a = 8
    b = 9
    if a>10:
        if b>10:
            print(b)
    print(a)



    #基础函数测试
    def sum(num1,num2):
        # 两数之和
        if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
            raise TypeError('参数类型错误')
        return num1+num2

    print(sum(1,2))


    #函数返回多个值测试
    def  division ( num1, num2 ):
        # 求商与余数
        a = num1 % num2
        b = (num1-a) / num2
        return b , a

    num1 , num2 = division(9,4)
    tuple1 = division(9,4)

    print (num1,num2)
    print (tuple1)



    #测试必须按照 特定名称传值 如age  *,age 是一体的 * 后面所有的参数必须要按照指定名称来传值
    def print_user_info( name , *,age  , sex = '男' ):
        #打印用户信息
        print('昵称：{}'.format(name) , end = ' ')
        print('年龄：{}'.format(age) , end = ' ')
        print('性别：{}'.format(sex))
        return;

    print_user_info( '张三',age='12',sex='女')




    #* hobby指的是一个可变长的元组，** hobby表示一个指定关键字的元组
    def print_user_info( name ,  age  , sex = '男' , ** hobby ):
        # 打印用户信息
         print('昵称：{}'.format(name) , end = ' ')
         print('年龄：{}'.format(age) , end = ' ')
         print('性别：{}'.format(sex) ,end = ' ' )
         print('爱好：{}'.format(hobby))
         return;
    print_user_info(12,23,'女',hobby=('234','343','43434'))


    #测试匿名函数 输出结果100001 表示执行的时候才确定数值
    num2 = 100
    sum1 = lambda num1 : num1 + num2 ;

    num2 = 10000
    sum2 = lambda num1 : num1 + num2 ;
    print( sum1( 1 ) )
    print( sum2( 1 ) )


    #################
    #   测试迭代     #
    #################

    # 1、for 循环迭代字符串
    for char in 'liangdianshui' :
        print ( char , end = ' ' )
    print('\n')

    # 2、for 循环迭代 list
    list1 = [1,2,3,4,5]
    for num1 in list1 :
        if num1 == 3:
            continue
        print ( num1 , end = ' ' )
    print('\n')

    # 3、for 循环迭代 （字典）
    dict1 = {'name':'张珊','age':'23','sex':'男'}
    for key in dict1 :    # 迭代 dict 中的 key
        print ( key+":",end = ' ')
        print ( dict1.get(key),end = ' ')
    print('\n')

    for value in dict1.values() :   # 迭代 dict 中的 value
        print ( value , end = ' ' )
    print ('\n')


    # 如果 list 里面一个元素有两个变量，也是很容易迭代的
    for x , y in [ (1,'a') , (2,'b') , (3,'c') ] :
        print ( x , y )



