# Xây dựng chương trình tính và in ra kết quả của các biểu thức

n = eval(input('Nhập n:\n'))

# Thuật toán, xây dựng chương trình tính tổng các số lẻ nhỏ hơn hoặc bằng n (Sửu dụng vòng lặp)
A = 0
chuoi_A = ''

B = 0
chuoi_B = ''

C = 0
chuoi_C = ''

D = 0
chuoi_D = ''

E = 0
chuoi_E = ''

i = 1

# Sử dụng vòng lặp while để duyệt qua các con số chạy từ 1 đến n
while i <= n:
    if i % 2 != 0:
        A = A + i
        chuoi_A = chuoi_A + str(i) + ' + '
    if i % 2 == 0:
        B = B + i
        chuoi_B = chuoi_B + str(i) + ' + '
    C = C * i
    chuoi_C = chuoi_C + str(i) + ' * '
    if i % 3 == 0:
        D = D * i
        chuoi_D = chuoi_D + str(i) + ' * '
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        E = E + i
        chuoi_E = chuoi_E + str(i) + ' + '
    i = i + 1
# Xuất hàm
print('A =', chuoi_A, '=', A)
print('B =', chuoi_B, '=', B)
print('C =', chuoi_C, '=', C)
print('D =', chuoi_D, '=', D)
print('E =', chuoi_E, '=', E)