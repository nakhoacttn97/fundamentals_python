'''
Created on Jan 20, 2017

@author: KTPHUONG
'''
import math
def tinh_bmi(can_nang, chieu_cao):
    #tinh BMI cua mot nguoi dua vao can nang va chieu cao
    bmi = can_nang / math.pow(chieu_cao,2)
    return bmi

def danh_gia_bmi(bmi):
    chuoi_kq = ''
    if bmi < 18.5:
        chuoi_kq = 'gầy'
    elif bmi < 25:
        chuoi_kq = 'bình thường'
    else:
        chuoi_kq = 'thừa cân'
    return chuoi_kq
    
can_nang = eval(input('Nhập cân nặng (kg):\n'))
chieu_cao = eval(input('Nhập chiều cao (m):\n'))
bmi = tinh_bmi(can_nang, chieu_cao)
print('Chỉ số BMI của bạn: %.2f'%bmi)
print('Kết quả: Bạn', danh_gia_bmi(bmi))

# hàm trong python có thể trả về nhiều hơn 1 giá trị
def tinh_danh_gia_bmi(can_nang, chieu_cao):
    #tinh BMI cua mot nguoi dua vao can nang va chieu cao
    bmi = can_nang / math.pow(chieu_cao,2)
    # danh gia BMI
    chuoi_kq = ''
    if bmi < 18.5:
        chuoi_kq = 'gầy'
    elif bmi < 25:
        chuoi_kq = 'bình thường'
    else:
        chuoi_kq = 'thừa cân'
    return bmi, chuoi_kq

bmi, chuoi_kq = tinh_danh_gia_bmi(can_nang, chieu_cao)
print('Chỉ số BMI của bạn: %.2f'%bmi)
print('Kết quả: Bạn', chuoi_kq)
