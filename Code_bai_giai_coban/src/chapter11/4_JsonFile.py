import json
# chuyển chuỗi json sang đối tượng json
Chuoi_Nhan_vien = '{"Ho_ten":"Lâm Bảo Khanh", "Gioi_tinh":true, "Luong":1000, "Ngay_sinh":"2000-01-25"}'
Nhan_vien = json.loads(Chuoi_Nhan_vien)
print("Họ tên:", Nhan_vien["Ho_ten"])
print("Giới tính:", Nhan_vien["Gioi_tinh"])
print("Lương:", Nhan_vien["Luong"])
print("Ngày sinh: ", Nhan_vien["Ngay_sinh"])
# chuyển đối tượng json sang chuỗi json
Nhan_vien = {"Ho_ten": "Lâm Bảo Khanh",
                       "Gioi_tinh": True, "Luong": 1000, "Ngay_sinh": "2000-01-25"}
Chuoi_Nhan_vien = json.dumps(Nhan_vien)
print(Chuoi_Nhan_vien)
Nhan_vien = json.loads(Chuoi_Nhan_vien)
print("Họ tên:", Nhan_vien["Ho_ten"])
print("Giới tính:", Nhan_vien["Gioi_tinh"])
print("Lương:", Nhan_vien["Luong"])
print("Ngày sinh: ", Nhan_vien["Ngay_sinh"])

# Ghi ra tập tin
Nhan_vien = {"Ho_ten": "Lâm Bảo Khanh",
                       "Gioi_tinh": True, "Luong": 1000, "Ngay_sinh": "2000-01-25"}
Duong_dan_Thu_muc = "JSON\\"
Ten_Tap_tin = "nhan_vien.json"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
with open(Duong_dan, 'w') as f:
    json.dump(Nhan_vien, f)                       
# Đọc từ tập tin
with open(Duong_dan, 'r') as f:
    Nhan_vien = json.load(f)                       
print("\n")    
print("Họ tên:", Nhan_vien["Ho_ten"])
print("Giới tính:", Nhan_vien["Gioi_tinh"])
print("Lương:", Nhan_vien["Luong"])
print("Ngày sinh: ", Nhan_vien["Ngay_sinh"])
    
