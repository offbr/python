'''
제어문
'''
#if
no = 30
if no >= 5:
    print('크네')
    if no <= 20:
        print('와우')
    else:
        print('허걱')
else:
    print('작네')
    
print('end1')

#jum = int(input('점수입력:'))
jum = 90
print(jum + 10) #TypeError: Can't convert 'int' object to str implicitly
#print(jum + '점') #TypeError: unsupported operand type(s) for +: 'int' and 'str'

if 90 <= jum <= 100:
    print('우수')
elif 70 <= jum < 90:
    print('보통')
else:
    print('저조')
a = 3
result = a * 2 if a > 5 else a + 2 
print(result)


#while
a = 1 
while a <= 5:
    print(a, end=' ')
    a += 1

print()
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print('i=' + str(i) + ':j=' + str(j))
        j += 1
    print()
    i += 1

print()
a = 0
while a < 10:
    a += 1
    if a == 5: continue
    if a == 7: break #강제종료
    print(a)
else: #선택 옵션 (종료 형태에 따라 else를 만나거나 건너뛴다)
    print('정상종료')

print()
#for
for i in [1,2,3,4,5,1,2]:
    print(i, end = ' ')

print()
for i in (1,2,3,4,5,1,2):
    print(i, end = ' ')
     
print() 
for i in {1,2,3,4,5,1,2}:
    print(i, end = ' ')
 
print()
soft = {'java':'웹용', 'python':'만능', 'oracle':'db'}
for i in soft.items():
    #print(i)
    print(i[0], i[1])

print()
for i in soft.keys():
    print(i)
    
print()
for i in soft.values():
    print(i)

chars = []
ss = "대한민국은 좋은나라"
for i in ss:
    chars.append(i)
    
print(chars)
 
print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 2: continue
    if i == 4: break
    print(i, end= ' ')
else: 
    print('정상종료')

print()
print(sum([2, 5]))

#과일 값 계산하기
price = {'사과':1000, '감':300, '배':2000}
my = {'사과':5, '감':2}

bill = sum(price[f] * my[f] for f in my)
print('지불 총액 : {}원'.format(bill)) 
print() 
 


 
 
 
 
 
 
 
 
 
 
 
 










