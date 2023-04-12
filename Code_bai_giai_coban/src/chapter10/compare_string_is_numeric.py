def check_int(chuoi_so):
    la_so = True
    try:
        int(chuoi_so)
    except:
        la_so = False
    return la_so


def check_float(chuoi_so):
    la_so = True
    try:
        float(chuoi_so)
    except:
        la_so = False
    return la_so


chuoi_so = input("Nhập một số nguyên: ")
if check_int(chuoi_so):
    so = int(chuoi_so)
    print("Số nguyên bạn nhập:", so)
else:
    print("Bạn phải nhập số nguyên")
"""
chuoi_so = input("Nhập một số thực: ")
if check_float(chuoi_so):
    so = float(chuoi_so)
    print("Số thực bạn nhập:", so)
else:
    print("Bạn phải nhập số thực")
"""