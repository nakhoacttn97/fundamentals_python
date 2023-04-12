from datetime import date

Tuoi = 23
Luong = 1200
Co_gia_dinh = True
Hop_le = Tuoi >= 20 and Luong >= 1000 and not Co_gia_dinh
print("Hợp lệ:", Hop_le)

Hop_le = (Tuoi >= 20 or Luong >= 1000) and Co_gia_dinh
print("Hợp lệ:", Hop_le)

Ngay_hien_tai = date.today()
print("Ngày hôm nay: ", Ngay_hien_tai)
Nam_hien_tai = Ngay_hien_tai.year
Nam_nhuan = (Nam_hien_tai % 4 == 0 and not Nam_hien_tai %
             100 != 0) or (Nam_hien_tai % 400 == 0)
print("Năm nay là nhuần:", Nam_nhuan)

Chuoi_Dung_sai = "true"
Dung_sai = bool(Chuoi_Dung_sai)
print(Dung_sai)

Dung_sai = False
Chuoi_Dung_sai = str(Dung_sai)
print(Chuoi_Dung_sai)
