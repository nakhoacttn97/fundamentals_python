# Tính giá trị biểu thức A = (x^2 + x + 1) ^ n + (x^2 - x - 1) ^ n
# Bước 1: Xây dựng hàm
def tinh_a(n, x):
    if n == 0:
        A = 2
    else:
        A1 = 1
        A2 = 2
        for i in range(0, n):
            A1 = A1 * (x * x + 1)
            A2 = A2 * (x * x + 1)
        A = A1 + A2
    print('A = (x^2 + x + 1^n + (x^2 - x + 1)^n =', A)
# Bước 2: Gọi hàm
nhap_n = int(input('Nhập n:\n'))
nhap_x = eval(input('Nhập x:\n'))
tinh_a(nhap_n, nhap_x)