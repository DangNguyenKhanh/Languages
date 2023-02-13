# Kiểu dữ liệu từ điển <khóa> : <giá trị>
d = {}    # từ điển rỗng
print(type(d))  # <class 'dict'>


# Cách 2 tạo từ điển rỗng
d = dict()


# In ra từ điển
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
print(d)    # {'1': 'Khanh', '2': 'Hieu', '3': 'Trung'}


# Truy xuất giá trị bằng khóa
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
print(d["1"])       # Khanh
print(d["Khanh"])   # KeyError: 'Khanh'


# Thêm khóa : dữ liệu vào từ điển
d = {}
d["1"] = "Khanh"
d["2"] = "Tony"
d["3"] = "Trung"
print(d)    # {'1': 'Khanh', '2': 'Tony', '3': 'Trung'}


# Gía trị key có thể nhận là
key = số
key = xâu
key = tuple
key không được bằng list


# Giá trị của value có thể nhận là
value = số, xâu, tuple, list
value = từ điển
value = tập hợp


# Xem phương thức của class dict
print(dir(dict))


# Xem tất cả key trong dict
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
for key in d:
    print(key, end=' ') # 1 2 3
    
# Khuyên dùng cho tương tự
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
for key in d.keys():
    print(key, end=' ') # 1 2 3
 

# Xem tất cả value trong dict
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
for value in d.values():
    print(value, end=' ')   # Khanh Hieu Trung 
    
    
# Duyệt cả key lẫn value
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
for key in d.keys():
    print("Mã sinh viên: {:7}, tên: {:10}".format(key, d[key]))
    

# Sắp xếp dict trước khi in bằng hàm sorted()
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
for key in sorted(d.keys()):
    print(key, end=' ') # 2 3 9
    
d = {"1": "Khanh", "2": "Hieu", "3": "Trung"}
for value in sorted(d.values()):
    print(value, end=' ')   # Hieu Khanh Trung


# Hàm items() là cho phép lấy cả key và value
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
for id, name in d.items():
    print(id, name)
# 9 Khanh
# 2 Hieu
# 3 Trung


# Thay đổi value trên từ điển
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
d["9"] = "lol"
print(d)    # {'9': 'lol', '2': 'Hieu', '3': 'Trung'}


# Lệnh update nhận vào một từ điển con đồng bộ từ điển gốc
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
sub_d = {"9": "lol", "3": "hello"}
d.update(sub_d)
print(d)    # {'9': 'lol', '2': 'Hieu', '3': 'hello'}


# Nếu nhập sai khóa sẽ báo lỗi => hàm get() giúp thay vì báo lỗi sẽ trả về None hoặc giá trị muốn nhận
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
print(d.get("10"))  # None
print(d.get("9"))   # Khanh
print(d.get("10", "Chưa có trong cơ sở dữ liệu"))   # Chưa có trong cơ sở dữ liệu


# Xóa khóa 
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
del d["9"]
print(d)    # {'2': 'Hieu', '3': 'Trung'}


# Xóa toàn bộ từ điển
d = {"9": "Khanh", "2": "Hieu", "3": "Trung"}
d.clear()
print(d)    # {}


