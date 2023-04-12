# Nhập vào một số x kiểm tra xem có phải là số nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó)

x = int(input('Nhập x:\n'))
ket_qua = True

if x < 2:
    ket_qua = False
elif x == 2:
    ket_qua = True
elif (x % 2) == 0:
    ket_qua = False
else:
    for i in range(3, x, 2):
        if (x % i == 0):
            ket_qua = False

if ket_qua == True:
    print(x, "là số nguyên tố")
else:
    print(x, "không là số nguyên tố")