import csv

Danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"]
# Ghi
Duong_dan_Thu_muc = "TXT\\"
Ten_Tap_tin = "hoc_sinh.txt"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
Tap_tin = open(Duong_dan, "w", encoding="UTF-8")
Chuoi = ""
for Ten in Danh_sach_Ten:
    if Chuoi == "":
        Chuoi = Ten
    else:
        Chuoi += ","+Ten
Tap_tin.write(Chuoi)
Tap_tin.close()
# Đọc
Tap_tin = open(Duong_dan, "r", encoding="UTF-8")
Chuoi = Tap_tin.read()
Danh_sach_Ten = Chuoi.split(",")
for Ten in Danh_sach_Ten:
    print(Ten)

# Ghi bằng thư viện csv
Danh_sach_Sinh_vien = [["Họ tên", "Tuổi"], ["Minh Quang", 20], ["Hoàng Vũ", 23], ["Kiều Hương", 30],
                       ["Ngọc Lan", 25], ["Mỹ Ngọc", 21], ["Ngọc Linh", 40]]
Ten_Tap_tin = "sinh_vien.csv"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
Tap_tin = open(Duong_dan, "w", encoding="UTF-8", newline='')
for Sinh_vien in Danh_sach_Sinh_vien:
    csv.writer(Tap_tin).writerow(Sinh_vien)
Tap_tin.close()


# Đọc bằng thư viện csv
Tap_tin = open(Duong_dan, "r", encoding="UTF-8")
Danh_sach = csv.reader(Tap_tin)
print("\n")
for Sinh_vien in Danh_sach:
    print(Sinh_vien[0].ljust(30,' ')+"\t"+Sinh_vien[1].rjust(10,' '))
Tap_tin.close()
