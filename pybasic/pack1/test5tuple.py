'''
tuple : list와 유사. ()를 사용. 읽기전용. 검색속도가 빠름.
'''
#t = 'a', 'b', 'c'
t = ('a','b','c', 'a')
print(t, type(t))
imsi = ('a') # tuple 에서 하나 쓸때는 , 를 적용(적용 안할경우 스트링) 복수는 마지막에 안써줘도 된다
imsi2 = ('a',)
print(imsi, imsi2)
print(type(imsi), type(imsi2))
print(len(t), t.count('a'), t.index('b'))

print()
p = (1,2,3)
#p[1] = 100  #TypeError: 'tuple' object does not support item assignment
q = list(p)
print(q)
q[1] = 100
p = tuple(q)
print(p)

print()
t1 = (10, 20)
a, b = t1
b, a = a, b
t2 = a, b
print(t2)

print()
v = ('kor', 2, True)
(x, y, z) = v
print(x, y, z)

























