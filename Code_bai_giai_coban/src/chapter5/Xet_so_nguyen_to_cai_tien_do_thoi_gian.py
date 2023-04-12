import math
from datetime import datetime
from dateutil import relativedelta

print("CT xét số N có là số nguyên tố ? với N là số nguyên và N>=2") #13194761
n = int(input("N = "))
i = 2
bat_dau = datetime.now()
while i <= math.sqrt(n):
    if n % i == 0:
        break
    i += 1
ket_thuc = datetime.now()    
if i > math.sqrt(n):
    print(n, "là số nguyên tố.")
else:
    print(n, "không là số nguyên tố.")

chenh_lech = relativedelta.relativedelta(ket_thuc,bat_dau).microseconds
print(str(chenh_lech)+" micro seconds.")
