# Viết chương trình tính chỉ số BMI
# Xây dựng hàm
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao * 2)
    if bmi < 18.5:
        print('Kết quả: Bạn gầy')
    elif 18.5 <= bmi <= 24.99:
        print('Kết quả: Bạn bình thường')
    else:
        print('Kết quả : Bạn thừa cân')

# Gọi hàm
nhap_can_nang = eval(input('Nhập cân nặng (kg):\n'))
nhap_chieu_cao = float(input('Nhập chiều cao (m):\n'))

ket_qua_bmi = nhap_can_nang / (nhap_chieu_cao * 2)

print('Chỉ số BMI của bạn là:', ket_qua_bmi)
tinh_bmi(nhap_can_nang, nhap_chieu_cao)