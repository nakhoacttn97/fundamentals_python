'''
Created on Feb 14, 2017

@author: KTPHUONG
'''
# don gia loai phong
loai1 = 1260000
loai2 = 1550000
loai3 = 1830000
loai4 = 1830000
loai5 = 2120000
loai6 = 2120000
loai7 = 2540000
loai8 = 4800000

loai_phong = int(input('Nhập loại phòng (từ 1 đến 8):\n'))
so_dem = int(input('Nhập số đêm:\n'))
don_gia_phong = 0
thanh_tien_resort = 0
if loai_phong == 1:
    don_gia_phong = loai1
elif loai_phong == 2:
    don_gia_phong = loai2
elif loai_phong == 3:
    don_gia_phong = loai3
elif loai_phong == 4:
    don_gia_phong = loai4
elif loai_phong == 5:
    don_gia_phong = loai5
elif loai_phong == 6:
    don_gia_phong = loai6
elif loai_phong == 7:
    don_gia_phong = loai7
elif loai_phong == 8:
    don_gia_phong = loai8

if so_dem == 1:
    thanh_tien_resort = so_dem * don_gia_phong
elif so_dem >=2 and so_dem <=3:
    thanh_tien_resort = so_dem * don_gia_phong * 0.75
else:
    thanh_tien_resort = so_dem * don_gia_phong * 0.7

print('Thành tiền =', thanh_tien_resort, 'vnđ')