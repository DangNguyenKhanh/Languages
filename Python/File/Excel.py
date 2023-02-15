# Đọc file excel in ra dòng đầu
  # Bật terminal trong PyCharm
  # Cài đặt: >pip install openpyxl
  # Update pip: python.exe -m pip install --upgrade pip
  # Setting pandas: >pip install pandas
  # Kiểm tra list pip: >pip list
  # Lưu ý phải đóng file mới chạy được chương trình: Nếu không là lỗi PermissionDenied
import pandas as pd

# raw string cho phép có kí tự escape '\'
# tạo biến file_path giúp thay đổi dễ dàng hơn thay vì update tất cả
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"

# data-frame = 2-dimensional labeled
df = pd.read_excel(file_path)

# print first row
print(df.head())    # Khi read ra dù trong excel có chỉnh căn giữa ô thì vô file: đều căn sang phải hết


# 
