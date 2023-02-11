# Cấu trúc của hàm range()
range(start=0, stop, step)  


# Ví dụ range()
a = list(range(1, 11, 1))   # chỉ được cài giá trị số
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In ra kiểu range
R = range(10)
print(R)        # range(0, 10)
for x in R:
    print(x, end=' ')   # 0 1 2 3 4 5 6 7 8 9 


# Truy xuất phần tử trong range
R = range(10)
print(R[0])     # 0


# Tạo nhanh generator
R = (i * i for i in range(10))
print(type(R))              # <class 'generator'>
print(R)                    # <generator object <genexpr> at 0x000002AF837500B0> - Chưa được kích hoạt đợi đợt duyệt 
for x in R:                 # Kích hoạt
    print(x, end=' ')       # 0 1 4 9 16 25 36 49 64 81
    
    
# Kiểu dữ liệu generator chỉ tạo 1 lần xong biến mất
R = (i*i for i in range(10))
print(type(R))              # <class 'generator'>
for x in R:                 # Kích hoạt
    print(x, end=' ')       # 0 1 4 9 16 25 36 49 64 81
for x in R:                 # Không còn
    print(x, end=' ')       # 

    
# yield giúp tạo ra một dữ liệu mỗi lần lặp trong hàm
def even_num(n):          # generator function
    for i in range(n):
        if 2 * i > n:
            return
        yield 2 * i       # Gửi xuống 2 * 0 = 0 xuống

n = 10
for x in even_num(n):     # x in 0 in ra 0 xong quay lên hàm gọi lại
    print(x, end=' ')     # 0 2 4 6 8 10


# Dữ liệu generator như đầu đọc, đọc qua sẽ xóa dữ liệu đó
def even_num(n):
    for i in range(n):
        if 2 * i > n:
            return
        yield 2 * i

n = 10
G = even_num(n)             # Đợi hiệu lệnh
for x in G:                 # Lần sinh đầu tiên
    print(x, end=' ')       # 0 2 4 6
    if x > 5:
        break
print()
for x in G:                 # Lần sinh thứ hai, sinh nốt
    print(x, end=' ')       # 8 10
print()
for x in G:                 # Lần sinh thứ ba, hết dữ liệu sinh đọc đầu generator đã ở cuối bộ đọc
    print(x, end=' ')       # 





    
    
