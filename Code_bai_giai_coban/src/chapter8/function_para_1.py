# Khai báo hàm
def Tinh_In_Tong(a, b):
    tong = a+b
    print("Tổng %i + %i = %i" % (a, b, tong))


def Tinh_Tong(a, b):
    tong = a+b
    return tong


# CT chính
Tinh_In_Tong(34, 25)  # truyền literal
a = 14
b = 25
Tinh_In_Tong(a, b)  # truyền variable
print("\n")
a = 17
b = 15
tong = Tinh_Tong(a, b)
print("Tổng %i + %i = %i" % (a, b, tong))
