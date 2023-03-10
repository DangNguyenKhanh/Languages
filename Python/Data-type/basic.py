# int 
x = 10
print(x)


# float
x = 10.0
print(x)


# string
x = '10'
print(x)


# xâu ký tự không cho thay đổi phần tử
s = "abc"
s[0] = 'k'
print(s)    # TypeError: 'str' object does not support item assignment


# bool
x = 3 > 2
print(x)                # True
print(3 < 2)            # False
print(bool(3 < 2))      # False
print(bool(0))          # False
print(bool(4))          # True
print(bool([]))         # False
print(bool("Dang")) # True
print(bool((1, 2, 3)))  # True
print(bool(12 and [1, 2]))  # True
print(bool(33 and ""))      # False

print(0 in [0, 1, 2])   # True
print(0 in range(10))   # True

print(bool(print("Hi"))) # False, hàm print trả về None

Giá trị False:
- Là các số = 0
- Trả về None
- list, tuple rỗng
- xâu ký tự rỗng
- hàm void
- hàm trả về 0


# Biến trong python có thể thay đổi kiểu dữ liệu một cách tự động
x = 100
x = 'Hello'
print(x)        # Hello
print(type(x))  # <class 'str'>


# Hàm trả về kiểu dữ liệu
print(type(123))    # <class 'int'>
print(type(2.4))    # <class 'float'> 
print(type('a'))    # <class 'str'>
print(type("HCM"))  # <class 'str'>
print(type(3 > 2))  # <class 'bool'>


# Số lớn
12e50 = 12.10^50
1.56e-2 = 1,56.10^-2




