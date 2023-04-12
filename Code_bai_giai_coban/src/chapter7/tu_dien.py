'''
Created on Feb 15, 2017

@author: KTPHUONG
'''
'''
Created on Feb 15, 2017

@author: KTPHUONG
'''
dictionary = {'ant': 'con kiến', 'bear':'con gấu', 'cat': 'con mèo', 'dog' : 'con chó'}
i = 1
while i == 1:    
    cv = int(input('Bạn muốn làm gì? 1: Xem từ điển; 2: Tra từ, 3: Thêm từ, 4: Xóa từ\t'))
    if cv == 1:
        print('Dictionary:')
        print('Từ Anh \t Nghĩa Việt')
        for key, value in dictionary.items():
            print(key, '\t ', value)
    elif cv == 2:    
        name_search = input('Nhập từ cần tra:\t')
        if dictionary.get(name_search) != None:
            print(name_search, ':', dictionary.get(name_search))
        else:       
            print('Không tìm thấy từ trong từ điển')
    elif cv == 3:
        word = input('Nhập từ Anh:\t')
        meaning = input('Nhập nghĩa Việt:\t')
        dictionary[word] = meaning
        print('Dictionary:')
        print('Từ Anh \t Nghĩa Việt')
        for key, value in dictionary.items():
            print(key, '\t ', value)
    elif cv == 4:
        word_delete = input('Nhập từ cần xóa:\t')
        x = int(input('Bạn có thật sự muốn xóa hay không? 1: Xóa, 0: Không\t'))
        if x == 1:
            del dictionary[word_delete]
            print('Đã xóa từ trong từ điển')
            print('Dictionary:')
            print('Từ Anh \t Nghĩa Việt')
            for key, value in dictionary.items():
                print(key, '\t ', value)                
    i = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\t'))
