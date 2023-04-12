import math

print("CT xét số N có là số nguyên tố ? với N là số nguyên và N>=2") #13194761
n = int(input("N = "))
i = 2
while i <= math.sqrt(n):
    if n % i == 0:
        break
    i += 1
if i > math.sqrt(n):
    print(n, "là số nguyên tố.")
else:
    print(n, "không là số nguyên tố.")
