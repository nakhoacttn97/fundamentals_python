# Xây dựng chương trình giải phương trình bậc 2: ax^2 + bx + c = 0

import math
# Nhập
a = eval(input('Nhập a:\n'))
b = eval(input('Nhập b:\n'))
c = eval(input('Nhập c:\n'))

# Xây dựng bài toán
if a == 0:
    # b * x + c = 0
    if b == 0 and c != 0:
        print('Phương trình vô nghiệm')
    elif b == 0 and c == 0:
        print('Phương trình vô số nghiệm')
    else:
        print('Phương trình có nghiệm = ', -c/d)

if a != 0:
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('Phương trình vô nghiệm')
    if delta == 0:
        print('Phương trình có nghiệm kép:', -b/2*a)
    if delta > 0:
        x_1 = (-b + math.sqrt(delta))/2*a
        x_2 = (-b - math.sqrt(delta))/2*a
        print('Phương trình có 2 nghiệm phân biệt x1 =', x_1, ', x2 =', x_2)