#int
print(1 + 1)                # 2
print(type(1 + 1))          # <class 'int'>

# float
print(1.1 + 1.1)            # 2.2
print(type(1.1 + 1.1))      # <class 'float'>

# string
print('1' + '1')            # 11
print(type('1' + '1'))      # <class 'str'>

# string + int
print('1' + str(1))         # 11 
print(type('1' + str(1)))   # <class 'str'>

# int + string
print(1 + int('1'))         # 2
print(type(1 + int('1')))   # <class 'int'>


# calculate sum
x = 3
y = 10
print('x + y =', x + y)


# Special quotes
print('This is double quotes ""')   # This is double quotes ""
print("This is single quotes ''")   # This is single quotes ''


# Escape sequence
print('\\')     # \
print('\'')     # '
print('\"')     # "
print('\n')     # breakline
print('\t')     # tab


# in cùng 1 dòng
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4


# In nhiều giá trị 1 lúc
print(1, 2, "Đặng Nguyên Khánh")


# Sử dụng biến sep và end - sep và end là tham số lựa chọn
print("Đặng", "Nguyên", sep="|", end="---")
print("Khánh")          # Đặng|Nguyên---Khánh


# Phải đặt tham số thực sự trước tham số mặc định
def foo(a, b=1, c=2):
    # do something




