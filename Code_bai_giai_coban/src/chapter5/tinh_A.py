'''
Created on Feb 9, 2017

@author: KTPHUONG
'''
# A = (x2 + x + 1)^n + (x2 - x + 1)^n
n = int(input('Nhập n:\n'))
x = eval(input('Nhập x:\n'))
if n==0:
    A = 2
else:
    A1 = 1
    A2 = 1
    for i in range(0,n):
        A1 = A1 * (x * x + x + 1)
        A2 = A2 * (x * x - x + 1)
    A = A1 + A2
print('A = (x2 + x + 1)^n + (x2 - x + 1)^n =', A)  