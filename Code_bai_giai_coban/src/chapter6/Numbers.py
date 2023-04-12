Tuoi = 37
So_tien = 1234.56

print("Tuổi:", Tuoi)
print("Số tiền:", So_tien)

Tuoi = int("37")
So_tien = float("1345234.56789")

print("\nTuổi:", Tuoi)
print("Số tiền:", So_tien)

So_tien = 1345234.56789
print("\nSố tiền: {:,.2f}".format(So_tien))

So_tien = 1345234
print("\nSố tiền:","{:,}".format(So_tien))
a = 12
b = 12
if a == b:
    print("bằng")
else:
    print("không bằng")
a = 12
b = 13
if a is b:
    print("bằng")
else:
    print("không bằng")
