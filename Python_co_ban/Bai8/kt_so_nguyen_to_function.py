# Nhập vào một số x kiểm tra xem có phải là số nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó)

# Bước 1: Xây dựng hàm
def kt_so_nguyen_to(x):
    if x < 2:
        print(x, "không là số nguyên tố")
    elif x == 2:
        print(x, "là số nguyên tố")
    elif (x % 2) == 0:
        print(x, "không là số nguyên tố")
    else:
        for i in range(x, x + 1):
            if (x % i) == 0:
                print(x, "không là số nguyên tố")
# Bước 2: Gọi hàm
nhap_x = int(input('Nhập x:\n'))
kt_so_nguyen_to(nhap_x)