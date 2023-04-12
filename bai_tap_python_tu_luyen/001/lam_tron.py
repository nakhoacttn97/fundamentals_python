# Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.
nhap_so = float(input('Nhập số:\n'))
lam_tron_den_B = round(float(input('Cần làm tròn đến bao nhiêu chữu số?\n')), 2)
print('Số thập phân %f sau khi làm tròn đến chữ số thứ 2 là %f' % (nhap_so, lam_tron_den_B)