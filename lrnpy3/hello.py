# -*- coding: utf-8 -*-

import logging
import math
import os
from functools import reduce

# log config
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' 
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"./hello.log" 
                    )


# self-defined function
def gabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    
    if x >= 0:
        return x
    else:
        return -x

# self-defined function
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

'''
name = input('Please enter your name: ')
print('hello ', name)
'''

# print absolute value of an integer
"""
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
"""

# self-defined function
"""

    
print("absolute value of -99 is: %i" % gabs(-99))
print("absolute value of 99 is: %s" % gabs(99))
"""

# print("nx is %s, ny is %s." % move(10,10,1,30))

# app01: to make a list
"""
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print('list L is %s' % L)
print('the first 10 elements of list L is %s' % L[0:10])
"""

# ex-list all dirs and files
"""
df = [d for d in os.listdir('.')]
print('dirs & files : %s' % df)
"""

# ex-get string elements from a list
"""
L1 = ['Hello', 18, 'MY', 32, 'wORld']
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print('List with string elements only of L1: %s' % L2)
"""

# ex -- high-order function
'''
def gadd(x, y, f):
    return f(x) + f(y)

a = gadd(5, -6, abs)
print('a = %s' % a)
'''

# ex -- high-order function
'''
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

listByName = sorted(L, key=by_name)
listByScore = sorted(L, key=by_score)

print('list to be sorted: %s' % L)
print('sorted by name: %s' % listByName)
print('sorted by score: %s' % listByScore)
'''

# ex -- class
'''
class Student(object):

    def __init__(self, name, gender):
        self.__name   = name
        self.__gender = gender

    def set_gender(self, gender):
        if gender == 'M' or gender == 'F':
            self.__gender = gender
        else:
            raise ValueError('bad gender. F or M is expected.')
    
    def get_gender(self):
        return self.__gender

if __name__ == '__main__':
    george = Student('George Dong', 'M')
    print(george.get_gender())
    george.set_gender('F')
    print(george.get_gender())

elsa = Student('Elsa Donne', 'Female')
print('elsa is %s' % elsa.get_gender())
elsa.set_gender('Female')
'''

# ex -- class
"""
class Screen(object):

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError('width must be an integer.')
        if width < 0 or width > 5000:
            raise ValueError('width must between 1 and 5000.')
        self.__width = width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError('height must be an integer.')
        if height < 0 or height > 5000:
            raise ValueError('height must between 1 and 5000.')
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height

s = Screen()
s.width  = 1024
s.height = 768
print('width = %s, height = %s' % (s.width, s.height))
print('resolution = %s' % s.resolution)        
"""

# ex -- class
'''
class Student(object):
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'STUDENT object (name: %s)' % self.name
    
    def __getattr__(self, attr):
        if attr == 'score':
            return 'score is unavaible, return 99 as default value.'
    
    __repr__ = __str__

# george = Student('George Donne')    
# print('name  = %s' % george.name)
# print('score = %s' % george.score)
# print('age   = %s' % george.age)

class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))
    
    def __str__(self):
        return self.__path
    
    __repr__ = __str__

chain = Chain()
print('0 = %s' % chain)
print('1 = %s' % chain.status)
print('2 = %s' % chain.status.user)
print('3 = %s' % chain.status.user.timeline)
print('4 = %s' % chain.status.user.timeline.list)

'''

# ex -- debug
'''
logging.basicConfig(level=logging.INFO)

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    # print("exp = %s" % exp)
    # print("ss = %s" % ss)
    logging.info('exp = %s' % exp)


    ns = map(str2num, ss)
    # print('ns = ', ns)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    
    # 7 is 7.6 in initial version.
    r = calc('99 + 88 + 7')
    print('99 + 88 + 7 =', r)

main()
'''

# ex --- read file
'''
fpath = '/etc/hosts'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
'''

# ex --- file i/o
'''
from datetime import datetime
import os

pwd = os.path.abspath('.')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d %s %s%s' % (fsize, mtime, f, flag))
'''

# ex --- re
'''
import re

str = 'a b   c'
print(re.split(r'\s+', str))

str = 'a,b, c   d'
print(re.split(r'[\s\,]+', str))

str = 'a,b;; c   d'
print(re.split(r'[\s\,\;]+', str))

tm = '23:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', tm)
print(m.group(0), m.group(1), m.group(2), m.group(3))
'''

# ex -- argparse
'''
import argparse

def main_arg():

    parser = argparse.ArgumentParser(
        prog        = 'backup',
        description = 'Backup MySQL database',
        epilog      = 'Copyright(r), 2003-2023'
    )

    parser.add_argument('outfile')
    parser.add_argument('--host', default = 'localhost')
    parser.add_argument('--port', default = 3306, type = int)
    parser.add_argument('-u', '--user', required = True)
    parser.add_argument('-p', '--password', required = True)
    parser.add_argument('--database', required = True)
    parser.add_argument('-gz', '--gzcompress', action = 'store_true', required = False, help = 'Compress backup files by gz.')

    args = parser.parse_args()

    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main_arg()
'''

# ex -- urllib
# there is something wrong with the ex demo, to be fixed later. -- George, on 2023-10-10 16:13

# from urllib import request, parse

'''
with request.urlopen('http://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
'''
    
'''
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

# ex -- gui
'''
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text = 'Hello', command = self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()

app.master.title('Hello World')
app.mainloop()
'''

# ex -- turtle gui

from turtle import *

# draw rectangle
'''
width(4)
forward(200)
right(90)

pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

done()
'''

# draw star
'''
def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()
'''

# ex -- tcp/ip
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))

print('sending...')
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
print('done.')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
'''

# ex -- tcp/ip, server and client on same host.

# logging.info('test starting...')
# logging.info('done')

'''
import socket

svr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
svr_socket.bind((host, port))

svr_socket.listen(5)

while True:
    
    clt_socket, addr = svr_socket.accept()
    msg = '连接地址：' + str(addr)
    print(msg)
    logging.info(msg)
    
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    clt_socket.send(msg.encode('utf-8'))
    clt_socket.close()
'''

# ex -- http

# function used in WSGI
'''
def gdhttpapp(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
# Type 'http://localhost:8000/George' in brower, and will get back 'Hello George!' on the screen.
'''
'''
# server
from wsgiref.simple_server import make_server
from hello import gdhttpapp

httpd = make_server('', 8000, gdhttpapp)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
'''

# ex -- http
'''
from flask import Flask, request, render_template

gdapp = Flask(__name__)

@gdapp.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('f-home.html')

@gdapp.route('/signin', methods = ['GET'])
def signin_form():
    return render_template('f-form.html')

@gdapp.route('/signin', methods = ['POST'])
def signin():
    user_name = request.form['username']
    password  = request.form['password']
    if user_name =='admin' and password =='password':
        return render_template('f-signin-ok.html', username = user_name)
    return render_template('f-form.html', message = 'Bad username or password', username = user_name)

if __name__ == '__main__':
    gdapp.run(debug=True)
'''

# ex -- coroutine

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def producer(c):
    c.send(None)
    
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
producer(c)
