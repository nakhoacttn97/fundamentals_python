# Bài tập 6.11 Xây dựng chương trình xử lý ngày, tháng, năm
# ĐÃ XONG
# Nhập
ngay = int(input('Nhập ngày:\n'))
thang = int(input('Nhập tháng:\n'))
nam = int(input('Nhập năm:\n'))

# Xây dựng chương trình
print('Ngày tháng năm vừa nhập: ', ngay, '-', thang, '-', nam)
# Xác định năm nhuận. Nếu năm đó chia hết cho 400 (hặc chia hết cho 4) và không chia hết cho 100
if nam % 4 == 0 and nam % 100 != 0:
    print('Năm ', nam, 'là năm nhuận')
else:
    print('Năm ', nam, 'không là năm nhuận')

# Xác định ngày/tháng/năm vừa nhập là thứ mấy
import calendar
thu = calendar.weekday(nam, thang, ngay)
if thu == 0:
    thu = 'Thứ Hai'
elif thu == 1:
    thu = 'Thứ Ba'
elif thu == 2:
    thu = 'Thứ Tư'
elif thu == 3:
    thu = 'Thứ Năm'
elif thu == 4:
    thu = 'Thứ Sáu'
elif thu == 5:
    thu = 'Thứ Bảy'
else:
    thu = 'Chủ Nhật'
print(ngay, '-', thang, '-', nam, 'là', thu)

# Xác định số ngày trong tháng
so_ngay = calendar.monthrange(nam, thang)
print('Số ngày trong tháng ', thang, 'là:', so_ngay[-1])