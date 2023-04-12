
# đọc tập tin heights.txt (inch)
f = open('heights.txt')
data = f.read() # biến data kiểu chuỗi
f.close()

print("data:", data)

# đổi sang list, phần tử kiểu chuỗi
lst = data.split(",")

print(lst)

# list, phần tử kiểu số thực
height = [float(item) for item in lst]
print(height)

# đổi inch sang mét
height_m = [h*0.0254 for h in height]

print(height_m[:10])

# tính chiều cao trung bình
mean = sum(height_m)/len(height_m)
print('Chiều cao trung bình:', round(mean,2))

