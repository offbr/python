'''
List : 다양한 형태의 자료 저장. []를 사용. 순서O. 수정O. 중복O
'''

a = [1, 2, 3]
b = [10, a, 20.5, True, '안녕']
print(a, id(a))
print(b, id(b))

print()
friends = ['오공', '팔계', '삼장']
print(friends, len(friends), friends[1])

friends.append('관우')
friends.remove('팔계')
friends.insert(0, '장비')
friends.extend(['조조', '제갈량'])
friends += ['손권']
print(friends)

print('오공인 친구 : ', '오공' in friends) #True
print('팔계인 친구 : ', '팔계' in friends) #False

print()
aa = [1,2,3,4,5,1,2]
print(aa, aa[0:5:2]) #0번쨰에서부터 
aa = [1,2,3,['a','b', 'kbs'],4,5 ]
aa[0] = 100
aa[3][0] = 'good'
print(aa)
print(aa[1], aa[3][1])

print()
aa.remove(4) #값에 의한 삭제
del aa[4]   #순서에 의한 사겢
print(aa)

print()
aa = [3,1,5,2,4]
aa.sort(reverse=True) #reverse=True desc none asc
print(aa)

print()
aa2 = ['123', '34', '234']
print(aa2)
aa2.sort()
print(aa2)
aa2.sort(key=int, reverse=False)
print(aa2)

print()
aa2 = [3,1,2]

aa3 = sorted(aa2)
print(aa2, aa3)

#deepcopy
#짧은 복사
name1 = ['tom', 'james', 'oscar']
name2 = name1
print(name1, id(name1))
print(name2, id(name2))
name1[0] = 'john'
print(name1, name2)

print()

#깊은 복사
import copy
name3 = copy.deepcopy(name1)
name1[0] = 'charles'
print(name1, name2, name3) 

print('\n stack(LIFO) / queue(FIFO)')
#stack
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop()
print(sbs)
sbs.pop()
print(sbs)
#queue
print() 
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop(0)
print(sbs)
























