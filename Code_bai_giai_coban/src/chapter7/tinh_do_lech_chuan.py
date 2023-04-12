import math
# độ lệch chuẩn – Standard deviation (SD)
nhom_1 = [160, 160, 167, 156, 161]
nhom_2 = [142, 150, 187, 180, 145]
n = 5
# trung bình - mean
trung_binh_1 = sum(nhom_1)/n
trung_binh_2 = sum(nhom_2)/n
print('Trung bình nhóm 1:', trung_binh_1)
print('Trung bình nhóm 2:', trung_binh_2)
# phương sai - variance
phuong_sai_1 = sum([(x-trung_binh_1)**2 for x in nhom_1])/(n-1)
phuong_sai_2 = sum([(x-trung_binh_2)**2 for x in nhom_2])/(n-1)
print('Phương sai nhóm 1:', phuong_sai_1)
print('Phương sai nhóm 2:', phuong_sai_2)
# độ lệch chuẩn - standard deviation
std_1 = math.sqrt(phuong_sai_1)
std_2 = math.sqrt(phuong_sai_2)
print('Độ lệch chuẩn nhóm 1:', round(std_1, 2))
print('Độ lệch chuẩn nhóm 2:', round(std_2, 2))
'''
Nhận xét:
- Như vậy độ lệch chuẩn của nhóm 1 là 3.96, độ lệch chuẩn của nhóm 2 là 21.06.
- Như vậy những người ở nhóm 2 có sự khác biệt nhiều hơn so với những người ở nhóm 1.
- Những người trong nhóm 2 nằm cách xa hơn giá trị trung bình so với những người trong nhóm 1.
'''
