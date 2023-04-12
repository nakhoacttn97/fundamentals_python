# tính dãy số Fibonacci
# F0 = 0 và F1 = 1
# Fn = Fn-1 + Fn-2
print('CT in ra n số đầu tiên trong dãy Fibonacci, với n được nhập từ bàn phím')
n = int(input('Nhập n: '))
a = 0
b = 1
if n <= 0:
    print("n phải là số nguyên dương")
elif n == 1:
    chuoi_in = '0, 1'
    print(chuoi_in)
else:
    chuoi_in = '0, '
    for i in range(n):
        chuoi_in += str(b)+', '
        c = a + b
        a = b
        b = c
    print(chuoi_in+'...')