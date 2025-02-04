'''
Created on 2016. 10. 24.

일급함수 : 함수 안에 함수, 인자로 함수를 전달, 반환값이 함수인 경우
'''
def func1(a, b):
    return a + b
func2 = func1
print(func1(3, 4))
print(func2(3, 4))

print()
def func3(func):
    def func4(): #함수안에 함수
        #pass
        print('나는 내부함수') 
    func4()
    return func #반환값이 함수

mbc = func3(func1) #인자로 함수 전달
print(mbc(3, 4))

print()
#람다(lambda) : 이름이 없는 한 줄 짜리 함수 (축약함수, 무명함수), 내부적으로 return 사용
def hap(x, y):
    return x + y

print(hap(1,2))
print('위의 코드를 람다로 표현')
print((lambda x, y:x + y)(1, 2)) #형식 lambda 인자...:표현식

aa = lambda x, y:x * y #주소 치환
print(aa) #<function <lambda> at 0x1034c00d0>
print(aa(3,4))

print()
print('람다도 가변인수 지정이 가능')
bb = lambda a, *tu, **di:print(a) or print(tu) or print(di)
bb(1, 2, 3, m = 4, n = 5)

print('\n어떠한 함수의 인자로 lambda를 사용')
print(list(filter(lambda a:a < 5, range(10)))) #0부터 9까지를 a가 받아서 5보다 작은 수
print(list(filter(lambda a:a % 2, range(10)))) #0부터 9까지를 a가 받아서 2로 나눈 나머지 홀수



















