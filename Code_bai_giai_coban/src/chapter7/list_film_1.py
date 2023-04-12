danh_sach_phim = []
danh_sach_phim.append("Titanic")
danh_sach_phim.append("Star Wars")
danh_sach_phim.append("The Good, the Bad and the Ugly")
danh_sach_phim.append("Apollo 13")
danh_sach_phim.append("The Proposal")


def In_phim(phim):
    print("* "*15)
    print("Phim:", phim)
    print("* "*15+"\n")


def In_Danh_sach_Phim():
    for phim in danh_sach_phim:
        In_phim(phim)


def Them_phim_moi():
    ten_phim = input("Tên phim: ")
    danh_sach_phim.append(ten_phim)
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
        danh_sach_phim[i-1] = ten_phim
        In_Danh_sach_Phim()
    else:
        print("Thứ tự cập nhật", i, "Không hợp lệ.")


def Tim_phim_theo_ten():
    ten_phim_muon_tim = input("Tên phim muốn tìm: ").strip()
    ket_qua = []
    for phim in danh_sach_phim:
        if phim.upper().find(ten_phim_muon_tim.upper()) >= 0:
            ket_qua.append(phim)
    if len(ket_qua) > 0:
        print("Phim tìm thấy:", ket_qua)
    else:
        print("Không tìm thấy phim.")

