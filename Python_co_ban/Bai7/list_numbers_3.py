# Viết chương trình thực hiện xử lý list như sau
# Tạo list_numbers_3 với 10 đơn vị chiều cao (đơn vị chiều cao tính là inch)
list_numbers_3 = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
# Đổi inch sang mét (1 inch == 0.0245 mét)
list_doi_met = []
i = 0
for i in list_numbers_3:
    i *= 0.0245
    list_doi_met.append(i)
print('Đổi inch sang mét:', list_doi_met)
# In ra 3 chiều cao đầu tiên và 3 chiều cao cuối cùng
sub_list_1 = list_numbers_3[:3]
sub_list_2 = list_numbers_3[-3:]
print('3 chiều cao đầu tiên:', sub_list_1)
print('3 chiều cau cuối cùng', sub_list_2)
# In ra chiều cao trung bình, chiều cao lớn nhất, chiều cao nhỏ nhất
chieu_cao_tb = sum(list_doi_met) / len(list_doi_met)
chieu_cao_lon_nhat = max(list_doi_met)
chieu_cao_nho_nhat = min(list_doi_met)
print('Chiều cao trung bình:', chieu_cao_tb)
print('Chiều cao lớn nhất:', chieu_cao_lon_nhat)
print('Chiều cao nhỏ nhất:', chieu_cao_nho_nhat)
# Sắp xếp list theo giá trị tăng dần
list_doi_met.sort()
print('Sắp xếp list theo giá trị tăng dần:', list_doi_met)
list_doi_met.sort(reverse=True)
print('Sắp xếp list theo giá trị giảm dần:', list_doi_met)