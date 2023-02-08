# Ép kiểu float sang int
x = int(2.5)  # x = 2.5

# Ép kiểu str sang int
x = int("2")      # x = 2
x = int("a2")     # ERROR
x = int("2a")     # ERROR
x = int("2.5")    # ERROR
x = int("2 + 5")  # ERROR

# Ép kiểu int sang float
x = float(2)      # 2.0

# Ép kiểu str sang float
x = float("1.2")  # 1.2

# Ép kiểu int sang str
x = str(5)        # '5'
x = str(3 + 4)    # '7' thực hiện tính toán trước

# str kết hợp divmod()
x = str(3, 4)         # ERROR
x = str((3, 4))       # "(3, 4)"
x = str(divmod(3, 4)) # "(0, 3)"

# Ép kiểu eval() xử lý biểu thức chuỗi
x = eval("12 + 5")
print(x)            # 17
print(type(x))      # <class 'int'>

# Ép kiểu eval() phân biệt biểu thức qua dấu phẩy
x = eval("1+2, 3**2")
print(x)    # (3, 9)

# Nhập nhiều số tự nhiên cách nhau dấu phẩy
m, n, p = eval(input())     # 10, 12, 21



