# Bài tập 6/ ĐÃ XONG
# Viết lại bài tìm |x| bằng cách sử dụng hàm abs


x = eval(input('Nhập x:'))
abs_x = x
if abs_x < 0:
    abs_x = -abs_x
    print('|%d| = %d'%(x, abs_x))