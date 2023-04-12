# Viết chương trình để giải PT bậc nhất ax + b = 0

a = float(input('Nhập a:\n'))
b = float(input('Nhập b:\n'))
#pt_bac_nhat = -ax + b = 0

if b == 0:
    if a == 0:
        print('PT có vô số nghiệm')
    else a != 0:
        print('PT vô nghiệm')
else b != 0:
    print('Nghiệm x =', -a/b)
