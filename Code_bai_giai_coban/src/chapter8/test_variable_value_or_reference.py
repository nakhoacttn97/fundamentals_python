# test 1
print("test 1")
d = ["Hương", "Thủy", "Bảo", "Hùng"]
# biến tham trị
for t in d:
    t = t.upper()
print(d)
print("\n")
# biến tham chiếu
for i in range(len(d)):
    d[i] = d[i].upper()
print(d)

# test 2
print("\ntest 2")
s1 = "Hello the World."
s2 = s1
print("s1:", s1)
print("s2:", s2)
if(s1 == s2):
    print("s1=s2", id(s1), "-", id(s2))
else:
    print("s1!=s2", id(s1), "-", id(s2))
# test 3
print("\ntest 3")
s1 = "Hello the World."
s2 = "Hello the World."
print("s1:", s1)
print("s2:", s2)
if(s1 == s2):
    print("s1=s2", id(s1), "-", id(s2))
else:
    print("s1!=s2", id(s1), "-", id(s2))
# test 4
print("\ntest 4")
s = "Hello the World."
if(s == "Hello the World."):
    print("bằng", id(s1), "-", id("Hello the World."))
else:
    print("không bằng", id(s1), "-", id("Hello the World."))    
# test 5
print("\ntest 5")
s1 = "Hello the World."
s2 = "HeLLo the World."
print("s1:", s1)
print("s2:", s2)
if(s1.upper() == s2.upper()):
    print("s1=s2", id(s1), "-", id(s2))
else:
    print("s1!=s2", id(s1), "-", id(s2))
