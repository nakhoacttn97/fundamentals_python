# Viết chương trình thực hiện việc xử lý trên tuple như sau
tuple_a = (3, 1, 2, 4)
tuple_b = (5, 7, 6, 8)
tuple_c = tuple_a + tuple_b
tuple_d = sorted(tuple_c)
print('Tuple a: ', tuple_a)
print('Tuple b: ', tuple_b)
print('Tuple c: ', tuple_c)
print('Tuple d: ', tuple_d)
print('Tuple[3] = ', tuple_d[3])
print('3 phần tử cuối cùng của tuple d ', tuple_d[-3:])