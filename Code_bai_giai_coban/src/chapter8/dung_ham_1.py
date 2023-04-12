# khai bao cac ham
# In ten cac nguoi ban
def In_danh_sach():
    for ten in danh_sach:
        print(ten)
# Them ten nguoi ban moi
def Them_ten(ten_moi):
    danh_sach.append(ten_moi)
    print("Da them thanh cong.")
# Tim kiem ten nguoi ban trong danh sach
def Tim_kiem(ten_tim):
    if ten_tim in danh_sach:
        print("Tim thay.")
    else:
        print("Khong tim thay.")
def Hien_thuc_don():
    print("1. In danh sach")       
    print("2. Them ten moi")       
    print("3. Tim kiem theo ten")       
    print("4. Thoat")        

# CT chinh
danh_sach=["Ngoc Thao","Minh Toan","Bao Trang"]
while True:
    Hien_thuc_don()
    chon = int(input("Moi ban chon: "))
    if chon==1:
        In_danh_sach()
    elif chon==2:
        ten_moi = input("Ten nguoi ban moi: ")
        Them_ten(ten_moi)
        In_danh_sach()
    elif chon==3:
        ten_tim = input("Ten nguoi ban muon tim: ")
        Tim_kiem(ten_tim)
    elif chon==4:
        break;
