
'''
Created on Jan 23, 2017

@author: KTPHUONG
'''
import math
# tinh S = (x*x + 1)^n
s = lambda x, n: math.pow(math.pow(x,2) + 1, n)

s_tron = lambda r: math.pi * math.pow(r,2)

print('S = ', s(2, 3))

print('S tròn=',s_tron(10))


s = 'Hello Python'
def in_s():
    print(s)
    return

in_s()
print(s)