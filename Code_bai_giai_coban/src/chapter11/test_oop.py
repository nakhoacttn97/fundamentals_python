"""
a = 23
b = 34
tong = a + b;
print("Tong: ", tong)
hieu = a - b;
print("Hieu: ", hieu)
"""
"""
def Tinh_tong(a,b):
    return a + b

def Tinh_hieu(a,b):
    return a - b

a = 23
b = 34
tong = Tinh_tong(a,b)
print("Tong: ", tong)
hieu = Tinh_hieu(a,b)
print("Hieu: ", hieu)    
"""
class Tinh_toan:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def Tinh_tong(self):
        return self.a + self.b

    def Tinh_hieu(self):
        return self.a - self.b 

t1 = Tinh_toan(23,45) # object t1 cua class Tinh_toan
tong = t1.Tinh_tong()
print("Tong: ", tong)
hieu = t1.Tinh_hieu()
print("Hieu: ", hieu)    

t2 = Tinh_toan(34,25) # object t2 cua class Tinh_toan
tong = t2.Tinh_tong()
print("Tong: ", tong)
hieu = t2.Tinh_hieu()
print("Hieu: ", hieu)    
