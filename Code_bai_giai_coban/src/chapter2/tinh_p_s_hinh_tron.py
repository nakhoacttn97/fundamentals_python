'''
Created on Feb 2, 2017

@author: KTPHUONG
'''
# tinh dien tich va chu vi hinh tron
PI = 3.14
r = eval(input('Nhập bán kính:\n'))
p = 2 * PI * r
s = PI * r * r
print('p = 2 * %.2f * %d = %.2f'%(PI, r, p))
print('s = %.2f * %d * %d = %.2f'%(PI, r, r, s))
