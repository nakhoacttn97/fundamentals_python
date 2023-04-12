'''
Created on Feb 15, 2017

@author: KTPHUONG
'''
danh_ba = {'Johnny': '0989741258', 'Katherine':'0903852147', 'Misu': '0913753951', 'Jack' : '0933753654'}
i = 1
while i == 1:    
    cv = int(input('Bạn muốn làm gì? 1: Xem danh bạ; 2: Tìm kiếm, 3: Thêm mới\t'))
    if cv == 1:
        print('Danh bạ điện thoại:')
        print('Tên \t Số điện thoại')
        for key, value in danh_ba.items():
            print(key, ' -- ', value)
    elif cv == 2:    
        name_search = input('Nhập tên cần tìm:\n')
        if danh_ba.get(name_search) != None:
            print(name_search, 'có số điện thoại là:', danh_ba.get(name_search))
        else:       
            print('Không tìm thấy tên này trong danh bạ')
    elif cv == 3:
        ten = input('Nhập tên:\n')
        fone = input('Nhập số điện thoại:\n')
        danh_ba[ten] = fone
        print('Danh bạ điện thoại:')
        print('Tên \t Số điện thoại')
        for key, value in danh_ba.items():
            print(key, ' -- ', value)
    i = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\t'))
