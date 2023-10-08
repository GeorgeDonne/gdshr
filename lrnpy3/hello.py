# -*- coding: utf-8 -*-

import math
import os

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