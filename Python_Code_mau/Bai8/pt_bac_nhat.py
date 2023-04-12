# Xây dựng chương trình giải phương trình bậc nhất 1 ẩn

# Xây dựng hàm
def giai_pt_bac_nhat(a, b):
    if a != 0:
        x = -b / a
        print('Phương trình có nghiệm là: ', x)
    elif a == 0 and b != 0:
        print('Phương trình có vô số nghiệm!')
    else:
        print('Phương trình vô nghiệm!')


# Gọi hàm
print('Giải phương trình bậc nhất: ax + b = 0')
a = eval(input('Nhập a:\n'))
b = eval(input('Nhập b:\n'))
giai_pt_bac_nhat(a, b)