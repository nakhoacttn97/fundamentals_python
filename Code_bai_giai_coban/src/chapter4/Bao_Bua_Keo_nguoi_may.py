import random

print("CT giả lập trò chơi Bao, Búa, Kéo")
print("Người dùng nhập vào các trường hợp ==> 1:BAO 2:BÚA 3:KÉO")
# Nhập
nd_1 = int(input("Người (A) ra: "))
nd_2 = random.randint(1, 3)
print("Máy (B) ra:", nd_2)
# Xử lý
chuoi = ""
if nd_1 == nd_2:
    chuoi = "A hòa với B"
elif (nd_1 == 1 and nd_2 == 2) or (nd_1 == 2 and nd_2 == 3) or (nd_1 == 3 and nd_2 == 1):
    chuoi = "A thắng B"
else:
    chuoi = "B thắng A"
# Xuất kết quả
chuoi_nd_1 = ""
if nd_1 == 1:
    chuoi_nd_1 = "BAO"
elif nd_1 == 2:
    chuoi_nd_1 = "BÚA"
elif nd_1 == 3:
    chuoi_nd_1 = "KÉO"

chuoi_nd_2 = ""
if nd_2 == 1:
    chuoi_nd_2 = "BAO"
elif nd_2 == 2:
    chuoi_nd_2 = "BÚA"
elif nd_2 == 3:
    chuoi_nd_2 = "KÉO"

print("A ra: "+chuoi_nd_1)
print("B ra: "+chuoi_nd_2)
print(chuoi)
