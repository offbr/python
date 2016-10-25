'''
Created on 2016. 10. 24.

인수 키워드 매핑
'''

def ShowGugu(start, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + ' 단 출력')
        
ShowGugu(2, 3)   
print()
ShowGugu(3)
print()
ShowGugu(start=2, end=3)
print()
ShowGugu(end=3, start=2)
print()
ShowGugu(2, end=3)
#ShowGugu(start=2, 3) #SyntaxError: positional argument follows keyword argument
#ShowGugu(end=4, 3) #SyntaxError: positional argument follows keyword argument

# 가변 인수 
def Func1(*ar): #동적 아귀먼트를 받을 수 있다
    print(ar)
    for i in ar:
        print(str(i) + ' ')
    
Func1(1, 2)
Func1(1, 2, 3, 4, 5)

print()
def Func2(a, *ar): #동적 아귀먼트를 받을 수 있다
    print(a)
    print(ar)
    
Func2(1)
Func2(1, 2, 3, 4, 5) #튜플타입
   
''' 
print()
def Func3(*ar, a): #가변인자는 뒤쪽에 있어야 한다. #TypeError: Func3() missing 1 required keyword-only argument: 'a'
    print(a)
    print(ar)

Func3(1, 2)
'''
   
print()
def Func4(a, b, *v1, **v2): 
    print(a, b)
    print(v1)
    print(v2)
    
Func4(1, 2)
Func4(1, 2, 3, 4, 5)
Func4(1, 2, 3, 4, 5, m=6, n=7)
    
print()
def Func5(a, b, c):    
    print(a, b, c)
    
Func5(1, 2, 3)
#tup = (10) #인트
#tup = (10, ) #튜플
tup = (10, 20) #튜플
dic = {'c':30}
Func5(*tup, **dic)  
print()
tup = ('go', 'python') #튜플
#dic = {'k':'nice'} #TypeError: Func5() got an unexpected keyword argument 'k' # 아귀먼트의 이름 하고 매핑 
dic = {'c':'nice'} # 아귀먼트의 이름 하고 매핑  
Func5(*tup, **dic)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


