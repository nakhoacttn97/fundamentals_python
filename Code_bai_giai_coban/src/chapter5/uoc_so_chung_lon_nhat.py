so_a = int(input("a = "))
so_b = int(input("b = "))
a = so_a
b = so_b
while a != b:
    if a > b:
        a = a-b
    else:
        b = b-a
uscln = a
print("USCLN của %i và %i là %i" % (so_a, so_b, uscln))
bscnn = so_a*so_b/uscln
print("BSCNN của %i và %i là %i" % (so_a, so_b, bscnn))
