try:
    a = 24
    b = int(input("Nhập số chia: "))
    print("Kết quả %i chia cho %i là %f:" % (a, b, a/b))
except:
    print("Lỗi chia %i/%i." % (a, b))
