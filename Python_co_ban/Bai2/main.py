hk1 = eval(input('Điểm HK1: '))
hk2 = eval(input('Điểm HK2: '))
dtb = (hk1 + hk2 * 2)/3
print('Điểm trung bình:', dtb)
if dtb >= 5:
    print('Kết quả: Đậu')
else:
    print('Kết quả: Rớt')