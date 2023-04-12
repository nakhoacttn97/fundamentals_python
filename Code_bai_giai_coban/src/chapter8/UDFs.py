import json


def In_Tong(a, b):
    # Hàm xử lý
    s = a+b
    print("Tổng:", s)


def Tinh_Tong(a, b):
    # Hàm xử lý và trả về kết quả
    s = a+b
    return s


In_Tong(2, 5)
s = Tinh_Tong(2, 5)
print("Tổng:", s)


def In_Danh_sach_Ten_HS(Danh_sach):
    for Ten in Danh_sach:
        print(Ten)


Danh_sach_Ten = ["Minh Quang", "Hoàng Vũ", "Kiều Hương",
                 "Ngọc Lan", "Mỹ Ngọc", "Ngọc Linh", "Toàn Trung", "Ngọc Phương", "Khoa Trường", "Đức Duy", "Đàm Phú"]
In_Danh_sach_Ten_HS(Danh_sach_Ten)


def In_Thong_tin_NV(Nhan_vien):
    print("Họ tên:", Nhan_vien["Ho_ten"])
    print("Giới tính:", Nhan_vien["Gioi_tinh"])
    print("Lương:", Nhan_vien["Luong"])
    print("Ngày sinh:", Nhan_vien["Ngay_sinh"])


def Chuoi_Thong_tin_NV(Nhan_vien):
    Chuoi = ""
    Chuoi += "\nHọ tên: "+Nhan_vien["Ho_ten"]
    Chuoi += "\nGiới tính: "+str(Nhan_vien["Gioi_tinh"])
    Chuoi += "\nLương: " + str(Nhan_vien["Luong"])
    Chuoi += "\nNgày sinh: " + Nhan_vien["Ngay_sinh"]
    return Chuoi


Chuoi_Nhan_vien = '{"Ho_ten":"Lâm Bảo Khanh", "Gioi_tinh":true, "Luong":1000, "Ngay_sinh":"2000-01-25"}'
Nhan_vien = json.loads(Chuoi_Nhan_vien)
print("\n")
In_Thong_tin_NV(Nhan_vien)
Chuoi = Chuoi_Thong_tin_NV(Nhan_vien)
print(Chuoi)
