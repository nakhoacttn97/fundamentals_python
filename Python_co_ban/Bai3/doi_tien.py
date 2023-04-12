# Viết chương trình nhập vào số tiền muốn đổi, dổi ra các so-ó tờ mệnh giá và xuất kết quả như sau:
so_tien_muon_doi = int(input('Số tiền muốn đổi:'))
# Thuật toán
so_to_500k = so_tien_muon_doi // 500000
so_to_200k = (so_tien_muon_doi - (so_to_500k * 500000)) // 200000
so_to_100k = (so_tien_muon_doi - ((so_to_500k * 500000) + (so_to_200k * 200000))) // 100000
so_to_50k = (so_tien_muon_doi - ((so_to_500k * 500000) + (so_to_200k * 200000) + (so_to_100k * 100000))) // 50000
so_tien_con_lai = so_tien_muon_doi % (((so_to_500k) * 500000) + ((so_to_200k) * 200000) + ((so_to_100k) * 100000) + ((so_to_50k) * 50000))
# In chương trình ra
print('Số tờ 500,000:', so_to_500k)
print('Số tờ 200,000:', so_to_200k)
print('Số tờ 100,000:', so_to_100k)
print('Số tờ 50,000:', so_to_50k)
print('Số tiền còn lại:', so_tien_con_lai)