# Nhập
try:
    so_1 = int(input('Nhập vào số nguyên thứ nhất:\n'))
    so_2 = int(input('Nhập vào số nguyên thứ hai:\n'))
    tong = so_1 + so_2
    print('Tổng của hai số nguyên vừa nhập là:', tong)
except:
    print('định dạng đầu vào không hợp lệ')