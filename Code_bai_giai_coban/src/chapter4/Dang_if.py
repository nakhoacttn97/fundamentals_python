print("CT tính tiền mua hàng, nếu mua với số tiền >= 1,000,000 thì được giảm 5%")
# Nhập
ten_hang = input("Tên hàng: ")
so_luong = int(input("Số lượng mua: "))
don_gia = int(input("Đơn giá bán: "))
# Tính toán
thanh_tien = so_luong*don_gia
tien_giam = 0
if thanh_tien >= 1000000:
    tien_giam = thanh_tien*5/100
tien_phai_tra = thanh_tien-tien_giam
# Xuất
thong_bao = "Thành tiền: "+"{:,} vnđ".format(thanh_tien)
print(thong_bao)
if tien_giam > 0:
    thong_bao = "Tiền được giảm: "+"{:,} vnđ".format(tien_giam)
    print(thong_bao)
thong_bao = "Tiền phải trả là: "+"{:,} vnđ".format(tien_phai_tra)
print(thong_bao)
