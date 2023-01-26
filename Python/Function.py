# Tên hàm không được viết hoa, phải dùng dấu gạch dưới _
def get_sum(a, b):
    return a + b
# Bỏ dòng này
# Bỏ dòng này
print(get_sum(1, 2))


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


