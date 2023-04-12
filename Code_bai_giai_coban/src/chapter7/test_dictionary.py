
Tu_dien_Thu_cung = {1: 'Chim Họa mi', 2: 'Cá ba đuôi',
                    3: 'Rắn', 4: 'Trăn', 5: 'Kỳ nhông', 6: 'Cá Ông tiên'}
for i in Tu_dien_Thu_cung:
    print('key',i, ':', Tu_dien_Thu_cung[i])

Ban_sao = Tu_dien_Thu_cung.copy()
print("\nBản sao:")
for i in Ban_sao:
    Ban_sao[i] = Ban_sao[i].upper()
    print(i, ':', Ban_sao[i])

print("\nBản gốc:")
for i in Tu_dien_Thu_cung:
    print(i, ':', Tu_dien_Thu_cung[i])

