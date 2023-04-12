import ast
# ghi
tu_dien_Thu_cung = {1: 'Chim Họa mi', 2: 'Cá ba đuôi',
                    3: 'Rắn', 4: 'Trăn', 5: 'Kỳ nhông', 6: 'Cá Ông tiên'}

tap_tin = open("tu_dien_Thu_cung.txt", "w", encoding="UTF-8")
tap_tin.write(str(tu_dien_Thu_cung))
tap_tin.close()
# đọc
tu_dien_Thu_cung = {}
tap_tin = open("tu_dien_Thu_cung.txt", "r", encoding="UTF-8")
chuoi_doc = tap_tin.read()
tap_tin.close()
tu_dien_Thu_cung = ast.literal_eval(chuoi_doc)
print(tu_dien_Thu_cung)
