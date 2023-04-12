# Giải hệ PT bậc nhất 2 ẩn bằng pp định thức Cramer
# a1x + b1x = c1
# a2x + b2x = c2
# ví dụ: 2x -y = 3 và x + 2y = 4 (nghiệm x=2, y=1)
# nhập các hệ số
a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))
# giải
d = a1*b2-a2*b1
dx = c1*b2-c2*b1
dy = a1*c2-a2*c1
if d != 0:
    x = dx/d
    y = dy/d
    print("Nghiệm x=", x, "và y=", y)
elif x == 0 and y == 0:
    print("PT có vô số nghiệm")
else:
    print("PT vô nghiệm")
