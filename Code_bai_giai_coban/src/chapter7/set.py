Danh_sach_Ten = {"Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"}
print(Danh_sach_Ten)
Danh_sach_Ten.add("Quang Mỹ")
Danh_sach_Ten.add("Ngọc Trí")
print(Danh_sach_Ten)

for Ten in Danh_sach_Ten:
    print(Ten)

Danh_sach_Ten.discard("Quang Mỹ")
Danh_sach_Ten.remove("Ngọc Trí")
Ten_xoa = Danh_sach_Ten.pop()
print("\n")
print("Tên xóa:",Ten_xoa)
for Ten in Danh_sach_Ten:
    print(Ten)
    
