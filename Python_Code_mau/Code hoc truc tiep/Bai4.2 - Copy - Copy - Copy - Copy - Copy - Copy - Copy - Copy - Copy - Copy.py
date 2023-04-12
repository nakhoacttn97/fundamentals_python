danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8]
gia_tri_tim = int(input("Gia tri can tim: "))
n = 0
while n<= len(danh_sach_so) - 1:
    if danh_sach_so[n] == gia_tri_tim:
        print(f'Tim thay gia tri {gia_tri_tim} tai vi tri index ={n}')
        break
    n += 1
else:
    print(f'Khong tim thay gia tri {gia_tri_tim} trong danh sach')

Cho nguoi dung nhap vao mot so nguyen, kiem tra no co phai la so nguyen to hay khong