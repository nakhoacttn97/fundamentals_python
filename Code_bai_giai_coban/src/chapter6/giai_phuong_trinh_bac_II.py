'''
Created on Feb 14, 2017

@author: KTPHUONG
'''
# giai phuong trinh bac 2
from math import sqrt
print('Giải phương trình bậc 2: ax^2 + bx + c = 0')
a = eval(input('Nhập a:\n'))
b = eval(input('Nhập b:\n'))
c = eval(input('Nhập c:\n'))
if a == 0:
    # giai phuong trinh bac nhat
    print('Phương trình bậc 2 suy biến thành phương trình bậc 1:')
    if b==0 and c!=0:
        print('Phương trình vô nghiệm')
    elif b==0 and c==0: 
        print('Phương trình vô số nghiệm')
    else:
        print('Nghiệm = ', -c/b)
else:
    # giai phuong trinh bac hai
    print('Phương trình bậc 2:')
    delta = pow(b,2) - (4 *a * c)
    if delta < 0 :
        print('Phương trình vô nghiệm')
    elif delta ==0:
        print('Phương trình có nghiệm kép x1 = x2 =', -b/(2*a))
    else:
        print('Phương trình có hai nghiệm phân biệt x1 =', (-b + sqrt(delta))/(2*a), ', x2 = ', (-b - sqrt(delta))/(2*a))