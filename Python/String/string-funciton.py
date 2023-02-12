# Các hàm bên dưới đây không áp dụng cho tiếng việt


# Viết hoa chuỗi
name = "khanh"
print(name.upper())     # KHANH
print(name)             # khanh   Hàm trả về không tham chiếu lên chuỗi


# In thường chuỗi
s = "ABC"
print(s.lower())        # abc


# Chuyển kí tự đầu chuỗi thành chữ hoa
s = "AB C"
print(s.capitalize())   # Ab c


# Viết hoa chữ cái đầu các từ
s = "dang nguyen khanh"
print(s.title())   # Dang Nguyen Khanh


# Nếu là chữ hoa sẽ thành thường và ngược lại
s = "aBc"
print(s.swapcase())   # AbC


# Xóa khoảng trống thừa đằng trước và đằng sau
s = "    aBc       "
print(s.strip())    # "aBc"


# Xóa khoảng trống đằng trước - left
s = "    aBc       "
print(s.lstrip())   # "aBc       " 


# Xóa khoảng trống đằng sau - right
s = "    aBc       "
print(s.rstrip())   # "    aBc"     


# Lệnh strip cũng xóa luôn kí tự escape
s = "    aBc       \n"
print(s.strip())    # "aBc"


# Lệnh count đếm số lần xuất hiện của ký tự hoặc chuỗi
s = "abc abc abc"
print(s.count('a'))     # 3
print(s.count("abc"))   # 3


# Tham số mở rộng của hàm count(x, [start, end))
s = "abc abc abc"
print(s.count("abc", 3, 6))     # 0
print(s.count("abc", 3, 7))     # 1
print(s[3:6].count("abc"))      # 0
print(s[3:7].count("abc"))      # 1




