def tao_list(list_create):
    i = 1
    while i==1:
        number = eval(input('Nhập giá trị:\t'))
        list_create.append(number)    
        i = int(input('Tiếp tục nhập giá trị? 1: Có, 0: không\t'))
    return list_create

def kiem_tra_so_nguyen_to(so):
    if so <= 1:
        return False
    count = 0;
    for i in range(1, so+1, 1):
        if so % i == 0:
            count += 1
    return count == 2

def tao_list_am(list_create):
    list_negative = []
    for item in list_create:
        if item < 0:
            list_negative.append(item)
    return list_negative
        
def tao_list_duong(list_create):
    list_positive = []
    for item in list_create:
        if item > 0:
            list_positive.append(item)
    return list_positive

def tinh_tong(list_create):
    tong = 0
    for item in list_create:
        tong += item
    return tong

list_numbers_new = []
list_numbers_new = tao_list(list_numbers_new)

list_so_NT = []
for item in list_numbers_new:
    if kiem_tra_so_nguyen_to(item):
        list_so_NT.append(item)

print('List:', list_numbers_new)
print('Các số nguyên tố trong list:', list_so_NT)

list_am = []
list_am = tao_list_am(list_numbers_new)
print('Các phần tử âm trong list:', list_am)
print('Trung bình cộng các phần tử âm: %.2f'%(tinh_tong(list_am)/len(list_am)))

list_duong = []
list_duong = tao_list_duong(list_numbers_new)
print('Các phần tử dương trong list:', list_duong)
print('Trung bình cộng các phần tử dương: %.2f'%(tinh_tong(list_duong)/len(list_duong)))

print('Giá trị max trong list', max(list_numbers_new))
print('Giá trị min trong list', min(list_numbers_new))

list_numbers_new.sort()
print('List sắp tăng dần:', list_numbers_new )



