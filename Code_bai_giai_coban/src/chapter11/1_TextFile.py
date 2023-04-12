Duong_dan_Thu_muc = "TXT\\"
Ten_Tap_tin = "tho.txt"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
# Ghi
Tap_tin = open(Duong_dan, "w", encoding="UTF-8")
Tap_tin.write("Ao thu lạnh lẽo nước trong veo")
Tap_tin.write("\nMột chiếc thuyền câu bé tẻo teo")
Tap_tin.close()
# Đọc nội dung
Tap_tin = open(Duong_dan, "r", encoding="UTF-8")
Chuoi = Tap_tin.read()
print(Chuoi)
# Đọc theo dòng
Tap_tin = open(Duong_dan, "r", encoding="UTF-8")
Cac_dong = Tap_tin.readlines()
print("\n")
for Dong in Cac_dong:
    print(Dong.replace("\n", ""))

# Ghi tiếp
Tap_tin = open(Duong_dan, "a", encoding="UTF-8")
Tap_tin.write("\nSóng biếc theo làn hơi gợn tí")
Tap_tin.write("\nLá vàng trước gió sẽ đưa vèo")
Tap_tin.close()
Tap_tin = open(Duong_dan, "r", encoding="UTF-8")
Chuoi = Tap_tin.read()
print("\n")
print(Chuoi)

Danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"]
Ten_Tap_tin = "ban.txt"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
Tap_tin = open(Duong_dan, "w", encoding="UTF-8")
for Ten in Danh_sach_Ten:
    Tap_tin.write(Ten+"\n")
Tap_tin.close()

Tap_tin = open(Duong_dan, "r", encoding="UTF-8")
Chuoi = Tap_tin.read()
print("\n")
print(Chuoi)