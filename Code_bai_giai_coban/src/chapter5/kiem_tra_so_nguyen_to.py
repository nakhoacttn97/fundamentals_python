'''
Created on Feb 9, 2017

@author: KTPHUONG
'''
# kiem tra so nguyen to
x = int(input('Nhập x:\n'))
count = 0
for i in range(1, x+1):
    if x%i == 0:
        count = count + 1
if count == 2:
    print('%d là số nguyên tố'%x)
else:
    print('%d không là số nguyên tố'%x)
    