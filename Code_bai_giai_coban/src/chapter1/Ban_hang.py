# Nhập
ten_hang = input("Tên hàng: ")
so_luong = int(input("Số lượng mua: "))
don_gia = int(input("Đơn giá bán: "))
# Tính toán
thanh_tien = so_luong*don_gia
# Xuất
thong_bao = "Tiền phải trả là: "+"{:,} vnđ".format(thanh_tien)
thong_bao += "\n"+"Để mua %s"%(ten_hang)
print(thong_bao)
