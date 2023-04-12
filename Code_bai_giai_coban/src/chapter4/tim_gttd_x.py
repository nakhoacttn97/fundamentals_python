'''
Created on Feb 9, 2017

@author: KTPHUONG
'''
# |x|
try:
    x = int(input('Nhập x:\n'))
    abs_x = x
    if abs_x < 0:
        abs_x = - abs_x
        print('|%d| = %d'%(x, abs_x))
except ValueError as err:
    print('Error:', err)    