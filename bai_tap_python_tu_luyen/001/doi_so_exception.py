# Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó ở hệ bát phân (Có xử lý ngoại lệ đầu vào)
try:
    thap_phan = int(input('Nhập số hệ thập phân:\n'))
    print('Số thập phân %d trong hệ bát phân là %o' % (thap_phan, thap_phan))
except:
    print('Định dạng đầu vào không hợp lệ')