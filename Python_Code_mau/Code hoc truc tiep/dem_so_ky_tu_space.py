chuoi = input('Nhập chuỗi: ')
i = 0
dem = 0
while i <= len(chuoi)-1:
    if chuoi[i] == " ":
        dem += 1
    i += 1
else:
    print(f'Chuỗi "{chuoi}" có chứa {dem} ký tự trắng')