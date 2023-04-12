import xml.dom.minidom
from datetime import datetime

def Xuat_Thong_tin_Phim(Phim):
    Ten = Phim.getAttribute("Ten")
    Nam_san_xuat = Phim.getAttribute("Nam_san_xuat")
    print("Tên phim: %s - Năm sản xuất: %s" % (Ten, Nam_san_xuat))
    The_loai = Phim.getElementsByTagName('The_loai')[0]
    print("Thể loại: %s" % The_loai.childNodes[0].data)
    Dinh_dang = Phim.getElementsByTagName('Dinh_dang')[0]
    print("Định dạng: %s" % Dinh_dang.childNodes[0].data)

Duong_dan_Thu_muc = "XML\\"
Ten_Tap_tin = "phim.xml"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
Tai_lieu = xml.dom.minidom.parse(Duong_dan)
Nut_goc = Tai_lieu.documentElement
Danh_sach_Phim = Nut_goc.getElementsByTagName("PHIM")
for Phim in Danh_sach_Phim:
    Xuat_Thong_tin_Phim(Phim)
    print("\n")

Duong_dan_Thu_muc = "XML\\"
Ten_Tap_tin = "ket_qua_hoc_tap.xml"
Duong_dan = Duong_dan_Thu_muc + Ten_Tap_tin
Tai_lieu = xml.dom.minidom.parse(Duong_dan)
Nut_goc = Tai_lieu.documentElement
Danh_sach_Hoc_sinh = Nut_goc.getElementsByTagName("HOC_SINH")
Chuoi_Dinh_dang = "%Y-%m-%d"
for Hoc_sinh in Danh_sach_Hoc_sinh:
    Ho_ten = Hoc_sinh.getAttribute("Ho_ten")
    Chuoi_Ngay_sinh = Hoc_sinh.getAttribute("Ngay_sinh")
    Ngay_sinh = datetime.strptime(Chuoi_Ngay_sinh, Chuoi_Dinh_dang)
    print("Họ tên: %s - Ngày sinh: %s" % (Ho_ten, Ngay_sinh.strftime("%d/%m/%Y")))
    Danh_sach_Ket_qua = Hoc_sinh.getElementsByTagName("KET_QUA")
    for Ket_qua in Danh_sach_Ket_qua:
        Ma_mon = Ket_qua.getAttribute("Ma_mon")
        Chuoi_Diem = Ket_qua.getAttribute("Diem")
        print("\tMôn: %s - Điểm: %s" % (Ma_mon, Chuoi_Diem))
    print("\n")
