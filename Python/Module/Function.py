# Xem hàm của hệ thống
print(dir())                # __builtins__
print(dir(__builtins__))    # Hàm của hệ thống
print(dir(math))            # Hàm của thư viện math
print(dir(class_name))      # Cấu trúc xem hàm của một class


# Một số hàm
a = [1, 2, 3, 4, 5]
print(min(a))       # 1
print(max(a))       # 5
print(sum(a))       # 15
print(abs(1 + 1j))  # 1.4142135623730951 số phức 1 + i


# Hàm round()
print(round(3.4))           # 3
print(round(3.5))           # 4
print(round(3.6))           # 4
print(round(3.617, 2))      # 3.62
print(round(3.1416, 2))     # 3.14


