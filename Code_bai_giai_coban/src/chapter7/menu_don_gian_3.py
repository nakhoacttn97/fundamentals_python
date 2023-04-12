cac_chuc_nang = ["Nhập hai số nguyên a và b.",
                 "Tính tổng a + b.", "Tính hiệu a - b.", "Thoát."]


def Xuat_thuc_don():
    print("Thực đơn".center(30, " "))
    print("* "*15)
    for i in range(len(cac_chuc_nang)):
        print(str(i+1)+". "+cac_chuc_nang[i])
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
