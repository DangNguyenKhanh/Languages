# Cấu trúc tuple
a = (1, 2, 3)


# tuple không thể thay đổi được giá trị
a = (1, 2, 3)
a[0] = 10   # ERROR


# Phép cộng tuple
a = (1, 2, 3)
b = (4, 5, 6)
a = a + b
print(a)        # (1, 2, 3, 4, 5, 6)


# Một số method
a = (1, 2, 3, 3)
print(len(a))        # 4
print(a.count(3))    # 2
print(a.index(3))    # 2



