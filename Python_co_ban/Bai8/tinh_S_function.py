# Tính giá trị biểu thức S = (x^2 + 1) ^ n
# Xây dựng hàm
def tinh_s(n, x):
    if n == 0:
        S = 1
    else:
        S = 1
        for i in range(0, n):
            S = S * (x * x + 1)
    print('S = (x*x + 1)^n=', S)
# Gọi hàm
nhap_n = int(input('Nhập n:\n'))
nhap_x = eval(input('Nhập x:\n'))

tinh_s(nhap_n, nhap_x)