'''
Created on Feb 2, 2017

@author: KTPHUONG
'''
# tinh tien lai gui tiet kiem
lai_suat_1_nam = eval(input('Lãi suất 1 năm (%):\n'))
so_tien_gui = eval(input('Số tiền gửi:\n'))
so_thang_gui = eval(input('Số tháng gửi:\n'))
tien_lai = so_tien_gui * so_thang_gui * lai_suat_1_nam/100/12
tien_von_va_lai = so_tien_gui + tien_lai
print('Tiền lãi = ', tien_lai)
print('Tiền vốn + lãi = %.0f + %.0f = %.0f'%(so_tien_gui, tien_lai,tien_von_va_lai)) 