# Học viên: Nguyễn Anh Khoa - LDS1_281T37
# Câu 2
# Xây dựng hàm
import math
def tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('là 3 cạnh của 1 tam giác')
        print('Chi vi tam giác là: ', a + b + c)
        # Gọi p là nửa chu vi của tam giác
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Diện tích tam giác là: ', float(s))
        ha = 2 * s / a
        hb = 2 * s / b
        hc = 2 * s / c
        print('3 Đường cao của tam giác lần lượt là: ', '(', float(ha), ',', float(hb), ',', float(hc), ')')
        # Xét tam giác thuộc loại nào (vuông, cân, đều, thường)
        if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            loai_tam_giac = 'Vuông'
        elif a==b and b==c:
            loai_tam_giac = 'Đều'
        elif a==b or a==c or b==c:
            loai_tam_giac = 'Cân'
        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
            loai_tam_giac = 'Tù'
        else:
            loai_tam_giac = 'Nhọn'
        print('Tam giác này thuộc loại: Tam giác', loai_tam_giac)
    else:
        print('không là ba cạnh của một tam giác')

# Gọi hàm
a,b,c = map(float,input('Nhập 3 cạnh của tam giác a,b,c: (nhập số cách khoảng trắng) ').split())
tam_giac(a, b, c)