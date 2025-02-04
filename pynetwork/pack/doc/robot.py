'''
Created on 2016. 11. 3.

검색 로봇 연습
'''
import urllib.robotparser
'''
rp = urllib.robotparser.RobotFileParser('http://blog.daum.net/robots.txt')
rp.read()

print(rp)
print()
print(rp.can_fetch('mycrawler', 'http://blog.daum.net))
'''
crawler_name = 'python _daum_crawler'
mainpage = 'http://blog.daum.net/'

rp = urllib.robotparser.RobotFileParser(mainpage + 'robots.txt')
rp.read()

def canFetch(url):
    return rp.can_fetch(crawler_name, url)

res = canFetch(mainpage)
print(res)

print()
import urllib.request
web_res = urllib.request.urlopen('http://www.daum.net').read()
print(web_res)

import time, traceback

def getContent(url, delay = 3):
    time.sleep(delay)
    if not canFetch(url):
        print('fail: ', url)
        return None
    
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', crawler_name)]
        contents = opener.open(url).read()
    except Exception as e:
        print('err: ', e)
        traceback.print_exc() #error log 출력
        return None
    
    return contents

while True:
    contents = getContent(mainpage)
    print(contents)































