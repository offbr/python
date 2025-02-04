'''
Created on 2016. 11. 3.

html 자료 읽어서 한글 형태소 분석하고 단어 수 세기
'''
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Komoran

Komoran = Komoran() #kkma()

try:
    url = "http://media.daum.net/foreign/others/newsview?newsid=20161103090136916"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "lxml")
    #print(soup)
    
    wordlist = []
    
    for item in soup.findAll('p'):
        #print(item.contents[0])
        itemDesc = item.contents[0]
        itemDesc = itemDesc.replace('[','')
        itemDesc = itemDesc.replace(']','')
        itemDesc = itemDesc.replace('(','')
        itemDesc = itemDesc.replace(')','')
        #print(itemDesc)
        wordlist += Komoran.nouns(itemDesc)
        
    
    print('wordlist : ')     
    print(wordlist)
    print('단어수 : ', len(wordlist))
    
    print()
    wordcount = {}
    for i in wordlist:
        if i in wordcount:
            wordcount[i] += 1
        else:
            wordcount[i] = 1
    print('wordcount : ')
    print(wordcount)
    
    print()
    setdata = set(wordlist)
    print(setdata)
    print('단어수(중복제거) : ', len(setdata))
except Exception as e:
    print("err : ", e)






























