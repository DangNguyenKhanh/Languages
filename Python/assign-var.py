# Gán nhiều biến cùng giá trị
x = y = z = 2


# Gán nhiều biến khác giá trị
x, y, z = 1, 2, 3

# Sinh ra lỗi 
x = 1, y = 2, z = 3   # ERROR: can't assign to literal


# Hoán đổi giá trị x và y cho nhau
x, y = 10, 3
temp = x
x = y
y = temp
print(x, y)     # 3 10

# Hoán đổi cách 2
x, y = 10, 3
x, y = y, x
print(x, y)     # 3 10


# Gán thay đổi
x = 10
x += 1    # x = x + 1
print(x)  # 11 

x = 10
x -= 1    # x = x - 1
print(x)  # 9


# Tính toán liên tục trên nhiều dòng
x = 1 + 2 + 3 \
    + 4
print(x)    # 10





