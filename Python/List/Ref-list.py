# sự tham chiếu của list
a = [1, 2]
b = a
a[0] = 10
print(a)        # [10, 2]
print(b)        # [10, 2]
print(a is b)   # True


# sự tham chiếu của list khi truyền tham số cho hàm
def foo(x):
    x[0] = 10
a = [1, 2]
foo(a)
print(a)    # [10, 2]


# Dấu += dẫn đến tham chiếu
def foo(x):
    x += x
a = [1, 2]
foo(a)
print(a)    # [1, 2, 1, 2]


# Nếu không thay dổi phần tử sẽ không ảnh hưởng gì hết
def foo(x):
    x = x + x       # phép cộng x + x không dẫn đến tham chiếu chỉ tạo mới, x = là biến x mới được tạo chỉ tồn tại trong hàm
a = [1, 2]
foo(a)
print(a)    # [1, 2]


