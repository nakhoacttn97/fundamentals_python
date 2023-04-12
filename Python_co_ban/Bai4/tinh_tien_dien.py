# Viết chương trình tính tiền điện dành cho hộ gia đình

tieu_thu = eval(input('Số kwh tiêu thụ:\n'))

if tieu_thu >= 0:
    if 0 <= tieu_thu <= 50:
        tien_dien = tieu_thu * 1484
    elif 51 <= tieu_thu <= 100:
        tien_dien = tieu_thu * 1484 + (tieu_thu - 50) * 1533
    elif 101 <= tieu_thu <= 200:
        tien_dien = tieu_thu * 1484 + 50 * 1533 + (tieu_thu - 100) * 1786
    elif 201 <= tieu_thu <= 300:
        tien_dien = tieu_thu * 1484 + 50 * 1533 + 100 * 1786 + (tieu_thu - 200) * 2242
    elif 301 <= tieu_thu <= 400:
        tien_dien = tieu_thu * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + (tieu_thu - 300) * 2503
    else:
        tien_dien = tieu_thu * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + 100 * 2503 + (tieu_thu - 400) * 2587

print('Tiền điện phải trả = ', tien_dien)