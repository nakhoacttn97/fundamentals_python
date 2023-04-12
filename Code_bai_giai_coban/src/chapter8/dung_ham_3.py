# khai bao cac ham
# In ten cac nguoi ban
def Lay_Ho_Ten(ho_ten):
    thong_tin = ho_ten.split(" ")
    ho = ""
    for i in range(len(thong_tin)-1):
        ho += thong_tin[i]+" "
    ten = thong_tin[len(thong_tin)-1]    
    return (ho,ten)

def In_danh_sach():
    print("HO".ljust(25," ")+"TEN")
    for ho_ten in danh_sach:
        ho,ten = Lay_Ho_Ten(ho_ten)
        print(ho.ljust(25," ")+ten)

# Them ten nguoi ban moi
def Them_ten(ten_moi):
    danh_sach.append(ten_moi)
    print("Da them thanh cong.")
# Tim kiem ten nguoi ban trong danh sach
def Tim_kiem(ten_tim):
    kq_tim=[]
    for ho_ten in danh_sach:
        ho,ten=Lay_Ho_Ten(ho_ten)
        if ten.upper()==ten_tim.upper():
            kq_tim.append(ho+" "+ten)
    if len(kq_tim)>0:
        print("Tim thay.")
        print(kq_tim)
    else:
        print("Khong tim thay.")

def Hien_thuc_don():
    print("1. In danh sach")       
    print("2. Them ten moi")       
    print("3. Tim kiem theo ten")       
    print("4. Thoat")        

# CT chinh
danh_sach=["Le Thi Ngoc Thao","Lam Van Minh Toan","Nguyen Thi Bao Trang"]
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
