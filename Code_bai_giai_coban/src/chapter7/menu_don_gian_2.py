def Xuat_thuc_don():
    print("Thực đơn".center(30, " "))
    print("* "*15)
    print("1. Nhập hai số nguyên a và b.")
    print("2. Tính tổng a + b.")
    print("3. Tính hiệu a - b.")
    print("4. Thoát.")
    print("* "*15)
    chon = int(input("Mời bạn chọn: "))
    return chon


def Xu_ly_thuc_don(chon):
    tiep_tuc = True
    if chon == 1:
        print("Nhập hai số nguyên a và b.")
    elif chon == 2:
        print("Tính tổng a + b.")
    elif chon == 3:
        print("Tính hiệu a - b.")
    elif chon == 4:
        tiep_tuc = False
    else:
        pass
    return tiep_tuc


tiep_tuc = True
while tiep_tuc:
    chon = Xuat_thuc_don()
    tiep_tuc = Xu_ly_thuc_don(chon)
