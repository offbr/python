'''
Created on 2016. 11. 1.

thread로 날짜, 시간 출력
'''
import time
now = time.localtime()

print('현재는 {}년 {}월 {}일'.format(now.tm_year, now.tm_mon, now.tm_mday))
print('현재는 {}시 {}분 {}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
print('오늘 요일 %d'%(now.tm_wday)) #월요일이 0
print('올해 몇번째 날 %d'%(now.tm_yday))

import threading
def cal_show():
    now = time.localtime()
    print('현재는 {0}년 {1}월 {2}일'\
          .format(now.tm_year, now.tm_mon, now.tm_mday), end = ' ')
    print('현재는 {}시 {}분 {}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
    
def run():
    while True:
        cal_show()
        time.sleep(1)

th = threading.Thread(target=run)  
th.start()
th.join()

print('프로그램 종료')      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        