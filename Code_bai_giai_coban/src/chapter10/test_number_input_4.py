# bẫy lỗi với nhản lỗi tường minh
so = None
dem = 0
while so == None:
    try:
        dem += 1
        if dem == 4:
            break
        chuoi_so = input("Nhập một số: ")
        so = float(chuoi_so)
        print("Số bạn nhập:", so)
    except ValueError:
        print("Bạn phải nhập số.")
    except Exception as e:
        print("Bạn nhập bị lỗi: "+format(e))
        print("Nhãn lỗi:", type(e).__name__)
