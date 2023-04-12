print('CT nhập chuỗi và in ra số ký tự, số chữ cái, số chữ số')
# chuoi = input('Chuỗi: ')
chuoi = 'Happy birthday to you 19/5'
print(chuoi)

print('Số ký tự:', len(chuoi))

s = 0
dem = 0
for ky_tu in chuoi:
    if ord('0')<=ord(ky_tu)<=ord('9'):
        dem += 1
print('Số chữ số:', dem)
s += dem

dem = 0
for ky_tu in chuoi:
    if ord('A')<=ord(ky_tu.upper())<=ord('Z'):
        dem += 1
print('Số chữ cái:', dem)
s += dem

dem = 0
for ky_tu in chuoi:
    if ord(ky_tu)==ord(' '):
        dem += 1
print('Số khoảng trắng:', dem)
s += dem

print('Số ký tự khác:', len(chuoi)-s)

from collections import Counter
import re

chuoi_moi = re.sub('[^a-zA-Z]', '', chuoi.lower())
my_count = Counter(chuoi_moi) # sub class của dictionary
print(my_count)
