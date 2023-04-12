# Nhập vào một con thú cần tìm
# => Chương trình in ra danh sách các con thú, số lượng các con thú và kết quả tìm kiếm
list_of_animals = ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']
print(list_of_animals)
so_luong = len(list_of_animals)
print('Number of animals:', so_luong)
nhap = str(input('I want to find:\n'))
if nhap in list_of_animals:
    print('There is ', nhap, 'in list of animals')
else:
    print('There is not', nhap, 'in list of animals')