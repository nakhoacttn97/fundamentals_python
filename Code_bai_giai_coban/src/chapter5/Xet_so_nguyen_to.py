print("CT xét số N có là số nguyên tố ? với N là số nguyên và N>=2") #13194761
chuoi_n = input("N = ")
if not chuoi_n.isdigit():
    print("Bạn phải nhập số")
    exit()
n=int(chuoi_n)
if n<2:
    print("N phải là số nguyên và N>=2")
    exit()
# Xét N có là số nguyên tố?    
i = 2
while i < n:
    if n % i == 0:
        break
    i += 1
if i < n:
    print(n, "không là số nguyên tố.")
else:
    print(n, "là số nguyên tố.")
