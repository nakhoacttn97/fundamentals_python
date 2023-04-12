diem_trung_binh = eval(input('Nhập điểm trung bình:\n'))
# Xếp loại 
if diem_trung_binh >= 0 and diem_trung_binh <=10:
    if diem_trung_binh < 5:
        print('Yếu/ Kém')
    elif diem_trung_binh < 6:
        print('Trung bình')
    elif diem_trung_binh < 7:
        print('Trung Bình Khá')
    elif diem_trung_binh < 8:
        print('Khá')
    elif diem_trung_binh < 9:
        print('Giỏi')
    else:
        print('Xuất sắc')
else:
    print('Điểm không hợp lệ!') 
