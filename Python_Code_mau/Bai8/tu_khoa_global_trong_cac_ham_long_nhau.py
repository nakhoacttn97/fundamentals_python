# Từ khóa global trong các hàm lồng nhau (nested function)
def ham_1():
    x = 20
    def ham_2():
        global x
        x = 25
    print('x trước khi gọi ham_2:', x)

    # Gọi hàm 2
    ham_2()
    print('x sau khi gọi ham_2:', x)
# Gọi hàm ham_1
ham_1()
print('x từ chương trình chính:', x)

