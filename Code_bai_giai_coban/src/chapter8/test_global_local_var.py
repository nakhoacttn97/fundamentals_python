"""
# test 1
def f1():
    a = 10
    print("\t","in f1(), local --> a =", a)


a = 1
print("global --> a =", a)
f1()
print("global --> a =", a)
exit()
"""
# test 2
def f2():
    global a
    a = 10
    print("\t","in f2(), global --> a =", a)

a = 1
print("global --> a =", a)
f2()
print("global --> a =", a)
a += 1
f2()
print("global --> a =", a)
