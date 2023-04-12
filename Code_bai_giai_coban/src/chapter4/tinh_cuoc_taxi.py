
# tinh cuoc taxi

muc_gia_4_0_8 = 11000
muc_gia_4_30 = 15300
muc_gia_4_31 = 12100

muc_gia_7_0_8 = 12000
muc_gia_7_30 = 16100
muc_gia_7_31 = 13800

loai_xe = int(input('Loại xe (chỉ nhập 4 hoặc 7):\n'))
so_km = eval(input('Số km di chuyển:\n'))
thoi_gian_cho = int(input('Thời gian chờ (làm tròn theo phút):\n'))
tien_di_chuyen = 0
tien_cho = 0

if thoi_gian_cho > 5:
    tien_cho = (thoi_gian_cho - 5) * 750
if loai_xe == 4:
    if so_km <= 0.8:
        tien_di_chuyen = muc_gia_4_0_8
    elif so_km < 31:
        tien_di_chuyen = muc_gia_4_0_8 + (so_km - 0.8) * muc_gia_4_30
    else:
        tien_di_chuyen = muc_gia_4_0_8 + (31 - 0.8) * muc_gia_4_30 + (so_km - 31) * muc_gia_4_31
if loai_xe == 7: 
    if so_km <= 0.8:
        tien_di_chuyen = muc_gia_7_0_8
    elif so_km < 31:
        tien_di_chuyen = muc_gia_7_0_8 + (so_km - 0.8) * muc_gia_7_30
    else:
        tien_di_chuyen = muc_gia_7_0_8 + (31 - 0.8) * muc_gia_7_30 + (so_km - 31) * muc_gia_7_31

tien_cuoc = tien_di_chuyen + tien_cho

print('Tiền chờ = (%d - 5) * 750đ = %.0f'%(thoi_gian_cho,tien_cho))
print('Tiền di chuyển = ', tien_di_chuyen)
print('Tiền cước = %.0f + %.0f = %.0f'%(tien_di_chuyen, tien_cho, tien_cuoc))
