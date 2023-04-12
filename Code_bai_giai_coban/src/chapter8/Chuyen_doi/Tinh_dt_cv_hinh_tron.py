def Tinh_DT(r):
    dien_tich = PI*r*r
    return dien_tich

def Tinh_CV(r):
    chu_vi = 2*PI*r
    return chu_vi

def Tinh_In_DT_CV(r):
    chu_vi = Tinh_CV(r)
    dien_tich = Tinh_DT(r)
    chuoi = "Chu vi: %.2f" % (chu_vi)
    chuoi += "\nDiện tích: %.2f" % (dien_tich)
    print(chuoi)
# CT chinh
print("CT nhập vào bán kính r --> tính diện tích và chu vi hình tròn")
PI = 3.14
r = float(input("Nhập vào bán kính r = "))
Tinh_In_DT_CV(r)