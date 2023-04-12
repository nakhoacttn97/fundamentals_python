print("CT in bảng cửu chương")
n = int(input("Bạn muốn in cửu chương ? (2-9): "))
if not(2 <= n and n <= 9):
    print("Chỉ in cửu chương từ 2 đến 9.")
    exit()
# In bảng cửu chương n
i = 1
while i <= 10:
    print(str(n)+" x "+str(i).rjust(2, " ")+" = "+str(n*i).rjust(2, " "))
    i += 1
