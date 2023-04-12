# kiem tra nhap mot so nguyen
try:
    so = int(input("Nhap mot so nguyen: "))
    print(so)
except ValueError:
    print("Phai nhap so nguyen.")    
except Exception as e:
    print("Bạn nhập bị lỗi: "+format(e))
    print("Nhãn lỗi:",type(e).__name__)
