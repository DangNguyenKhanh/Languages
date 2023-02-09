# Sự tham chiếu 2 danh sách
a = [1, 2, 3]
b = a
b[0] = 10
print(a)    # [10, 2, 3]


# Khắc phục sự tham chiếu
a = [1, 2, 3]
b = a.copy()
b[0] = 10
print(a)    # [1, 2, 3]
print(b)    # [10, 2, 3]

