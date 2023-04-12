'''
Created on Feb 15, 2017

@author: KTPHUONG
'''
# tinh can, chi => in năm ăm lịch
def tinh_can(nam):
    # tinh can = nam % 10
    chuoi_can = ''
    can = nam % 10
    if can == 0:
        chuoi_can = 'Canh'
    elif can == 1:
        chuoi_can = 'Tân'
    elif can == 2:
        chuoi_can = 'Nhâm'
    elif can == 3:
        chuoi_can = 'Quý'
    elif can == 4:
        chuoi_can = 'Giáp'
    elif can == 5:
        chuoi_can = 'Ất'
    elif can == 6:
        chuoi_can = 'Bính'
    elif can == 7:
        chuoi_can = 'Đinh'
    elif can == 8:
        chuoi_can = 'Mậu'
    else:
        chuoi_can = 'Kỷ'
    return chuoi_can

def tinh_chi(nam):
    #tinh chi = nam % 12
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
    elif chi == 11:
        chuoi_chi = 'Mùi'
    return chuoi_chi
  
def tinh_can_2(list_can, nam):    
    can = nam%10
    return list_can[can]

def tinh_chi_2(list_chi, nam):    
    chi = nam%12
    return list_chi[chi]

list_can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
list_chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

nam = int(input('Nhập năm:\n'))
print('Năm', nam, 'âm lịch là năm', tinh_can(nam), tinh_chi(nam))

print('Năm', nam, 'âm lịch là năm', tinh_can_2(list_can, nam), tinh_chi_2(list_chi, nam))
