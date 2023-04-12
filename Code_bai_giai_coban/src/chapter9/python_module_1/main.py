import my_lib  # import module my_lib với namespace có tên my_lib
# import các module object f5, f6 của module our_lib vào current namespace
from our_lib import f5, f6
# import tât cả module object của module your_lib vào current namespace
from your_lib import *


def f1():
    print("f1")


def f2():
    print("f2")


def main():
    f1()
    f2()
    my_lib.f3()
    my_lib.f4()
    f5()
    f6()
    my_lib.x = my_lib.x*my_lib.x
    print("x =", my_lib.x)
    print("y =", my_lib.y)


# main()
if __name__ == "__main__":
    main()
