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


# Hàm find() trả về index, thất bại trả về false
s = "abc cba abc"
print(s.find("cba"))    # 4
print(s.find("bbb"))    # -1


# Hàm index() cũng trả về index, thất bại lại báo lỗi
s = "abc cba abc"
print(s.index("cba"))    # 4
print(s.index("bbb"))    # ValueError: substring not found


# Hàm find() và index() đều có tham số [start, end]
s = "cba abc abc"
print(s.index("cba", 0, 3))    # 0
print(s.index("bbb", 0, 3))    # ValueError: substring not found


# Hàm replace() thay thế chuỗi con 
s = "cba abc abc"
print(s.replace("cba", "oke"))  # oke abc abc


# Tham số mở rộng của hàm replace(old, new, count=-1)
s = "cba abc abc"
print(s.replace('a', 'A', 2))  # cbA Abc abc    2 lần thay thế


# Hàm tách split()
s = "   cba abc abc   \n"
print(s.split())    # ['cba', 'abc', 'abc']


# Tham số trong split(sep=none, maxsplit=-1)
s = "   cba abc abc   \n"
print(s.split())                        # ['cba', 'abc', 'abc']
print(s.split(sep=' ', maxsplit=3))     # ['', '', '', 'cba abc abc   \n']
print(s.split(sep=' ', maxsplit=4))     # ['', '', '', 'cba', 'abc abc   \n']


# Hàm join nối phần tử của list
s = "   cba abc abc   \n"
a = s.split()
print(a)            # ['cba', 'abc', 'abc']
print("".join(a))   # cbaabcabc
print("*".join(a))  # cba*abc*abc
print(" ".join(a))  # cba abc abc



