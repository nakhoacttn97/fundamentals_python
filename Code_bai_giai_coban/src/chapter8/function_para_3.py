# Khai báo hàm
def Dat_xe(noi_di, noi_den="Sài gòn", so_cho=4):
    return "Bạn đã đặt xe %i chổ đi từ %s đến %s" % (so_cho, noi_di, noi_den)


# CT chính
print(Dat_xe("Sài gòn", "Cần thơ", 7))
print(Dat_xe(noi_di="Nha trang"))
