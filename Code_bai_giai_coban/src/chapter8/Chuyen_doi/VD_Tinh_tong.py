print("CT in tổng các số nguyên từ 1 đến N: S = 1+2+3+...+N")
n = int(input("N = "))
i = 1
s = 0
while i <= n:
    s += i
    i += 1
print("S = ", "{:,}".format(s))

s = 0
for i in range(1, n+1):
    s += i
print("S = ", "{:,}".format(s))
