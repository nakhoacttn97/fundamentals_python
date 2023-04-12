i = 1
while i <= 10:
    print("i =", i)
    i += 1
    if i == 5:
        break
else:
    print("Kết thúc trong vòng lặp")
print("Kết thúc sau vòng lặp")

print("\n")
for i in range(1,11):
    print("i =", i)
    if i == 5:
        break
else:
    print("Kết thúc trong vòng lặp")
print("Kết thúc sau vòng lặp")   

# Duyệt từ cao về thấp
for i in range(10, 0, -1):
    print(i)
