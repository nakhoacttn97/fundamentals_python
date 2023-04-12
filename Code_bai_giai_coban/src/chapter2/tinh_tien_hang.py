'''
Created on Feb 2, 2017

@author: KTPHUONG
'''
so_luong = eval(input('Nhập số lượng:\n'))
don_gia = eval(input('Nhập đơn giá:\n'))
thanh_tien = so_luong * don_gia
print("Thành tiền = %d * %.0f = %.0f"%(so_luong, don_gia, thanh_tien))
