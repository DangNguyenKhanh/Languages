# Số phức trong thư viện math
z = 3 + 2j
print(z)        # (3+2j)
print(type(z))  # <class 'complex'>
print(abs(z))   # 3.605551275463989


# Số phức liên hợp - thêm dấu trừ phần ảo
z = 3 + 2j
z = z.conjugate()
print(z)        # (3-2j)
print(type(z))  # <class 'complex'>
print(abs(z))   # 3.605551275463989
print(z.real)   # 3.0
print(z.imag)   # -2.0
