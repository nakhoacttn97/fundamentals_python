Danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"]

print(Danh_sach_Ten)
So_phan_tu = len(Danh_sach_Ten)
print("Số học sinh:", So_phan_tu)

for Ten in Danh_sach_Ten:
    print(Ten)

for i in range(So_phan_tu):
    Ten = Danh_sach_Ten[i]
    print(Ten)

i = 0
while i < So_phan_tu:
    Ten = Danh_sach_Ten[i]
    print(Ten)
    i += 1

Danh_sach_Ten.append("Bạch Lan")
Danh_sach_Ten.append("Diễm Trang")
print(Danh_sach_Ten)
So_phan_tu = len(Danh_sach_Ten)
print("Số học sinh:", So_phan_tu)
for Ten in Danh_sach_Ten:
    print(Ten)

Danh_sach_Ten[10-1] = Danh_sach_Ten[10-1].upper()
for Ten in Danh_sach_Ten:
    print(Ten)

Danh_sach_Ten.insert(0, "Thanh Thảo")
for Ten in Danh_sach_Ten:
    print(Ten)

Danh_sach_Ten.extend(["Ngọc Nga", "Minh Trang", "Minh Toàn"])
for Ten in Danh_sach_Ten:
    print(Ten)

i = Danh_sach_Ten.index("Đàm Phú")
print("Vị trí tìm thấy:", i+1)

Danh_sach_Ten.remove("Mỹ Ngọc")
Danh_sach_Ten.pop()
Danh_sach_Ten.pop(0)
for Ten in Danh_sach_Ten:
    print(Ten)

print("\n")
del Danh_sach_Ten[0]
for Ten in Danh_sach_Ten:
    print(Ten)

print("\n")
Danh_sach_Ten.sort()
for Ten in Danh_sach_Ten:
    print(Ten)

print("\n")
Danh_sach_Ten.reverse()
for Ten in Danh_sach_Ten:
    print(Ten)


def Lay_Ten(Chuoi_con):
    return Chuoi_con[Chuoi_con.rindex(" "):]


print("\n")
Danh_sach_Ten.sort(key=Lay_Ten)
for Ten in Danh_sach_Ten:
    print(Ten)

print("\n")
Danh_sach_Ten.sort(key=Lay_Ten, reverse=True)
for Ten in Danh_sach_Ten:
    print(Ten)

print(Danh_sach_Ten)
print("\n")
Mang_Danh_sach_Ten = tuple(Danh_sach_Ten)
print(Mang_Danh_sach_Ten)
