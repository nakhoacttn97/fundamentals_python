print("CT tính tiền mua hàng")
n = int(input("Bạn mua bao nhiêu mặt hàng ? "))
tong_thanh_tien = 0
for i in range(1, n+1):
    # Nhập
    ten_hang = input("Tên hàng thứ "+str(i)+": ")
    so_luong = int(input("Số lượng mua: "))
    don_gia = int(input("Đơn giá: "))
    # Tính toán
    thanh_tien = so_luong*don_gia
    tong_thanh_tien += thanh_tien
    # Xuất
    thong_bao = "Thành tiền: "+"{:,} vnđ".format(thanh_tien)
    print(thong_bao+"\n")
thong_bao = "Tiền phải trả là: "+"{:,} vnđ".format(tong_thanh_tien)
print(thong_bao)
