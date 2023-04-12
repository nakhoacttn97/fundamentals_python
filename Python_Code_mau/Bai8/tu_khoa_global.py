# Từ khóa global trong Python
# Xây dựng hàm
def tong():
    """Khai báo từ khóa global khi thay đổi giá trị của biến toàn cục bên trong function"""
    global c
    c = c + 5
    print(c)

# Gọi hàm
c = 10
tong()