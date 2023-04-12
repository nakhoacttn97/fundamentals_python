import csv

danh_sach = [["Bui Minh","Duc",40],
["Le Thi Kieu","Nga",30]]

f = open("danh_sach_nhan_vien.csv","w",encoding="utf-8",
    newline="")
for nhan_vien in danh_sach:
    csv.writer(f).writerow(nhan_vien)
f.close()
