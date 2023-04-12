'''
Created on Feb 13, 2017

@author: KTPHUONG
'''
import xu_ly_tap_tin
filename = input('Nhập tên tập tin:\n')
print('Nội dung tập tin:')
print(xu_ly_tap_tin.read_file(filename))