# -*- coding: utf-8 -*-
#解决文件中存在中文的问题，而且必须放在源文件第一行，否则会报错。
__author__ = 'Administrator'

#演示python的数据类型转换

print 1+int('123')
print 'HelloWorld%s'%str(123)
print bool('')
print bool(' ')

def isEqual(num1,num2):
    if(num1>num2):
        print 'too big'
        return  False
    elif(num1<num2):
        print 'too small'
        return  False
    else:
        print 'Bingo!'
        return True

from random import randint

number = randint(1,100)
print 'The correct answer is %d'%number

flag = False

while flag == False:
    answer = input('please input a number between 1 to 100!')
    flag =isEqual(answer,number)

