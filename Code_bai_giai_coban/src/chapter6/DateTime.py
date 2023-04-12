from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
import calendar

Thoi_gian_hien_tai = datetime.now()
print("Thời gian hiện tại: ", Thoi_gian_hien_tai)
Ngay_hien_tai = date.today()
print("Ngày hôm nay: ", Ngay_hien_tai)

Danh_sach_Ten_thu_trong_tuan = [
    "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ nhật"]
Thu_trong_tuan = Ngay_hien_tai.weekday()
Ten_Thu_trong_tuan = Danh_sach_Ten_thu_trong_tuan[Thu_trong_tuan]
Ngay = Ngay_hien_tai.day
Thang = Ngay_hien_tai.month
Nam = Ngay_hien_tai.year
print("%s, Ngày %d Tháng %d Năm %d" % (Ten_Thu_trong_tuan, Ngay, Thang, Nam))

Gio = Thoi_gian_hien_tai.hour
Phut = Thoi_gian_hien_tai.minute
Giay = Thoi_gian_hien_tai.second
Phan_ngan_giay = Thoi_gian_hien_tai.microsecond
print("%d Giờ - %d Phút - %d Giây - %d" % (Gio, Phut, Giay, Phan_ngan_giay))

Gio_hien_tai = datetime.time(datetime.now())
print("Giờ hiện tại: ", Gio_hien_tai)

print("%s, %s %s" % (Ngay_hien_tai.strftime("%B"),
                     Ngay_hien_tai.strftime("%d"), Ngay_hien_tai.strftime("%Y")))
print(Thoi_gian_hien_tai.strftime("%I:%M:%S %p"))
print(Thoi_gian_hien_tai.strftime("%A"))
print(Thoi_gian_hien_tai.strftime("%H:%M:%S"))

Ngay_sinh = date(2007, 4, 27)
print("Ngày sinh:", Ngay_sinh.strftime("%d/%m/%Y"))
Chenh_lech = relativedelta.relativedelta(Ngay_hien_tai, Ngay_sinh)
Tuoi = Chenh_lech.years
print("Tuổi:", Tuoi)

Chuoi_Dinh_dang = "%d/%m/%Y"
Chuoi_Ngay_vao = "22/11/1980"
Ngay_vao = datetime.strptime(Chuoi_Ngay_vao, Chuoi_Dinh_dang)
print("Ngày vào làm:", Ngay_vao.strftime("%d/%m/%Y"))
Chenh_lech = relativedelta.relativedelta(Ngay_hien_tai, Ngay_vao)
Tham_nien = Chenh_lech.years
print("Thâm niên:", Tham_nien)

Ngay_ke = Ngay_hien_tai + timedelta(days=1)
print("Ngày mai:", Ngay_ke)
Ngay_truoc = Ngay_hien_tai - timedelta(days=1)
print("Ngày hôm qua:", Ngay_truoc)

print(calendar.isleap(2016))
print(calendar.monthcalendar(2016,2))

Thu_trong_tuan = calendar.weekday(2018,4,26)
Ten_Thu_trong_tuan = Danh_sach_Ten_thu_trong_tuan[Thu_trong_tuan]
print(Ten_Thu_trong_tuan)
print(calendar.monthrange(2018,4))
