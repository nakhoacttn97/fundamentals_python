# Học viên Nguyễn Anh Khoa - LDS1_281T37
# Câu 6
# a) Đọc và in nội dung trong file từng dòng một.
import csv
from csv import reader
def read_csv_nhan_su(filename):
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        for row in csv_reader:
            print(row)
read_csv_nhan_su('NhanSu.csv')

# b) Cập nhật tiền lương cho các nhân viên bị thiếu
def read_csv_file_to_list(filename):
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        header.append("Salary")
        a = list(csv_reader)
        a.insert(0, header)
    return

data = read_csv_file_to_list('NhanSu.csv')

def cap_nhat_tien_luong(Dept):
    if 'KT' in Dept:
        return '1500'
    elif 'IT' in Dept:
        return '1600'
    elif 'TCHC' in Dept:
        return '1450'
for Dept in data:
    if Dept[4]=='?':
        Dept[4] = cap_nhat_tien_luong(Dept)


# e) Lưu thông tin của toàn bộ nhân viên sau khi đã cập nhật tiền lương và tính tiền Overtime vào trong file NhanSu2.csv
def write_csv_file(filename, listContent):
    f = open(filename,'w+', newline='')
    for item in listContent:
        csv.writer(f).writerow(item)
    f.close()
write_csv_file('NhanSu2.csv',data)

# Chưa xong !!!