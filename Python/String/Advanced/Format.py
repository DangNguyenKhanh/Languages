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


# Căn trái, giữa, phải
s = "{0:<10} {0:^10} {0:>10}"
print(s.format(123))    # 123           123            123
    
    
# Thêm kí tự
s = "{0:-<10} {0:*^10} {0:->10}"
print(s.format(123))   # 123------- ***123**** -------123


# Chỉ lệnh kiểu (type) dữ liệu muốn in
b: nhị phân
c: ký tự ASCII hoặc Unicode
d: số nguyên
f: số thập phân
e: số thập phân dạng lũy thừa của số e
X: dạng hex
g: số dạng tổng quát
 
s = "{0:b} {0:c} {0:d}"
print(s.format(66))     # 1000010 B 66


# Chỉ lệnh đặt dấu phẩy vào nhóm 3 chữ số
s = "{0:,.5f}"
print(s.format(100022800.234555))   # 100,022,800.23456
print(type(s.format(100022800.234555))) # <class 'str'>


# Chỉ lệnh format()
{chỉ số : <char> <kí tự căn hàng> <#> <width> <,> <.> <p> <type>}


# Sử dụng format(giá trị, kiểu biểu diễn)
print(format(123, 'b')) # 1111011
print(format(123, 'f')) # 123.000000
print(format(123, 'e')) # 1.230000e+02
print(format(123, 'g')) # 123.000000
print(format(123, 'X')) # 7B

print(format(123, '>10'))               # "       123"
print(format(0.123456789, "0<10.3"))    # "0.12300000"
 
print(format(1234567890, "f"))      # 1234567890.000000
print(format(1234567890, ",f"))     # 1,234,567,890.000000
 

# Cấu trúc f-string không cần đợi hàm format()
 ten = "khanh"
diem = 9
sdt = "0904090533"
s = f"ten: {ten:<5} diem: {diem:<5.2f} std: {sdt:<5}"
print(s)    # ten: khanh diem: 9.00  std: 0904090533
