# Hàm return nhiều giá trị
def tinh_diem_trung_binh(hk1, hk2):
    dtb = (hk1 + hk2 * 2) / 3
    if dtb >= 5:
        kq = 'Đậu'
    else:
        kq = 'Rớt'
    return dtb, kq