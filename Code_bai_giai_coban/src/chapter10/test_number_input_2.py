# khi xảy ra lỗi thì in thông báo lỗi và nhãn lỗi
so = None
try:
    chuoi_so = input("Nhập một số: ")
    so = float(chuoi_so)
    print("Số bạn nhập:", so)
except Exception as e:
    print("Bạn nhập bị lỗi: "+format(e))
    print("Nhãn lỗi:",type(e).__name__)

if so != None:
    print("xử lý ...")
