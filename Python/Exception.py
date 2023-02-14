# Thay thông báo lỗi mặc định thành thông báo của mình
try:
    print(int('abc'))
except ValueError:
    print("Không được ép kiểu int cho str")
    
try:
    [][2] = 5
except IndexError:
    print("Lỗi về index")
    
try:
    print(9 / 0)
except ZeroDivisionError:
    print("Lỗi chia cho 0")
    
    
# Kết hợp cách 1
try:
    print(int('abc'))
except ValueError:
    print("Không được ép kiểu int cho str")
except IndexError:
    print("Lỗi về index")
except ZeroDivisionError:
    print("Lỗi chia cho 0")
except Exception:
    print("Lỗi khác")
    
    
# Kết hợp cách 2
try:
  ...
except(ValueError, IndexError, ZeroDivisionError):
  ...
except Exception:
  ...
  
  
# Chỉ ra đối tượng lỗi
try:
    print(int('abc'))
except ValueError as err:
    print("Không được ép kiểu int cho str", err)
    
 
# Lệnh pass bỏ qua exception
while True:
    try:
        x = int(input())    # Nhập số nguyên
        break
    except ValueError as err:
        pass
print(x)


# Cú pháp ngoại lệ đầy đủ
def divide(x , y):
    try:
        res = x / y
    except ZeroDivisionError:
        print("y phải khác 0!...")
    else:
        print(res)
    finally:
        print("Done...")

divide(10, 0)


# Lệnh tạo lỗi
def nhap():
    n = int(input())
    if n <= 0 or n > 100:
        raise ValueError(n)
    return n

while True:
    try:
        x = nhap()
    except ValueError:
        print("Nhap lai")
    else:
        print("Ban da nhap", x)
        break
        
     
# Định nghĩa lỗi
class abc_error(Exception):
    def __init__(self, msg):
        self.msg = msg


# Nhận về đối tượng lỗi
class abc_error(Exception):
    def __init__(self, msg):
        self.msg = msg

def nhap():
    n = int(input())
    if n <= 0 or n > 100:
        raise abc_error("nằm từ 1 - 100")
    return n

while True:
    try:
        x = nhap()
    except ValueError as err:
        print("Nhap lai", err)
    except abc_error as err:
        print(err)
    else:
        print("Ban da nhap", x)
        break
        

# Mô hình cây đối tượng Exception
BaseException -> Exception -> lỗi thường gặp




