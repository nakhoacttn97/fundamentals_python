# Học viên: Nguyễn Anh Khoa - LDS1_281T37
# Câu 3
# Xây dựng hàm
def so_nguyen(n):
    chuyen_str = str(n)
    chuyen_list = list(chuyen_str)
    tong_list = 0
    for i in chuyen_list:
        tong_list += i
        print('Tổng các chữ số trong n là: ', tong_list)
    tich_list = 0
    for j in chuyen_list:
        tich_list *= j
        print('Tích các chữ số trong n là: ', tich_list)
# Gọi hàm
number = int(input('Nhập vào 1 số nguyên có từ 10 chữ số trở lên: '))
so_nguyen(number)
# Chưa xong