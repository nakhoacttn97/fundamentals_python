# Sử dụng vòng lặp while để duyệt qua các phần tử nhập vào
list_numbers = []               # Tạo một list rỗng
i = 1                           # Cho i = 1 để duyệt vòng lặp
while i==1:
    number = eval(input('Nhập giá trị:\t'))
    list_numbers.append(number)             # Sử dụng append để thêm phần tử vào phía sau một list đã có sẵn
    i = int(input('Tiếp tục nhập giá trị? 1: Có, 0: không\t'))
x = eval(input('Nhập giá trị cần tìm x:\t'))
sum_list = 0
count = 0       # Trả về số lần xuất hiện của chuỗi con trong khoảng [start, end]
for item in list_numbers:
    sum_list += item            # sum_list = sum_list + item
print('List:', list_numbers)
print('Tổng các giá trị trong list:', sum_list)

count = list_numbers.count(x)   # Trả về số lần xuất hiện của x trong list_number
if count > 0:
    print(x,'xuất hiện', count, 'lần trong list')
else:
    print(x, 'không xuất hiện trong list')

for item in list_numbers:
    if x <item:
        print(x, 'không lớn hơn tất cả các số trong list')
        break 
list_so_lon_hon_x = []
for item in list_numbers:
    if x < item:
        list_so_lon_hon_x.append(item)
print('Các số lớn hơn', x, 'trong list:',list_so_lon_hon_x)
    
        