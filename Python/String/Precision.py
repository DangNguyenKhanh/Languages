# Chọn 2 chữ số sau dấu phâỷ, làm tròn lên
import math
s = "{:.3}"     # width = 0, p = 3
print(s.format(math.pi))    # 3.14      nếu >= 1 thì tổng chữ số trước và sau dấu phẩy
print(s.format(1.9999))     # 2.0       làm tròn lên
print(s.format(1.8888))     # 1.89      làm tròn lên
print(s.format(0.33333))    # 0.333     nếu < 1 thì tổng chữ số sau dấu phẩy
print(s.format("hello"))    # hel


# Chỉ lệnh # hash giúp điền số 0 bên phải cho đủ chiều dài
s = "{:#6.3}"   # Độ rộng 6 tính luôn dấu chấm, lấy 3 chữ số nếu < 1 và lấy 4 chữ số nếu > 1
print(s.format(0.1))    # " 0.100"
print(s.format(1.0))    # "  1.00"


# Cú pháp hoàn chỉnh
{chỉ số : char <=> # width.p}
 
