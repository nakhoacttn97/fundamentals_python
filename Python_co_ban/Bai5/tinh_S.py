# Nhập vào một số nguyên n và một số thực x. Tính và in ra kết quả sau:
# S = (x^2 +1)^n

n = int(input('Nhập n:\n'))
x = int(input('Nhập x:\n'))
S = (x*x + 1)**n
if n == 0:
    S = 1
else:
    S = 1
    for i in range(0, n):
        S = S * (x * x + 1)
print('S = (x*x + 1)^n =', S)