lai_suat_nam = int(input('Lãi suất 1 năm (%):\n'))
so_tien_gui = int(input('Số tiền gửi:\n'))
so_thang_gui = int(input('Số tháng gửi:\n'))

tien_lai = (so_tien_gui*so_thang_gui)*(lai_suat_nam/100/12)
tong_so_tien = so_tien_gui + tien_lai

print('Tiền lãi =', tien_lai)
print('Tiền vốn + lãi = %.0f + %.0f = %.0f'%(so_tien_gui,tien_lai, tong_so_tien))