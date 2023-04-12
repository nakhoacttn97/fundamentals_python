hk1 = eval(input('Điểm HK1: '))
hk2 = eval(input('Điểm HK2: '))
dtb = (hk1 + hk2 * 2) / 3

if 0 <= dtb <= 10:
    if dtb >= 9:
        print("Xuất sắc")
    elif dtb >= 8:
        print("Giỏi")
    elif dtb >= 7:
        print("Khá")
    elif dtb >= 6:
        print("Trung bình - Khá")
    elif dtb >= 5:
        print("Trung bình")
    else:
        print("Yếu - Kém")
else:
    print('Điểm không hợp lệ')