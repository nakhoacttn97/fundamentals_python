
numbers = [3, 8, 5, 1, 4, 2, 7, 6, 9, 10]
print("Dãy số:", numbers)

print("\nnumbers[0] =", numbers[0])
print("numbers[2] =", numbers[2])
print("numbers[9] =", numbers[-1])

print("\nCác số từ index 0 đến cận 4:", numbers[0:4])
print("Các số từ index 6 đến hết:", numbers[6:])

print("\nIn 5 số đầu tiên:", numbers[:5])
print("In 5 số cuối cùng:", numbers[-5:])

ages = [23, 25, 22, 24, 23, 26]
print('\nAges:', ages)
s = sum(ages)
print('Tổng:', s)
m = sum(ages)/len(ages)
print('Trung bình:', round(m,2))

ages = [23, 25, 22, 24, 23, 26]
print('\nBefore:', ages)
ages.sort()
ages.reverse()
print('After reverse:', ages)