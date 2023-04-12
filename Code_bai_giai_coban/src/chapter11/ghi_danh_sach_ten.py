danh_sach = ["Thu Thuy","Anh Tuan","Bao Tran"]
# ghi danh_sach xuong tap tin danh_sach.txt
f = open("danh_sach.txt", "w", encoding="utf-8")
for ten in danh_sach:
    f.write(ten+"\n")
f.close()
#
for ten in danh_sach:
    f = open(ten + ".txt", "w", encoding="utf-8")
    f.write("Than moi ban "+ten+ " den du buoi ...")
f.close()
