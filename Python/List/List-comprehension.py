# Duyệt list a, tính toán x, thêm vào list b
a = [1, 2, 3, 4, 5]
b = [x * x for x in a]
print(b)        # [1, 4, 9, 16, 25]


# Tạo nhanh generator
R = (i * i for i in range(10))
print(type(R))              # <class 'generator'>
print(R)                    # <generator object <genexpr> at 0x000002AF837500B0> - Chưa được kích hoạt đợi đợt duyệt 
for x in R:                 # Kích hoạt
    print(x, end=' ')       # 0 1 4 9 16 25 36 49 64 81
    
    
# Kiểu dữ liệu generator như đầu đọc, đọc qua sẽ bỏ dữ liệu
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
