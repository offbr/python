#!/usr/local/bin/python3.5

import cgi

form = cgi.FieldStorage()

name = form['name'].value
tel = form["tel"].value
gen = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html><body>
이름은 {0}, 전화는 {1}, 성별은 {2}
</body></html>
'''.format(name, tel, gen))




'''
import cgi
form = cgi.FieldStorage()

name = form.getvalue('name') #request.getparameter
gen = form.getvalue('gen') #request.getparameter
phone = form["tel"].value #request.getparameter

print('content type:text/html;charset=utf-8\n')
print(
    
    <html><body>
    
    name {0}
    tel {1}
    gen {2}
    </body></html>
    .format(name,phone,gen)
)

'''
