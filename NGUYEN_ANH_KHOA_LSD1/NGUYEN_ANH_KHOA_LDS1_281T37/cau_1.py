# Học viên: Nguyễn Anh Khoa - LDS1_281T37
#
import csv
from csv import reader
def read_csv(filename):
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        for row in csv_reader:
            print(row)

# Cập nhật 4 chữ số đầu trong các số điện thoại
def read_csv_file_to_list(filename):
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        header.append("DienThoai")
        a = list(csv_reader)
        a.insert(0, header)
    return a
data = read_csv_file_to_list('DanhBa.csv')

#def cap_nhat_danh_ba(danh_ba):

# Goi ham
read_csv('DanhBa.csv')

# Chưa xong !!!