try:
    a = 24
    b = int(input("Nhập số chia: "))
    print("Kết quả %i chia cho %i là %f:" % (a, b, a/b))
except Exception as e:
    print("Bạn nhập bị lỗi: "+format(e))
    print("Nhãn lỗi:",type(e).__name__)

