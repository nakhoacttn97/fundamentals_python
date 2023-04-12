# Bài tập 6.10 # Đã xong
# Xây dựng chương trình xử lý chuỗi
s = str(input('Nhập chuỗi s:\n'))
s_sub = str(input('Nhập chuỗi con s_sub:\n'))
s_find = str(input('Nhập chuỗi tìm s_find:\n'))
s_replace = str(input('Nhập chuỗi thay thế s_replace:\n'))
# Loại bỏ khaongr trắng và viết hoa
khoang_trang = s.strip()
viet_hoa = s.capitalize()
# Đếm số lần chuỗi con s_sub xuất hiện trong chuỗi s, sau đó thay thế
so_lan_xuat_hien = s.count(s_sub)
thay_the = s.replace(s_find, s_replace)
 #
print('Chuỗi s sau khi loại bỏ khoảng trắng đầu và cuối chuỗi:', khoang_trang)
print('Chuỗi viết hoa ký t đầu:', viet_hoa)
print('Số lần s_sub xuất hiện trong s:', so_lan_xuat_hien)
print('Chuỗi s sau khi tìm kiếm và thay thế:', thay_the)