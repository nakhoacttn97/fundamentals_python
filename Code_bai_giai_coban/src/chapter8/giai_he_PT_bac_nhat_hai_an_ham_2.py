# Giải hệ PT bậc nhất 2 ẩn bằng pp định thức Cramer
# a1x + b1x = c1
# a2x + b2x = c2
# ví dụ: 2x -y = 3 và x + 2y = 4 (nghiệm x=2, y=1)
# Tạo hàm


def Nhap_so(chuoi_nhac):
    so_nhap = float(input(chuoi_nhac))
    return so_nhap


def Gia_tri(a, b, c, d):
    return a*d-c*b


def Giai_PT(a1, b1, c1, a2, b2, c2):
    d = Gia_tri(a1, b1, a2, b2)
    dx = Gia_tri(c1, b1, c2, b2)
    dy = Gia_tri(a1, c1, a2, c2)
    x = None
    y = None
    thong_bao = ""
    if d != 0:
        x = dx/d
        y = dy/d
    elif dx == 0 and dy == 0:
        thong_bao = "PT có vô số nghiệm"
    else:
        thong_bao = "PT vô nghiệm"

    return x, y, thong_bao  # trả về kiểu tuple


# CT chính
# nhập các hệ số
a1 = Nhap_so("a1 = ")
b1 = Nhap_so("b1 = ")
c1 = Nhap_so("c1 = ")
a2 = Nhap_so("a2 = ")
b2 = Nhap_so("b2 = ")
c2 = Nhap_so("c2 = ")
# giải
ket_qua = Giai_PT(a1, b1, c1, a2, b2, c2)
x = ket_qua[0]
y = ket_qua[1]
thong_bao = ket_qua[2]
if x != None:
    print("Nghiệm x=", x, "và y=", y)
else:
    print(thong_bao)
