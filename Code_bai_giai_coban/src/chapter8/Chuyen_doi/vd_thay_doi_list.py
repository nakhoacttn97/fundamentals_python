danh_sach = ["Thuy","Mai","Tung","Thao"]
"""
# cach 1
for ten in danh_sach:
    ten = ten.upper()
    print(ten)

for ten in danh_sach:
    print(ten)
"""
# cach 2
for i in range(len(danh_sach)):
    ten = danh_sach[i]
    danh_sach[i] = ten.upper()
    
for ten in danh_sach:
    print(ten)
