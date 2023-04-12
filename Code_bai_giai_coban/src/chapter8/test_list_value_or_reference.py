# test 1: d2 copy data của d1
print("test 1")
d1 = ["Hương", "Thủy", "Bảo", "Hùng"]
d2 = d1.copy()
print("*before")
print("d1:", d1)
print("d2:", d2)
# thay đổi d2
for i in range(len(d2)):
    d2[i] = d2[i].upper()
d2.append("tom")
d2.append("jack")
# xem kết quả
print("*after")
print("d1:", d1)
print("d2:", d2)
# test 2: d2 tham chiếu đến data của d1
print("\ntest 2")
d1 = ["Hương", "Thủy", "Bảo", "Hùng"]
d2 = d1
print("*before")
print("d1:", d1)
print("d2:", d2)
# thay đổi d2
for i in range(len(d2)):
    d2[i] = d2[i].upper()
d2.append("tom")
d2.append("jack")
# xem kết quả
print("*after")
print("d1:", d1)
print("d2:", d2)
