# Đọc dữ liệu từ tập tin heights_1.txt vào list height
f = open('heights_1.txt', 'r')
chuoi = f.read()
f.close()
# print(chuoi)
height = eval(chuoi)
print(len(height))  # 1015
# arr_height_m = arr_height * 0.0254
height_m = [h*0.0254 for h in height]
print('10 chiều cao đầu tiên:', [round(h, 2) for h in height_m[0:10]])
# tính chiều cao trung bình
tong = sum(height_m)
n = len(height_m)
trung_binh = tong/n
print('Chiều cao trung bình:', round(trung_binh, 2))
lon_nhat, nho_nhat = max(height_m), min(height_m)
print('Chiều cao lớn nhất:', round(lon_nhat, 2))
print('Chiều cao nhỏ nhất:', round(nho_nhat, 2))
# sắp giảm chiều cao
height_m_top10 = list(set(height_m))
height_m_top10.sort()
height_m_top10 = height_m_top10[::-1]
print('Top 10 chiều cao:', [round(h, 2) for h in height_m_top10[0:10]])
