# Khai báo bằng ngoặc đơn
s = 'hello'


# Khai báo bằng ngoặc kép
s = "hello"


# Chuỗi không cho phép thay đổi từng kí tự
s = "abc"
s[0] = 'k'    # ERROR
print(s)  


# Truy xuất phần tử trong chuỗi
s = "abc"
print(s[0])     # a


# Kiểm tra kiểu dữ liệu
s = "abc"
print(type(s))  # <class 'str'>


# Độ dài chuỗi
s = "abc"
print(len(s))   # 3


# Thực hiện nhân số nguyên cho chuỗi
s = "abc"
print(s*3)   # abcabcabc


# Phép cộng giữa 2 chuỗi
s = "abc"
print(s+s)   # abcabc


# Ép kiểu chuỗi
a = 1
b = 1.2
c = [3, 4]
s = str(a) + str(b) + str(c)
print(s)        # 11.2[3, 4]


# Xem các phương thức của class str
print(dir(str))


# 


