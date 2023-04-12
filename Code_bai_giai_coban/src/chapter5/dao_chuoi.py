print('CT đảo các từ trong chuỗi')
chuoi = input('Nhập chuỗi muốn đảo: ')
for tu in chuoi.split():
    print(tu[::-1])

print('-'*30)
for tu in chuoi.split()[::-1]:
    print(tu[::-1])