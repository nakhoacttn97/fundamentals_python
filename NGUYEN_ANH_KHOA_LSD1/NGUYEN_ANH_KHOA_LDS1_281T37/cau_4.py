# Học viên: Nguyễn Anh Khoa - LDS1_281T37
# Câu 4
# Tạo listA và listB
import random
listA = random.sample(range(100), k = 10)
listB = random.sample(range(100), k = 15)

print('ListA', listA)
print('listB', listB)

# Tạo listAinB bằng Comprehension
listAinB = list(set(listA) & set(listB))
print('Cách 1 dùng Comprehension:\n', listAinB)
# Tạo listAinB bằng Anonymous Function
listAinB_2 = list(filter(lambda a: a in listB , listA ))
print('Cách 2 dùng hàm ẩn danh:\n', listAinB_2)