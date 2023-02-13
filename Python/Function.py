# Tên hàm không được viết hoa, phải dùng dấu gạch dưới _
def get_sum(a, b):          # actual parameters - tham số thực sự
    return a + b
print(get_sum(1, 2))        # 3


# Default parameters - Tham số mặc định
def xep_loai(diem, diem_chuan = 5.0):
    if diem >= diem_chuan:
        return "Tot nghiep"
    else:
        return "Chua tot nghiep"
print(xep_loai(4))          # Chua tot nghiep
print(xep_loai(4.5, 4))     # Tot nghiep


# Return trả về nhiều giá trị trong (v1, v2, v3, ...)
def Rectangle(dai, rong):
    CV = (dai + rong) * 2
    DT = dai * rong
    return CV, DT
print(Rectangle(3, 4))      # (14, 12)
CV, DT = Rectangle(3, 4)
print(CV)                   # 14
print(DT)                   # 12


# Tham số không có tính tham chiếu
def foo(x):
    x = 10
x = 5
foo(x)
print(x)    # 5


# Tìm biến bên ngoài nếu biến trong hàm không có
x = 10
def foo():
    print(x + 2)

foo()       # 12
print(x)    # 10


# Quy định vị trí tham số truyền
def foo(a, b):
    return a - b
print(foo(3, 4))        # -1
print(foo(4, 3))        # 1
print(foo(b=4, a=3))    # -1


# Tham số mặc định (a) phải đứng trước tham số không mặc định (b=1, c=2)
def foo(a, b=1, c=2):
    print(a)


# Hàm định nghĩa trực tiếp  (Không nên dùng)
s = lambda a, b: a + b
print(s(10, 2))     # 12


# Đổi tên cho hàm
print(print)    # <built-in function print>
cout = print
cout("Hello world!")    # Hello world!



