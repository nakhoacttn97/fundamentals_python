print("CT nhập ba cạnh a,b,c và xét có là một tam giác?")
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
if a+b > c and b+c > a and a+c > b:
    print("Đây là một tam giác ABC.")
else:
    print("Không phải là tam giác!")
