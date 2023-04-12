'''
Created on Feb 14, 2017

@author: KTPHUONG
'''
import math

def tinh_gtbt(x,y):
    try:
        if (2*x + 7*y)==0 : 
            raise ZeroDivisionError('divisor must be <>0')
        A = math.sqrt((5*x - y)/(2*x + 7*y))
        return A
    except ZeroDivisionError as err:
        print('Error:',err)   

x = eval(input('Nhập x:\n'))
y = eval(input('Nhập y:\n'))
try:
    print('A =',tinh_gtbt(x,y))
except NameError as err:
    print(err)
        