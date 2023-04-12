# Bài tập 7.13
# Khai báo và khởi tạo set1, set2
# Cho phép người dùng lần lượt nhập các phần tử số cho set1 cho đến khi không muốn nhập nữa
set_1 = set()
while True:
    set_1.add(eval(input('Nhập giá trị cho element trong set 1: ')))
    thoat_1 = int(input('Bạn có tiếp tục nhập set 1? 1: có, khác 1: không    '))
    if thoat_1 != 1:
        break
# Set 2
set_2 = set()
while True:
    set_2.add(eval(input('Nhập giá trị cho element trong set 2: ')))
    thoat_2 = int(input('Bạn có tiếp tục nhập set 2? 1: có, khác 1: không    '))
    if thoat_2 != 1:
        break

print('Set 1: ', set_1)
print('Set 2: ', set_2)
# Cho biết mỗi set có bao nhiêu phần tử
print('Chiều dài Set 1: ', len(set_1))
print('Chiều dài Set 2: ', len(set_2))
# Tổng giá trị các phần tử của mỗi set
print('Tổng Set 1: ', sum(set_1))
print('Tổng Set 2: ', sum(set_2))
# Tìm giá trị lớn nhất, nhỏ nhất của set 1
max_set_1 = max(set_1)
min_set_1 = min(set_1)
print('Max Set 1, Min Set 1: ', max_set_1, min_set_1)
# Tìm giá trị lớn nhất, nhỏ nhất của set 2
max_set_2 = max(set_2)
min_set_2 = min(set_2)
print('Max Set 2, Min Set 2: ', max_set_2, min_set_2)
# Lấy ra một phần tử ở set_1 và in ra phần tử này
pop_set_1 = set_1.pop()
print('Pop Set 1: ', pop_set_1)
print('Set 1 sau khi pop: ', set_1)
# Thực hiện set union của set1 và set2 và in kết quả
set_union = set_1 | set_2
print('Set 1 union Set 2: ', set_union)
# Thực hiện set intersection của set1 và set2 và in kết quả
set_intersection = set_1 & set_2
print('Set 1 intersection Set 2: ', set_intersection)
# Thực hiện set difference của set1 với set2 và in kết quà
set_difference = set_1 - set_2
print('Set 1 difference Set 2: ', set_difference)
# Thực hiện set symmetric difference của set1 với set2 và in kết quà
set_symmetric = set_1 ^ set_2
print('Set 1, Set 2 symmetric difference: ', set_symmetric)
# Sắp xếp set1 tăng dần và set2 giảm dần
print('Set 1 tăng dần: ', sorted(set_1))
print('Set 2 giảm dần: ', sorted(set_2, reverse=True))