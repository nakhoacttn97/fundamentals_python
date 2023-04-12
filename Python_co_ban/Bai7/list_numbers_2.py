# Viết chương trình xử lý list như sau
# Tạo list
list_numbers_2 = []
i = 1
while i == 1:
    list_numbers_2.append(eval(input('Nhập giá trị: ')))
    i = int(input('Tiếp tục nhập giá trị? 1: Có, 0: Không '))
print('List:', list_numbers_2)
# Dòng vòng lặp duyệt qua list tìm ra các số nguyên tố
lis_so_ng_to = []
ket_qua = True
x = 0
for x in list_numbers_2:
    if x < 2:
        ket_qua = False
    elif x == 2:
        ket_qua = True
    elif (x % 2) == 0:
        ket_qua = False
    else:
        for i in range(3, x, 2):
            if (x % i == 0):
                ket_qua = False

if ket_qua == True:
    lis_so_ng_to.append(x)
    print('Các số nguyên tố trong list:', lis_so_ng_to)
else:
    print('Không có số nguyên tố trong list')

# Trung bình cộng của các phần tử âm/ phần tử dương trong list
phan_tu_am = []
iam = 0
for iam in list_numbers_2:
    if iam < 0:
        phan_tu_am.append(iam)
print('Các phần tử âm trong list:', phan_tu_am)
tb_am = sum(phan_tu_am) / len(phan_tu_am)
print('Trung bình cộng các phần tử âm:', tb_am)
phan_tu_duong = []
iduong = 0
for iduong in list_numbers_2:
    if iduong > 0:
        phan_tu_duong.append(iduong)
print('Các phần tử dương trong list:', phan_tu_duong)
tb_duong = sum(phan_tu_duong) / len(phan_tu_duong)
print('Trung bình cộng các phần tử dương', tb_duong)
# Tìm max/min trong list
print('Giá trị max trong list ', max(list_numbers_2))
print('Giá trị min trong list ', min(list_numbers_2))
# Sắp xếp list theo giá trị tăng dần
list_numbers_2.sort()
print('List sắp tăng dần: ', list_numbers_2)