'''
Created on Feb 13, 2017

@author: KTPHUONG
'''
import xu_ly_tap_tin_csv
filename = input('Nhập tên tập tin:\n')
print('Nội dung tập tin:')
print(xu_ly_tap_tin_csv.read_csv_file(filename))
'''
filename = input('Nhập tên tập tin:\n')
print('Nội dung tập tin:')
print(xu_ly_tap_tin_csv.read_csv_file_to_list(filename))

filename = input('Nhập tên tập tin:\n')
print('Nội dung tập tin:')
xu_ly_tap_tin_csv.read_csv_file_column(filename)
'''