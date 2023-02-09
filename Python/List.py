# many type list
a = [1, 2.2, "Hello", [1, 2, "True"]]


# type
a = [1, 2, 3, 4, 5]
print(type(a))  # <class 'list'>


# empty list
a = []
print(a)    # []


# int List
a = [1, 2, 3, 4, 5]
# index(+):  0  1  2  3  4
# index(-): -5 -4 -3 -2 -1
# value   :  1  2  3  4  5
print(a)        # [1, 2, 3, 4, 5]
print(a[0])     # 1
print(a[-5])    # 1


# Modify element
a[0] = 10
print(a[0])     # 10
print(a)        # [10, 2, 3, 4, 5]


# Cộng 2 list
a = [10, 2, 3, 4, 5]
b = [1, 2, 3]
c = a + b
print(c)    # [10, 2, 3, 4, 5, 1, 2, 3]


# Nhân 2 list
a = [1, 2, 3]
b = 2 * a
print(b)    # [1, 2, 3, 1, 2, 3]


# length of list (number of elements)
print(len(a))   # 5
print(len([1, 2] + [3, 4]))     # 4


# Check exist or not exist element
print(a)            # [10, 2, 3, 4, 5]
print(10 in a)      # True
print(9 in a)       # False
print(9 not in a)   # True


# Insert tail in list
print(a)            # [10, 2, 3, 4, 5]
a.append(1)
print(a)            # [10, 2, 3, 4, 5, 1]


# insert any-where
print(a)            # [10, 2, 3, 4, 5, 1]
a.insert(0, 9)
print(a)            # [9, 10, 2, 3, 4, 5, 1]
a.insert(len(a), -1)
print(a)            # [9, 10, 2, 3, 4, 5, 1, -1]
a.insert(100, -2)
print(a)            # [9, 10, 2, 3, 4, 5, 1, -1, -2]


# Delete tail
a = [1, 2, 3, 4, 5]
print(a.pop())      # 5
print(a)            # [1, 2, 3, 4]


# Xóa 1 phần tử a[i]
a = [1, 2, 3, 4, 5]
del a[1]
print(a)            # [1, 3, 4, 5]


# Delete first element while found and stop
a = [1, 2, 2, 4, 5]
print(a.remove(2))      # none
print(a)                # [1, 2, 4, 5]


# Counting a number of appearing of element
a = [1, 2, 2, 2, 5]
print(a.count(2))       # 3


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
