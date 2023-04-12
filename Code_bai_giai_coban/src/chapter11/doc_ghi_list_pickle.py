import pickle
# ghi
danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"]
tap_tin = open("danh_sach_Ten.dat", "wb")
pickle.dump(danh_sach_Ten, tap_tin)
tap_tin.close()
# đọc
tap_tin = open("danh_sach_Ten.dat", "rb")
danh_sach_Ten = pickle.load(tap_tin)
tap_tin.close()
print(danh_sach_Ten)
