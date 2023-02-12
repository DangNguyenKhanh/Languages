# Thêm thư viện random
from random import random


# Sinh ra số thực từ [0, 1)
print(random())


# Sinh ra số nguyên từ [0, 100]
print(int(101 * random()))


# Sinh ra số nguyên trong đoạn [M, N]
M = 3
N = 5
print(int(M + (N - M + 1) * random()))


# Sinh ra số nguyên trong đoạn [0, N]
N = 5
print(int(N * random()))


# Lấy giá trị ngẫu nhiên trong range() bằng choice()
import random as r
x = r.choice(range(100))
print(x)


# Lấy giá trị ngẫu nhiên trong list cho trước
import random as r
a = [1, 2, 3, 'a', 'b', 'c']
x = r.choice(a)
print(x)


# Lấy giá trị ngẫu nhiên trong xâu cho trước
import random as r
s = "abcdefg"
x = r.choice(s)
print(x)


# Lấy ra giá trị ngẫu nhiên trong đoạn [a, b]
import random as r
print(r.randint(1, 3))


# Lấy ra giá trị ngẫu nhiên trong [start, end) có step 
import random as r
print(r.randrange(0, 10, 2))    # 0 2 4 6 8


