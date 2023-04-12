# Tính diên tích tam giác
# Gọi S là diện tich tam giác và a, b, c lần lượt là 3 cạnh của tam giác:
import math
a = float(input('Cạnh a:'))
b = float(input('Cạnh b:'))
c = float(input('Cạnh c:'))

# p là nửa chu vi của tam giác
p = (a + b + c)/2
# s là diện tích của tam giác
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Diện tích tam giác: ', float(s))