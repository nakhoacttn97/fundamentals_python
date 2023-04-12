def f1():
    print("f1")

def f3():
    f2()
    print("f3")

def f2():
    f1()
    print("f2")

f3()    
