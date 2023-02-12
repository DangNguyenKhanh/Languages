# Hàm kiểm tra có phải năm nhuận không trả về bool
def leap_year(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 == 0):
        return True
    else:
        return False

print(leap_year(2023))  # False
print(leap_year(2000))  # True


  
