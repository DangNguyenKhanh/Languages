# Ứng dụng của split để lấy 2 giá trị cùng 1 hàng
s = input()     # 3 10
x, y = s.split()
print(x, y)     # 3 10
print(type(x))  # <class 'str'>
m, n = eval(x), eval(y)
print(type(m))  # <class 'int'>
print(m, n)     # 3 10


