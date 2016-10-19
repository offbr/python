'''
자료형과 연산자
'''
A=3
a=4
print(A, a)

import keyword
print('사용자명으로 쓰지말아야 할 키워드목록: ', keyword.kwlist) #이미 사용하고 있는 것들

print()
print(10, oct(10), hex(10), bin(10)) 
print(10, 0o12, 0xa, 0b1010)

print()
#다 객체
print(3, type(3))   #정수
print(3.5, type(3.5)) #실수
print(3 + 4j, type(3+4j))
print(True, type(True))
print('abc', type('abc'))
print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))

print('\n연산자----------')
v1 = 3
v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2 #값을 맞바꿀때 임시변수를 안잡아도 된다.
print(v1, v2)

print('packing 연산')
v1, *v2 = 1,2,3,4,5 #배열로 들어간다 list타입
print(v1, v2)

*v1, v2 = 1,2,3,4,5 #배열로 들어간다 list타입
print(v1, v2)

v1, *v2, v3 = 1,2,3,4,5
print(v1, v2, v3)
# v1, *v2, *v3 = 1,2,3,4,5 #err

print()
print(5 + 3, 5 - 3, 5 * 3, 5 / 3)
print(5 / 3, 5 // 3, 5 % 3) # '//'몫만 가진다 , '%'나머지만 가진다.

print(divmod(5, 3)) #(1, 2)

print(3 + 4 * 5, (3 + 4) * 5)
print(5 > 3, 5 == 3, 5 != 3)
print(5 > 3 and 4 <= 3, not(True))

print('한국' + '인')
print('한국' * 20)

a = 10
a = a + 1
a += 1
print(a)

#a++, ++a, --a, a--
print(a, a * -1, -a, --a)

print('boo l: ', bool(0), bool(1), bool(10), bool(-20), bool('kbs'))
print(bool(None), bool(''), bool([]), bool(()), bool({}))
print((1 / 10, 1.0 / 10))

print(3 + 4, str(3) + '4', 3 + int('4'))

print('\n\a\b\tgood')

print('c:\nbc\abc\bb.txt')
print(r'c:\nbc\abc\bb.txt') #raw string을 사용하면 일반자료로 인정 / 이스케이프탈출






















