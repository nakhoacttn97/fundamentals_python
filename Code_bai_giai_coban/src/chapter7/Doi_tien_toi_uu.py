cac_loai_tien = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000, 500]
print('Các loại tiền:', cac_loai_tien)
tien_muon_doi = int(input("Nhập số tiền muốn đổi: "))
so_tien = tien_muon_doi
i = 0
while i < len(cac_loai_tien):
    so_to = so_tien//cac_loai_tien[i]
    if so_to > 0:
        print("Số tờ", "{:,}".format(cac_loai_tien[i]), "là:", so_to)
    so_tien = so_tien % cac_loai_tien[i]
    i += 1
if so_tien>0:
    print('Tiền 1 đồng:', so_tien)