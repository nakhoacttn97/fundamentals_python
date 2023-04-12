# Xây dựng chương trình Count down

count_down = eval(input('Input number:\n'))

while count_down <= 11:
    print(count_down)
    count_down -= 1
    if count_down < 0:
        break
print('Start!!!')