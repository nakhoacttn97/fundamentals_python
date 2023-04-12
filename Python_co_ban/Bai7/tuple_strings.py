# Viết chương trình thực hiện việc xử lý tuple như sau
Tuple = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')

nhap_so_09 = eval(input('Nhập số từ 0 đến 9: '))
nhap_so_9_1 = eval(input('Nhập số từ -1 đến -9: '))
nhap_chuoi = str(input('Nhập chuỗi cần tìm:\n'))

print('Tuple: ', Tuple)
print('Tuple[', nhap_so_09, '] = ', Tuple[nhap_so_09])
print('Tuple[', nhap_so_9_1, '] = ', Tuple[nhap_so_9_1])
print(nhap_chuoi, 'xuất hiện trong Tuple ', Tuple.count(nhap_chuoi), 'lần')