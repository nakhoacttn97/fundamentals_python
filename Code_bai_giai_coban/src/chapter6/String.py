import datetime

Ho_ten = "Thanh Thảo"
Loi_chao = "Xin chào " + Ho_ten
print(Loi_chao)
n = len(Ho_ten)
print("Số ký tự của Họ tên: "+str(n))

Loi_chao = "Xin chào \n\t" + Ho_ten
print(Loi_chao)

Loi_chao = "Xin chào " + Ho_ten
Loi_chao_Hoa = Loi_chao.upper()
print(Loi_chao_Hoa)
Loi_chao_Thuong = Loi_chao.lower()
print(Loi_chao_Thuong)

Ho_ten = "     Thanh Thảo   "
print("Số ký tự của Họ tên: "+str(len(Ho_ten)))
print("Số ký tự của Họ tên: "+str(len(Ho_ten.strip())))

Ho_ten = "Thanh Thảo"
i = Ho_ten.startswith("Thanh")
print(i)
i = Ho_ten.endswith("Thảo")
print(i)

i = Ho_ten.find("Th")
print(i)
i = Ho_ten.find("Th", 2)
print(i)
i = Ho_ten.find("Th", 2, len(Ho_ten)-1)
print(i)

Ho_ten_Thay_the = Ho_ten.replace("Thanh", "Nguyễn Ngọc Thanh ")
print(Ho_ten_Thay_the)

for Ky_tu in Ho_ten:
    print(Ky_tu)

Cau_Tho = "Bước tới đèo ngang bóng xế tà"
Chuoi_Tach = Cau_Tho.split(" ")
print(Chuoi_Tach)
for Tu in Chuoi_Tach:
    print(Tu)
for i in range(len(Chuoi_Tach)):
    print(Chuoi_Tach[i])
for i in range(len(Chuoi_Tach)):
    Chuoi_Tach[i] += " "
print(Chuoi_Tach)
Chuoi = ""
Chuoi = Chuoi.join(Chuoi_Tach)
print(Chuoi)

print(Ho_ten)
print(Ho_ten[6:])
print(Ho_ten[6:8])
print(Ho_ten[2:5])

Ngay_hien_tai = datetime.date.today()
Ngay_sinh = datetime.date(2007, 4, 27)
Nam_sinh = Ngay_sinh.year
Tuoi = Ngay_hien_tai.year - Nam_sinh
Chuoi = "Xin chào %s. Tuổi của bạn là: %d tuổi" % (Ho_ten, Tuoi)
print(Chuoi)
print("Xin chào " + Ho_ten + ". Tuổi của bạn là: " + str(Tuoi) + " tuổi")
print("Xin chào", Ho_ten, ". Tuổi của bạn là:", Tuoi, "tuổi")

x = "Hương"
y = "Hương"
if x == y:
    print("bằng")
else:
    print("không bằng")

x = "Hương"
y = "hương"
if x == y:
    print("bằng")
else:
    print("không bằng")

x = "Hương"
y = "Hương"
if x is y:
    print("bằng")
else:
    print("không bằng")
