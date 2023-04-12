# ghi
tu_dien_Thu_cung = {1: 'Chim Họa mi', 2: 'Cá ba đuôi',
                    3: 'Rắn', 4: 'Trăn', 5: 'Kỳ nhông', 6: 'Cá Ông tiên'}

tap_tin = open("tu_dien_Thu_cung.txt", "w", encoding="UTF-8")
for thu_tu in tu_dien_Thu_cung:
    tap_tin.write(str(thu_tu)+":"+tu_dien_Thu_cung[thu_tu]+"\n")
tap_tin.close()
# đọc
tu_dien_Thu_cung = {}
tap_tin = open("tu_dien_Thu_cung.txt", "r", encoding="UTF-8")
for dong in tap_tin:
    dong = dong.replace("\n", "")
    chuoi_tach = dong.split(":")
    key = int(chuoi_tach[0])
    value = chuoi_tach[1]
    tu_dien_Thu_cung[key] = value
tap_tin.close()
print(tu_dien_Thu_cung)
