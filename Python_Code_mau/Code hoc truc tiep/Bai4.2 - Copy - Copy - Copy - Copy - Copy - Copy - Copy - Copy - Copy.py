n = int(input('Ban muon nhap bao nhieu gia tri?\t'))
tong = 0
for i in range(1, n+1):
    gia_tri = int(input(f'Nhap so thu {i}: '))
    tong += gia_tri
else:
    print(f'Gia tri trung binh: {tong/n}')
