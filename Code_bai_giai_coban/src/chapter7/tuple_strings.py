'''
Created on Feb 15, 2017

@author: KTPHUONG
'''
tuple_strings = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange','red', 'blue')
print('Tuple:', tuple_strings)
chuoi_1 = 'Nhập số từ 0 đến ' + str(len(tuple_strings) -1) + ': \t'
chuoi_2 = 'Nhập số từ -1 đến ' + str(-(len(tuple_strings) -1)) + ':\t'
index_duong = int(input(chuoi_1))
index_am = int(input(chuoi_2))
s_find = input('Nhập chuỗi cần tìm:\n')
print('Tuple[', index_duong,']=', tuple_strings[index_duong])
print('Tuple[', index_am,']=', tuple_strings[index_am])
count = tuple_strings.count(s_find)
if count > 0:
    print(s_find, 'xuất hiện trong tuple', count, 'lần')
else:
    print(s_find, 'không xuất hiện trong tuple')