# Hàm __repr__() trả về xấu ký tự
a = [1, 2, 3, 4]
x = a.__repr__()
print(type(x))  # <class 'str'>
print(x)        # [1, 2, 3, 4]

s = "Tony"
x = s.__repr__()
print(type(x))  # <class 'str'>
print(x)        # 'Tony'

s = 'Tony'
x = s.__repr__()
print(type(x))  # <class 'str'>
print(x)        # 'Tony'

b = 2 > 1
x = b.__repr__()
print(type(x))  # <class 'str'>
print(x)        # True

s = 12.5**34
x = s.__repr__()
print(type(x))  # <class 'str'>
print(x)        # 1.9721522630525294e+37


# Hàm format điền vào {}:field trong chuỗi - placeholder - hộp giữ chỗ không chỉ số
s = "Xin chào {} và {}"
x = s.format("Tony", "Khanh")
print(type(x))  # <class 'str'>
print(x)        # Xin chào Tony và Khanh


# Có thể thay thế cho bất kỳ dữ liệu. 
print("Đây là {} và {}".format(1, 2))   # Đây là 1 và 2
print("Đây là {} và {}".format([1, 2, 3], 5.3))   # Đây là [1, 2, 3] và 5.3


# Hộp giữ chỗ có chỉ số
s = "Đây là {0} và {1}. Ta có {1} và {0}".format('a', 'b')  # Khi dùng chỉ số thì không được để trống {}
print(s)    # Đây là a và b. Ta có b và a


# Tham số của placeholder {chỉ số : độ rộng}  - Số căn phải, chữ căn trái
s = "hello{:5}và{:5}".format(1, 2)
print(s)    # hello    1và    2









