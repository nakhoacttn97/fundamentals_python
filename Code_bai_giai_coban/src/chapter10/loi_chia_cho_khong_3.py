try:
    a = 24
    b = int(input("Nhập số chia: "))
    print("Kết quả %i chia cho %i là %f:" % (a, b, a/b))0
    
except ZeroDivisionError:
    print("Bạn phải nhập số chia khác 0.")    
except Exception as e:
    print("Bạn nhập bị lỗi: "+format(e))
    print("Nhãn lỗi:",type(e).__name__)
