# hàm map
# cú pháp: r = map(func, seq)
# r có kiểu iterator, dùng hàm list để đổi sang kiểu list


def fahrenheit(T):
    return ((float(9)/5)*T + 32)


def celsius(T):
    return (float(5)/9)*(T-32)


temp = [36.5, 37, 37.5, 39]
# sử dụng hàm tự định nghĩa
F = map(fahrenheit, temp)
F_copy = list(F)

C = map(celsius, F_copy)
C_copy = list(C)

print("F:", F_copy)
print("C:", C_copy)
# sử dụng biểu thức lambda
F = map(lambda x: (float(9)/5)*x + 32, temp)
F_copy = list(F)
print("F:", F_copy)
