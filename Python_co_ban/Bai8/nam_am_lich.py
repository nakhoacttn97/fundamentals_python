# Viết chương trình tính năm âm lịch từ năm dương lịch
# Bước 1: Xây dựng hàm
# C1
def tinh_can(nam):
    can = nam % 10
    chuoi_can = ''
    if can == 0:
        chuoi_can = 'Canh'
    elif can == 1:
        chuoi_can = 'Tân'
    elif can == 2:
        chuoi_can = 'Bính'
    elif can == 7:
        chuoi_can = 'Đinh'
    elif can == 8:
        chuoi_can = 'Mậu'
    else:
        chuoi_can = 'Kỷ'
    return  chuoi_can

def tinh_chi(nam):
    chuoi_chi = ''
    chi = nam % 12
    if chi == 0:
        chuoi_chi = 'Thân'
    elif chi == 1:
        chuoi_chi = 'Dậu'
    elif chi == 2:
        chuoi_chi = 'Tuất'
    elif chi == 3:
        chuoi_chi = 'Hợi'
    elif chi == 4:
        chuoi_chi = 'Tý'
    elif chi == 5:
        chuoi_chi = 'Sửu'
    elif chi == 6:
        chuoi_chi = 'Dần'
    elif chi == 7:
        chuoi_chi = 'Mão'
    elif chi == 8:
        chuoi_chi = 'Thìn'
    elif chi == 9:
        chuoi_chi = 'Tỵ'
    elif chi == 10:
        chuoi_chi = 'Ngọ'
    else:
        chuoi_chi = 'Mùi'
    return  chuoi_chi


# Bước 2: Gọi hàm
nam = int(input('Nhập năm:\n'))
# print C1
print('Năm', nam, 'âm lịch là năm', tinh_can(nam), tinh_chi(nam))
