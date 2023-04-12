
from libs import my_lib as mylib

# sử dụng package libs/sublibs và module your_lib

import libs.sublibs.your_lib 
# from libs.sublibs import your_lib

def f1():
    print("f1")


def f2():
    print("f2")


def main():
    f1()
    f2()
    mylib.f3()
    mylib.f4()
    # your_lib.f5()
    libs.sublibs.your_lib.f5()        
# main()
main()
