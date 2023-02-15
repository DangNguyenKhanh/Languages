# Đọc file excel in ra hết danh sách
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

# print all
print(df.head())    # Khi read ra dù trong excel có chỉnh căn giữa ô thì vô file: đều căn sang phải hết
         Tên sách  Tác giả  Năm xuất bản      # header row sẽ không được đánh thứ tự
0  Python căn bản      NaN        2020.0
1    Java căn bản      NaN        2021.0
2             NaN      NaN           NaN
3     C++ căn bản      NaN        2022.0
4       C căn bản      NaN        2018.0
# Tối đa 5 object sẽ được in
# Hàm head() chỉ dùng để kiểm tra xem có đọc được file chưa 


# In ra header row
print(df.columns)
# Index(['Tên sách', 'Tác giả', 'Năm xuất bản'], dtype='object')


# Đếm số lượng hàng
print(len(df))          # 6, không tính header row chỉ tính trong dataframe
print(len(df.columns))  # 3


# Truy xuất hàng 2 - mỗi 1 hàng được coi là 1 object
import pandas as pd
file_path = r"C:\Users\Admin\OneDrive - hcmut.edu.vn\Desktop\Books.xlsx"
df = pd.read_excel(file_path)
print(df.iloc[0])
# Tên sách        Python căn bản
# Tác giả                    NaN
# Năm xuất bản              2020
# Name: 0, dtype: object
print(df.iloc[0][0])    # iloc - integer location
# Python căn bản
print(df.iloc[0]['Tên sách'])   
# Python căn bản


# 
