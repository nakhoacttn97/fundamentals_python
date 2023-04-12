'''
Created on Feb 13, 2017

@author: KTPHUONG
'''
import xu_ly_tap_tin
filename = input('Nhập tên tập tin:\n')
content = input('Nhập nội dung:\n')
xu_ly_tap_tin.write_file(filename, content)
print(xu_ly_tap_tin.read_file(filename))