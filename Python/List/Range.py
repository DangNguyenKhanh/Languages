# Cấu trúc của hàm range()
range(start=0, stop, step)  


# Ví dụ range()
a = list(range(1, 11, 1))   # chỉ được cài giá trị số
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In ra kiểu range
R = range(10)
print(R)        # range(0, 10)
print(type(R))  # <class 'range'>
for x in R:
    print(x, end=' ')   # 0 1 2 3 4 5 6 7 8 9


# Truy xuất phần tử trong range
R = range(10)
print(R[0])     # 0








    
    
