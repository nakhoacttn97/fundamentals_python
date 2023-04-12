import math

print("CT nhập ba cạnh a,b,c của một tam giác và tính diện tích theo công thức Heron")
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
if a+b > c and b+c > a and a+c > b:
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    chuoi = "Diện tích tam giác: "+"{:,.2f}".format(s)
    print(chuoi)
else:
    print("Không phải là tam giác!")
