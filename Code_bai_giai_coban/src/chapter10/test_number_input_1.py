# bẫy lỗi không tường minh
so = None
try:
    chuoi_so = input("Nhập một số: ")
    so = float(chuoi_so)
    print("Số bạn nhập:", so)
except:
    print("Lỗi nhập số.")

if so != None:
    print("xử lý ...")
