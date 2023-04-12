# ghi
danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương",
                 "Khoa Trường", "Đức Duy", "Đàm Phú"]
tap_tin = open("danh_sach_Ten.txt", "w", encoding="UTF-8")
for ten in danh_sach_Ten:
    tap_tin.write(ten+"\n")
tap_tin.close()
# đọc
danh_sach_Ten = []
tap_tin = open("danh_sach_Ten.txt", "r", encoding="UTF-8")
for dong in tap_tin:
    danh_sach_Ten.append(dong.replace("\n", ""))
tap_tin.close()
print(danh_sach_Ten)
