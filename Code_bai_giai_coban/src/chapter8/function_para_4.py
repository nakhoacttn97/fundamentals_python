# Khai báo hàm
def Tinh_Tong(*day_so):
    tong = 0
    for so in day_so:
        tong += so
    return tong


def Tim_so_min(*day_so):
    so_min=None
    if len(day_so)>0:
        so_min = day_so[0]
        for so in day_so:
            if so_min > so:
                so_min = so
    return so_min


# CT chính
tong = Tinh_Tong(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tổng =", tong)
print("\n")
so_min = Tim_so_min(100, 25, 3, 41, 51, 60, 75, 8, 9, 60)
print("Số nhỏ nhất =", so_min)
print("\n")
so_min = Tim_so_min()
if so_min!=None:
    print("Số nhỏ nhất =", so_min)
else:
    print("Chuỗi số rỗng.")    
