#!/usr/local/bin/python3.5
'''
Created on 2016. 11. 3.

db 자료 출력
'''
import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'test',
    'port' : 3306,
    'use_unicode' : True,
    'charset' : 'utf8'
}

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body><h2>상품자료</h2>')
print('<table border="1"><tr><td>코드</td><td>품명</td><td>수량</td><td>단가</td></tr>')
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    for d in datas:
        print('''
           <tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
           </tr> 
        '''.format(str(d[0]), str(d[1]), str(d[2]), str(d[3]))
        )
    

except Exception as e:
    print('처리 오류: ', e)
    
finally:
    cursor.close()
    conn.close()
    
print('</table></body></html>')



















