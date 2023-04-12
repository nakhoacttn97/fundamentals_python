# Viết chương trình xử lý list như sau
# Tạo list
list_numbers = []
so = 1
while so == 1:
    list_numbers.append(eval(input('Nhập giá trị: ')))
    so = int(input('Tiếp tục nhập giá trị? 1: Có, 0: Không '))

# Nhập giá trị cần tìm
x = eval(input('Nhập giá trị cần tìm x: '))

# Sử dụng vòng lặp for để tính tổng
sum_list = 0
count = 0
for item in list_numbers:          # Sử dụng vòng lặp for để duyệt item trong list_numbers
    sum_list += item
print('List:', list_numbers)
print('Tổng các giá trị trong list:', sum_list)

# Sử dụng hàm count để đếm số lần xuất hiện của x trong list_number
count = list_numbers.count(x)
if count > 0:
    print(x, 'xuất hiện', count, 'lần trong list')
else:
    print(x, 'không xuất hiện trong list')

# Sử dụng vòng lặp for để duyệt qua list_numbers xác định xem x có phải là số lớn nhất
for item in list_numbers:
    if x < item:                        # if trong vòng lặp for không nhất thiết phải có else
        print(x, 'không lớn hơn tất cả các số trong list')
        break

# Sử dụng vòng lặp for để duyệt qua list_number
list_so_lon_hon_x = []
for item in list_numbers:
    if x < item:
        list_so_lon_hon_x.append(item)
print('Các số lớn hơn', x, 'trong list', list_so_lon_hon_x)