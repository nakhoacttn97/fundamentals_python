# Tạo list
numbers = []

# Nhập các phần tử số cho list
while True:
    number = input("Nhập vào một số (hoặc nhập 'stop' để dừng): ")
    if number == 'stop':
        break
    numbers.append(int(number))

# Nhập vào một số x
x = int(input("Nhập vào một số x: "))

# Tính tổng các phần tử trong list
total = sum(numbers)
print("Tổng các phần tử trong list là:", total)

# Kiểm tra x xuất hiện trong list hay không
count = numbers.count(x)
if count > 0:
    print(f"{x} xuất hiện {count} lần trong list")
else:
    print(f"{x} không xuất hiện trong list")

# Kiểm tra x lớn hơn tất cả các số trong list hay không
if all(x > num for num in numbers):
    print(f"{x} lớn hơn tất cả các số trong list")
else:
    print(f"{x} không lớn hơn tất cả các số trong list")
    # In ra tất cả các số trong list lớn hơn x
    greater_numbers = [num for num in numbers if num > x]
    if greater_numbers:
        print("Những số trong list lớn hơn x là:", greater_numbers)
    else:
        print("Không có số nào trong list lớn hơn x")