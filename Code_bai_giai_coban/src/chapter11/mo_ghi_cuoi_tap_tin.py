'''
Created on Feb 13, 2017

@author: KTPHUONG
'''
import xu_ly_tap_tin
filename = input('Nhập tên tập tin:\n')
xu_ly_tap_tin.write_to_end_of_file(filename)
print(xu_ly_tap_tin.read_file(filename))