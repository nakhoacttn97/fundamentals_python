'''
Created on Feb 14, 2017

@author: KTPHUONG
'''
from datetime import datetime
import calendar

print(datetime.now())

print(datetime(2017, 12, 10))

ngay = int(input('Nhập ngày:\n'))
thang = int (input('Nhập tháng:\n'))
nam = int(input('Nhập năm:\n'))

date1 = datetime.now()
date2 = datetime(nam, thang, ngay)

print('Ngày tháng năm vừa nhập:', date2.strftime('%d - %m - %Y'))

if calendar.isleap(nam):
    print('Năm', nam, 'là năm nhuận' )
else:
    print('Năm', nam, 'không là năm nhuận' )

#print('Thứ trong tuần:',calendar.weekday(nam, thang, ngay))

thu = calendar.weekday(nam, thang, ngay)
chuoi_thu = ''
if thu == 0:
    chuoi_thu = 'Thứ Hai'
elif thu ==1:
    chuoi_thu = 'Thứ Ba' 
elif thu ==2:
    chuoi_thu = 'Thứ Tư'
elif thu ==3:
    chuoi_thu = 'Thứ Năm'
elif thu==4:
    chuoi_thu = 'Thứ Sáu'   
elif thu==5:
    chuoi_thu = 'Thứ Bảy'
elif thu==6:
    chuoi_thu = 'Chủ Nhật'

    
print(date2.strftime('%d - %m - %Y'),'là', chuoi_thu)

print ('Số ngày trong tháng', thang,'là:', calendar.monthrange(nam, thang)[1])

if date1==date2:
    print('Hai ngày trùng nhau.')

    


dateStr = input("Enter a date (mm/dd/yyyy): ")
monthStr, dayStr, yearStr = dateStr.split("/")
print(monthStr)
print(dayStr)
print(yearStr)





