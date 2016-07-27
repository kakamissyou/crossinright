#coding=utf-8
__author__ = 'Administrator'
#演示不需要使用转义，并且可以换行的简单方法。
print '''
  He said, "I'm yours!"
  '''
print '''
  \\\_v_//
'''
print'''
"What's your name?" I asked.
"I'm Han Meimei."
'''
print '''
*
***
*****
***
*
'''

# 演示使用function doc的方法
def getUserName():
    '''return user'name by id'''
    return 1

print "=========================="
for i in range(0,5):
    for i in range(0,5):
        print "*",
    print

print "=========================="
for i in range(0,5):
    print "*",
print
print "=========================="
for i in range(0,5):
    print "*"
print
print "xxx=========================="
for i in range(0,5):
    for j in range(0,i+1):
        print "*",
    print






