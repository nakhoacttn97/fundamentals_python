import ast # Abstract Syntax Trees
# ghi
danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"]
tap_tin = open("danh_sach_Ten.txt", "w", encoding="UTF-8")
tap_tin.write(str(danh_sach_Ten))
tap_tin.close()
# đọc
tap_tin = open("danh_sach_Ten.txt", "r", encoding="UTF-8")
chuoi_doc = tap_tin.read()
tap_tin.close()
danh_sach_Ten = ast.literal_eval(chuoi_doc)
print(danh_sach_Ten)
