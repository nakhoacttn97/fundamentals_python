import getpass 

print('Người dùng nhập vào chuỗi mật khẩu và CT sẽ kiểm tra mật khẩu đó có đủ an toàn không.')
print('1. Ít nhất 1 chữ cái viết thường')
print('2. Ít nhất có 1 ký số từ [0-9]')
print('3. Ít nhất 1 kí tự viết HOA')
print('4. Ít nhất có 1 ký tự đặc biệt trong các giá trị [$ # @]')
print('5. Độ dài mật khẩu tối thiểu: 6')
print('6. Độ dài mật khẩu tối đa: 12')

mat_khau = getpass.getpass(prompt='Mật khẩu: ')

print('\n')
print('Mật khẩu:',mat_khau)
print('Kiểm tra ...')
loi = ''
# kiểm tra 1
hop_le = False
for ky_tu in mat_khau:
    if 'a'<=ky_tu<='z':
        hop_le = True
        break
if not hop_le:
    loi += '- phải có ít nhất 1 chữ cái viết thường\n'

# kiểm tra 2
hop_le = False
for ky_tu in mat_khau:
    if '0'<=ky_tu<='9':
        hop_le = True
        break
if not hop_le:
    loi += '- phải có ít nhất 1 ký số từ [0-9]\n'

# kiểm tra 3 ...

if loi=='':
    print('Mật khẩu an toàn')
else:
    print('Mật khẩu không an toàn.\nLý do:')    
    print(loi)
