import csv

f = open("danh_sach_nhan_vien.csv","r",encoding="utf-8")
for d in csv.reader(f):
    chuoi = "Ho ten: " + d[0] + " " + d[1]
    chuoi += "\nTuoi: " + str(d[2])
    print(chuoi)
f.close()

