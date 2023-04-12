danh_sach_phim = []
danh_sach_phim.append("Titanic;1997;Tình cảm, lãng mạn")
danh_sach_phim.append("Star Wars;1977;Chiến tranh")
danh_sach_phim.append("The Good, the Bad and the Ugly;1966;Cao bồi")
danh_sach_phim.append("Apollo 13;1995;Hành động")
danh_sach_phim.append("The Proposal;2009;Tình cảm, hài")


def In_phim(phim):
    thong_tin_phim = phim.split(";")
    ten_phim = thong_tin_phim[0]
    nam_sx = thong_tin_phim[1]
    the_loai = thong_tin_phim[2]
    print("* "*15)
    print("Tên phim:", ten_phim)
    print("Năm sản xuất:", nam_sx)
    print("Thể loại:", the_loai)
    print("* "*15+"\n")


def In_Danh_sach_Phim():
    for phim in danh_sach_phim:
        In_phim(phim)


def Them_phim_moi():
    ten_phim = input("Tên phim: ")
    nam_sx = input("Năm sản xuất: ")
    the_loai = input("Thể loại: ")
    danh_sach_phim.append(ten_phim+";"+nam_sx+";"+the_loai)
    In_Danh_sach_Phim()


def Sap_tang_ten_phim():
    danh_sach_phim.sort()
    In_Danh_sach_Phim()


def Sap_giam_ten_phim():
    danh_sach_phim.sort()
    danh_sach_phim.reverse()
    In_Danh_sach_Phim()


def Xoa_phim():
    print("Số phim hiện có:", len(danh_sach_phim))
    i = int(input("Thứ tự phim muốn xóa: "))
    if i >= 1 and i <= len(danh_sach_phim):
        del(danh_sach_phim[i-1])
        In_Danh_sach_Phim()
    else:
        print("Thứ tự xóa", i, "Không hợp lệ.")


def Sua_phim():
    print("Số phim hiện có:", len(danh_sach_phim))
    i = int(input("Thứ tự phim muốn cập nhật: "))
    if i >= 1 and i <= len(danh_sach_phim):
        phim = danh_sach_phim[i-1]
        print("Trước khi cập nhật:")
        In_phim(phim)
        print("Cập nhật phim:")
        ten_phim = input("Tên phim: ")
        nam_sx = input("Năm sản xuất: ")
        the_loai = input("Thể loại: ")
        danh_sach_phim[i-1] = ten_phim+";"+nam_sx+";"+the_loai
        In_Danh_sach_Phim()
    else:
        print("Thứ tự cập nhật", i, "Không hợp lệ.")

def Tim_phim_theo_ten():
    ten_phim_muon_tim = input("Tên phim muốn tìm: ").strip()
    ket_qua = []
    for phim in danh_sach_phim:
        thong_tin_phim = phim.split(";")
        ten_phim = thong_tin_phim[0]
        if ten_phim.upper().find(ten_phim_muon_tim.upper()) >= 0:
            ket_qua.append(ten_phim)
    if len(ket_qua) > 0:
        print("Phim tìm thấy:", ket_qua)
    else:
        print("Không tìm thấy phim.")

def Tim_phim_theo_nam_sx():
    nam_sx_muon_tim = input("Năm sản xuất muốn tìm: ").strip()
    ket_qua = []
    for phim in danh_sach_phim:
        thong_tin_phim = phim.split(";")
        nam_sx = thong_tin_phim[1]
        if nam_sx==nam_sx_muon_tim:
            ten_phim = thong_tin_phim[0]
            ket_qua.append(ten_phim)
    if len(ket_qua) > 0:
        print("Phim tìm thấy:", ket_qua)
    else:
        print("Không tìm thấy phim.")

def Tra_cuu_phim_theo_nam_sx(tu_nam,den_nam):
    ket_qua = []
    for phim in danh_sach_phim:
        thong_tin_phim = phim.split(";")
        nam_sx = int(thong_tin_phim[1])
        if nam_sx>=tu_nam and nam_sx<=den_nam:
            ten_phim = thong_tin_phim[0]
            ket_qua.append(ten_phim)
    if len(ket_qua) > 0:
        print("Phim tìm thấy:", ket_qua)
    else:
        print("Không tìm thấy phim.")

Tra_cuu_phim_theo_nam_sx(1990,2000)