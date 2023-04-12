a, b, c, d = eval(input('Nhập a, b, c, d: \n '))
print('a, b, c, d =', a, b, c, d)
so_lon_nhat = a
so_nho_nhat = a
if so_lon_nhat < b:
    so_lon_nhat = b
if so_lon_nhat < c:
    so_lon_nhat = c
if so_lon_nhat < d:
    so_lon_nhat = d
print('Max =', so_lon_nhat)
if so_nho_nhat > b:
    so_nho_nhat = b
if so_nho_nhat > c:
    so_nho_nhat = c
if so_nho_nhat > d:
    so_nho_nhat = d
print('Min =', so_nho_nhat)