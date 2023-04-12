# Bài tập 5:
#Nhập vào một số nguyên n và một số thực x, tính các biểu thức sau đây:

n = int(input('Nhập n:\n'))
x = eval(input('Nhập x:\n'))
# A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
# A = A1 + A2

if n == 0:
     A = 2
else:
    A1 = 1
    A2 = 1
    for i in (0, n):
        A1 = (x**2 + x + 1)**n
        A2 = (x**2 - x + 1)**n
    A = A1 + A2
print('A = (x2 + x + 1)^n + (x2 - x + 1)^n =', A)