Tu_dien_Thu_cung = {1: 'Chim Họa mi', 2: 'Cá ba đuôi',
                    3: 'Rắn', 4: 'Trăn', 5: 'Kỳ nhông', 6: 'Cá Ông tiên'}

print(Tu_dien_Thu_cung)
print(Tu_dien_Thu_cung[4])
Tu_dien_Thu_cung[6] = Tu_dien_Thu_cung[6].upper()
print(Tu_dien_Thu_cung[6])

So_phan_tu = len(Tu_dien_Thu_cung)
print("Số thú cưng:", So_phan_tu)

for i in Tu_dien_Thu_cung:
    print(i, ':', Tu_dien_Thu_cung[i])

Tu_dien_Thu_cung.items
Tu_dien_Thu_cung.keys
Tu_dien_Thu_cung.values

Tu_dien_Thu_cung[7] = "Chim Vành khuyên"
Tu_dien_Thu_cung[8] = "Mèo Ấn"
Tu_dien_Thu_cung[9] = "Chó Nhật"
print(Tu_dien_Thu_cung)

Ban_sao = Tu_dien_Thu_cung.copy()
print("\nBản sao:")
for i in Ban_sao:
    Ban_sao[i] = Ban_sao[i].upper()
    print(i, ':', Ban_sao[i])

print("\nBản gốc:")
for i in Tu_dien_Thu_cung:
    print(i, ':', Tu_dien_Thu_cung[i])

Tu_dien_Thu_cung = {1: 'Chim Họa mi', 2: 'Cá ba đuôi',
                    3: 'Rắn', 4: 'Trăn', 5: 'Kỳ nhông', 6: 'Cá Ông tiên'}
Ban_tham_chieu = Tu_dien_Thu_cung
print("\nBản tham chiếu:")
for i in Ban_tham_chieu:
    Ban_tham_chieu[i] = Ban_tham_chieu[i].upper()
    print(i, ':', Ban_tham_chieu[i])

print("\nBản gốc:")
for i in Tu_dien_Thu_cung:
    print(i, ':', Tu_dien_Thu_cung[i])

Danh_ba_Dien_thoai = {"A01": "0168456789", "A02": "0987456789",
                      "A03": "01782267890", "A04": "0973455666", "A05": "0100234567"}
print("\n")
print(Danh_ba_Dien_thoai)
print("A03 -", Danh_ba_Dien_thoai["A03"])
print("A03 -", Danh_ba_Dien_thoai.get("A03"))
print("\n")
for i in Danh_ba_Dien_thoai:
    print(i, ':', Danh_ba_Dien_thoai[i])

Danh_sach_Cong_ty = {"A01": ["Công ty TNHH Việt Nhật", "345 Lý Chính Thắng", "0988123456"],
                     "A02": ["Công ty May Bình Minh", "123 An Dương Vương", "0983222555"],
                     "A03": ["Công ty Rạng Đông", "135 Tân Hóa", "0168777999"]}
print("\n")
print("Danh sách Công ty:", Danh_sach_Cong_ty)
Cong_ty = Danh_sach_Cong_ty.get("A01")
print("Công ty A01:", Cong_ty)

print("\nDanh sách Công ty")
Tieu_de_Cong_ty = ["Tên", "Địa chỉ", "Điện thoại"]
for Ma_so in Danh_sach_Cong_ty:
    print("Mã số:", Ma_so)
    Cong_ty = Danh_sach_Cong_ty.get(Ma_so)
    for i in range(len(Cong_ty)):
        print("\t", Tieu_de_Cong_ty[i]+":", Cong_ty[i])

print("\nDanh sách Công ty")
Tieu_de_Cong_ty = ["Mã số", "Tên", "Địa chỉ", "Điện thoại"]
Kich_thuoc = [10, 30, 40, 15]
Chuoi_Tieu_de = ""
for i in range(len(Tieu_de_Cong_ty)):
    Chuoi_Tieu_de += Tieu_de_Cong_ty[i].ljust(Kich_thuoc[i], " ")
print(Chuoi_Tieu_de)
for Ma_so in Danh_sach_Cong_ty:
    Cong_ty = Danh_sach_Cong_ty.get(Ma_so)
    Chuoi_Cong_ty = Ma_so.ljust(Kich_thuoc[0], " ")
    for i in range(len(Cong_ty)):
        Chuoi_Cong_ty += Cong_ty[i].ljust(Kich_thuoc[i+1], " ")
    print(Chuoi_Cong_ty)

# Xóa
del Danh_sach_Cong_ty["A01"]
print("\n",Danh_sach_Cong_ty)

Danh_sach_Cong_ty.clear()
print("\n",Danh_sach_Cong_ty)

del Danh_sach_Cong_ty

