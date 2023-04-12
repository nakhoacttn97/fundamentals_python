# Tạo một danh bạ kiểu dictionary để lưu trữ danh bạ điện thoại với các cặp key-value
danh_ba = dict([('Johnny', '0989741258'), ('Katherine', '0903852147'), ('Misu', '0913753951'), ('Jack', '0933753654')])
# Sửu dụng vòng lặp

while True:
    what_do = eval(input('Bạn muốn làm gì? 1: Xem danh bạ; 2: Tìm kiếm; 3: Thêm mới'))
    if what_do == 1:
        print('Danh bạ điện thoại:')
        print('Tên         Số điện thoại')
        for key, value in danh_ba.items():
            print(key, '--', value)
        tiep_tuc = eval(input('Tiếp tục lựa chọn? 1: có; 0: Không'))

    elif what_do == 2:
        tim_ten = str(input('Nhập tên cần tìm:\n'))
        for name in danh_ba:
            if name == tim_ten:
                print(name, 'có số điện thoại là: ', )
            else:
                print('Không tìm thấy')
    elif what_do == 3:
        them_ten = str(input('Nhập tên:\n'))
        them_sdt = int(input('Nhập số điện thoại:\n'))
        danh_ba[them_ten] = them_sdt
        print('Danh bạ điện thoại:')
        print('Tên         Số điện thoại')
        for key, value in danh_ba.items():
            print(key, '--', value)