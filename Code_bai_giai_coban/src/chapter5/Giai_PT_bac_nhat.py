print("Giải PT bậc nhất: ax + b = 0")
tiep_tuc = True
while tiep_tuc:
    a = float(input("a = "))
    b = float(input("b = "))
    print("Giải PT bậc nhất:", a, "x", "+", b, "= 0")
    if a != 0:
        x = -b/a
        print("Nghiệm x =", x)
    elif b == 0:
        print("PT có vô số nghiệm.")
    else:
        print("PT vô nghiệm.")
    # Có tiếp tục ?
    tra_loi = input("Bạn có tiếp tục (y)?. Xin trả lời: ")
    if tra_loi.upper() != "Y":
        tiep_tuc = False
