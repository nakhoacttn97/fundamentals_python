# Viết CT tính tiền thuê phòng của resort

loai_1 = 1260000
loai_2 = 1550000
loai_3 = 1830000
loai_4 = 1830000
loai_5 = 2120000
loai_6 = 2120000
loai_7 = 2540000
loai_8 = 4800000

loai_phong = int(input('Nhập loại phòng (từ 1 đến 8):\n'))
so_dem = int(input('Nhập số đêm:\n'))

don_gia_phong = 0
thanh_tien = 0

if loai_phong == 1:
    don_gia_phong = loai_1
elif loai_phong == 2:
    don_gia_phong = loai_2
elif loai_phong == 3:
    don_gia_phong = loai_3
elif loai_phong == 4:
    don_gia_phong = loai_4
elif loai_phong == 5:
    don_gia_phong = loai_5
elif loai_phong == 6:
    don_gia_phong = loai_6
elif loai_phong == 7:
    don_gia_phong = loai_7
else:
    don_gia_phong = loai_8

if so_dem == 1:
    thanh_tien = don_gia_phong * so_dem
elif 2 <= so_dem <= 3:
    thanh_tien = (don_gia_phong * 25//100) * so_dem
else:
    thanh_tien = (don_gia_phong * 30//100) * so_dem
print('Thành tiền =', thanh_tien)