# Sử dụng append() để giữ nguyên đối tượng tuple và range
a = [1, 2, 3]
b = (4, 5, 6)       # tuple
c = range(7, 9)     # range
a.append(b)
print(a)            # [1, 2, 3, (4, 5, 6)]
a.append(c)
print(a)            # [1, 2, 3, (4, 5, 6), range(7, 9)]


# Sử dụng extend() để phá đối tượng tuple và range
a = [1, 2, 3]
b = (4, 5, 6)       # tuple
c = range(7, 9)     # range
a.extend(b)
print(a)            # [1, 2, 3, 4, 5, 6]
a.extend(c)
print(a)            # [1, 2, 3, 4, 5, 6, 7, 8]
