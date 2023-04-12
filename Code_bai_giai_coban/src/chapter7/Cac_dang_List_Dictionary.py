danh_sach_ten = ["Thanh Hoa", "Bảo An", "Tuấn Hùng", "Thành Nghĩa",
                 "Minh Toàn", "Kim Bảo"]
print("Danh sách tên:", danh_sach_ten)

nhan_vien = ["A01", "Lê Thanh", "Nghĩa", "1989-10-24", True, 1000]
print("\nNhân viên:", nhan_vien)

danh_sach_nhan_vien = {
    "A01": ["Lê Thanh", "Nghĩa", "1989-10-24", True, 1000],
    "A02": ["Bùi Ngọc Mạnh", "Phái", "1999-12-12", True, 2000],
    "A03": ["Trần Thị Ngọc", "Bảo", "1979-01-25", False, 1000]
}
print("\nDanh sách Nhân viên:", danh_sach_nhan_vien)

nhan_vien = {"Ma_so": "A01", "Ho": "Lê Thanh", "Ten": "Nghĩa",
             "Ngay_sinh": "1989-10-24", "Gioi_tinh": True, "Luong": 1000}
print("\nNhân viên:", nhan_vien)

danh_sach_nhan_vien = {
    "A01": {"Ho": "Lê Thanh", "Ten": "Nghĩa", "Ngay_sinh": "1989-10-24",
            "Gioi_tinh": True, "Luong": 1000},
    "A02": {"Ho": "Bùi Ngọc Mạnh", "Ten": "Phái", "Ngay_sinh": "1999-12-12",
            "Gioi_tinh": True, "Luong": 2000},
    "A03": {"Ho": "Trần Thị Ngọc", "Ten": "Bảo", "Ngay_sinh": "1979-01-25",
            "Gioi_tinh": False, "Luong": 1000}
}
print("\nDanh sách Nhân viên:", danh_sach_nhan_vien)
