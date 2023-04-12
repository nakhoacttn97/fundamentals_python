# Gồm các loại tiền: 500000, 200000, 100000, 50000
loai_500k = 500000
loai_200k = 200000
loai_100k = 100000
loai_50k = 50000

print('Các loại tiền: 500,000đ; 200,000đ; 100,000đ; 50,000đ')
tien_muon_doi = int(input("Nhập số tiền muốn đổi: "))

so_to_1 = tien_muon_doi//loai_500k
tien_con_lai = tien_muon_doi % loai_500k

so_to_2 = tien_con_lai//loai_200k
tien_con_lai = tien_con_lai % loai_200k

so_to_3 = tien_con_lai//loai_100k
tien_con_lai = tien_con_lai % loai_100k

so_to_4 = tien_con_lai//loai_50k
tien_con_lai = tien_con_lai % loai_50k

print("Số tờ 500,000đ:", so_to_1)
print("Số tờ 200,000đ:", so_to_2)
print("Số tờ 100,000đ:", so_to_3)
print("Số tờ 50,000đ:", so_to_4)
print("Tiền còn lại:", tien_con_lai)
