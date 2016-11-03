'''
Created on 2016. 11. 1.

'''
import socket
import threading
import sys            

def Handle(socket):
    while True:
        data = socket.recv(1024)
        if not data:
            continue
        print(data.decode('utf-8'))
sys.stdout.flush() #캐시메모리삭제

name = input('채팅 아이디 입력:')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('', 9999))
cs.send(name.encode(encoding='utf_8', errors='strict'))

th = threading.Thread(target=Handle, args=(cs,))
th.start()

while True:
    msg = input()
    sys.stdout.flush() #캐시메모리삭제
    if not msg:continue
    cs.send(msg.encode('utf-8'))

cs.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        