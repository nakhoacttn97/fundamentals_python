def La_so_nguyen_to(n):
    # tra ve 1 neu n la so nguyen to, 
    # tra ve 0 neu n khong la so nguyen 
    tra_ve = 0
    # tim uoc cua n
    uoc = 2
    while uoc<n:
        if n%uoc==0:
            break
        uoc+=1
    # n khong co uoc that su    
    if uoc==n:
        tra_ve=1
    return tra_ve    

n = 17
if La_so_nguyen_to(n)==1:
    print("La so nguyen to")
else:
    print("Khong la so nguyen to")
# in cac so nguyen to trong pham vi tu 2 den 100
danh_sach = []
for n in range(2,100+1):
    if La_so_nguyen_to(n)==1:
        danh_sach.append(n)
print(danh_sach)        