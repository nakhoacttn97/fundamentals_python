"""
try:
    f = open("bai_tho.txt","r",encoding="utf-8")
    noi_dung = f.read()
    print(noi_dung)
    f.close()
except FileNotFoundError:
    print("Tap tin khong ton tai.")
"""

def Doc_tap_tin(ten_tap_tin):
    try:
        f = open(ten_tap_tin,"r",encoding="utf-8")
        noi_dung = f.read()
        f.close()
        return noi_dung
    except FileNotFoundError:
        print("Tap tin khong ton tai.")    

ten_tap_tin = "bai_tho.txt"
noi_dung = Doc_tap_tin(ten_tap_tin)    
if(noi_dung!=None):
    print(noi_dung)
