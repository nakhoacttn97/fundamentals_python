# Viết chương trình tính năm âm lịch từ năm dương lịch
# Bước 1: Xây dựng hàm
# C2
def tinh_can(list_can, nam):
    can = nam % 10
    return list_can[can]

def tinh_chi(list_chi, nam):
    chi = nam % 12
    return list_chi[chi]

list_can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
list_chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

# Bước 2: Gọi hàm
nam = int(input('Nhập năm:\n'))

#print C2
print('Năm', nam, 'âm lịch là năm', tinh_can(list_can, nam), tinh_chi(list_chi, nam))