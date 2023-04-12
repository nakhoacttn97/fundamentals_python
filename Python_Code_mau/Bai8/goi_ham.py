# Xây dựng hàm
def tinh_diem_trung_binh(hk1, hk2):
    dtb = (hk1 + hk2 * 2) / 3
    print('Điểm trung bình:', dtb)
# Gọi hàm
diem_hk1 = eval(input('Điểm HK1: '))
diem_hk2 = eval(input('Điểm HK2: '))
tinh_diem_trung_binh(diem_hk1, diem_hk2)

# Note_ Phần khai báo hàm phải nằm trước (bên trên) lời gpoij hàm trong chương trình