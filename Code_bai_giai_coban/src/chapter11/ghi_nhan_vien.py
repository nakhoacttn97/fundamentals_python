nhan_vien = ["Tran Minh Bao","Ngoc",25]
f = open("nhan_vien.txt", "w", encoding="utf-8")
chuoi = "Ho ten: " + nhan_vien[0] + " " + nhan_vien[1]
chuoi += "\nTuoi: " + str(nhan_vien[2])
f.write(chuoi)
f.close()
#
nhan_vien = {"Ho":"Tran Minh Bao","Ten":"Ngoc","Tuoi":25}
f = open("nhan_vien.txt", "w", encoding="utf-8")
chuoi = "Ho ten: " + nhan_vien["Ho"] + " " + nhan_vien["Ten"]
chuoi += "\nTuoi: " + str(nhan_vien["Tuoi"])
f.write(chuoi)
f.close()