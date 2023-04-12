# CT xét năm nhập vào có là năm nhuần hay không?

nam = int(input('Năm xét ?'))

if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
        print('Năm nhuần')
else:
    print('Năm không nhuần')
