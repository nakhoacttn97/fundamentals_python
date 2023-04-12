# Khai báo hàm
def Chuc_mung_sinh_nhat(ten, tuoi):
    loi_chuc = "Mừng sinh nhật lần thứ %i của bạn %s." % (tuoi, ten)
    return loi_chuc


# CT chính
ten_ban = input("Bạn vui lòng cho biết tên: ")
tuoi_ban = int(input("và cả tuổi: "))
chuoi = Chuc_mung_sinh_nhat(tuoi=tuoi_ban, ten=ten_ban)
print(chuoi)
