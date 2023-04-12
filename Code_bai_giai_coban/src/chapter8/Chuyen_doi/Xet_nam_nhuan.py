import datetime

print("CT xét năm nhập vào có là năm nhuần hay không?")
nam_xet = int(input("Năm xét ? "))
la_nam_nhuan = (nam_xet % 4 == 0 and nam_xet % 100 != 0) or nam_xet % 400 == 0
if la_nam_nhuan:
    print("Năm %d là năm nhuần." % (nam_xet))
else:
    print("Năm %d không là năm nhuần." % (nam_xet))

# xét năm hiện tại có là năm nhuấn?
now = datetime.datetime.now()
print("Năm hiện tại:", now.strftime("%Y"))
nam_xet = int(now.strftime("%Y"))
la_nam_nhuan = (nam_xet % 4 == 0 and nam_xet % 100 != 0) or nam_xet % 400 == 0
if la_nam_nhuan:
    print("Năm %d là năm nhuần." % (nam_xet))
else:
    print("Năm %d không là năm nhuần." % (nam_xet))
