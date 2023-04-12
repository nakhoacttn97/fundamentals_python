# Bài tập 6
# Hãy viết một phương thức giúp kiểm tra dữ liệu mã zip (zip code) của VN

nhap_ma_zip = int(input('Nhập mã zip:\n'))
ma_zip = range(100000, 880000)
i = 100000
while i < 880000:
    if i == nhap_ma_zip:
        print(True)
        i += 1
    else:
        print(False)
    break
