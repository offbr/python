'''
Created on 2016. 10. 25.

함수 장식자 : meta 기능이 있다.
'''
def func2(fn):
    return lambda : 'hello ? ' + fn()

def func1(fn):
    return lambda : 'welcome ' + fn()

def myfunc():
    return 'world'

my = func2(func1(myfunc))
print(my())

print('\n---Decorator 사용---')
@func2
@func1
def myfunc2():
    return '동동'

print(myfunc2())

my2 = myfunc2() #실행결과 치환
print(my2)
my3 = myfunc2 #주소 치환
print(my3())

















