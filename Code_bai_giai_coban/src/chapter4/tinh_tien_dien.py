'''
Created on Feb 2, 2017

@author: KTPHUONG
'''
# tinh tien dien cho ho gia dinh dua theo bieu gia
muc1 = 1484
muc2 = 1533
muc3 = 1786
muc4 = 2242
muc5 = 2503
muc6 = 2587

bac50 = 50
bac100 = 100

tien_dien = 0;

so_kw = eval(input('Số kw tiêu thụ:\n'))
if so_kw <= 50:
    tien_dien = so_kw * muc1
elif so_kw <= 100:
    tien_dien = bac50 * muc1 + (so_kw - bac50) * muc2
elif so_kw <= 200:
    tien_dien = bac50 * muc1 + bac50 * muc2 + (so_kw - bac100) * muc3
elif so_kw <= 300:
    tien_dien = bac50 * muc1 + bac50 * muc2 + bac100 * muc3 + (so_kw - bac50 - bac50 - bac100) * muc4
elif so_kw <= 400:
    tien_dien = bac50 * muc1 + bac50 * muc2 + bac100 * muc3 + bac100 * muc4 + (so_kw - bac50 - bac50 - bac100 - bac100) * muc5
else:
    tien_dien = bac50 * muc1 + bac50 * muc2 + bac100 * muc3 + bac100 * muc4 + bac100 * muc5 + (so_kw - bac50 - bac50 - bac100 - bac100 - bac100) * muc6
print('Tiền điện phải trả=', tien_dien)