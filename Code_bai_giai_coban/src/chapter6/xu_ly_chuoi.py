'''
Created on Feb 14, 2017

@author: KTPHUONG
'''
# xu ly chuoi
s = input('Nhập chuỗi s:\n')
s_sub = input('Nhập chuỗi con s_sub:\n')
s_find = input('Nhâp chuỗi tìm s_find:\n')
s_replace = input('Nhập chuỗi thay thế s_replace:\n')
s = s.strip()
print('Chuỗi s sau khi loại bỏ khoảng trắng đầu và cuối chuỗi:', s)
s = s.capitalize()
print('Chuỗi viết hoa ký tự đầu:', s)
print('Số lần s_sub xuất hiện trong s:', s.count(s_sub))
s = s.replace(s_find, s_replace)
print('Chuỗi s sau khi tìm kiếm và thay thế:', s)

