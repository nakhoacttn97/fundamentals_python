# Viết chương trình tính cước taxi theo biểu phí cơ bản:

xe_4_cho_0_8 = 11000
xe_4_cho_30 = 15300
xe_4_cho_31 = 12100

xe_7_cho_0_8 = 12000
xe_7_cho_30 = 15300
xe_7_cho_31 = 12100

loai_xe = int(input('Loại xe (chỉ nhập 4 hoặc 7):\n'))
so_km_di_chuyen = float(input('Số km di chuyển:\n'))
thoi_gian_cho = int(input('Thời gian chờ (làm tròn theo phút):\n'))

tien_di_chuyen = 0
tien_cho = 0

if thoi_gian_cho > 5:
    tien_cho = (thoi_gian_cho - 5) * 750
if loai_xe == 4:
    if so_km_di_chuyen <= 0.8:
        tien_di_chuyen = xe_4_cho_0_8
    elif so_km_di_chuyen <31:
        tien_di_chuyen = xe_4_cho_0_8 +(so_km_di_chuyen - 0.8) * xe_4_cho_30
    else:
        tien_di_chuyen = xe_4_cho_0_8 + (31 - 0.8) * xe_4_cho_30 + (so_km_di_chuyen - 31) * xe_4_cho_31
if loai_xe == 7:
    if so_km_di_chuyen <= 0.8:
        tien_di_chuyen = xe_7_cho_0_8
    elif so_km_di_chuyen < 31:
        tien_di_chuyen = xe_7_cho_0_8 + (so_km_di_chuyen - 0.8) * xe_7_cho_30
    else:
        tien_di_chuyen = xe_7_cho_0_8 + (31 - 0.8) * xe_7_cho_30 + (so_km_di_chuyen -31) * xe_7_cho_31

    tien_cuoc = tien_di_chuyen + tien_cho

    print ('Tiền chờ = (%d - 5) * 750 = %.0f'%(thoi_gian_cho,tien_cho))
    print('Tiền di chuyển = ',tien_di_chuyen)
    print('Tiền cước = %.0f + %.0f = %.0f'%(tien_di_chuyen, tien_cho, tien_cuoc))

