
chuoi = input('Nhap chuoi: ')
i = 0
dem = 0
while i<= len(chuoi)-1:
    if chuoi[i] == ' ':
        dem += 1
    i += 1
else:
    print(f'Chuoi "{chuoi}" co chua {dem} ky tu trang')