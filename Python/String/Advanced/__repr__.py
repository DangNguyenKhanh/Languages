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



 
 


 
 
 
