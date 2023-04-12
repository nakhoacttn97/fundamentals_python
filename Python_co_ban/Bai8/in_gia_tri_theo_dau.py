# In ra giá trị theo dấu của một số
# Xây dựng hàm
def so(n):
    if n < 0:
        print('-1')
    elif n > 0:
        print('1')
    else:
        print('0')
    return  so(n)
# Gọi hàm
so(-7)