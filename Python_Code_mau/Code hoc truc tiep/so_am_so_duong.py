so = int(input('Nhập số:'))
if so >= 0:
    if so == 0:
        print('Giá trị %i' % so)
    else:
        print('Giá trị %i là số dương'% so)
else:
    print('Giá trị %i là số âm' % so)