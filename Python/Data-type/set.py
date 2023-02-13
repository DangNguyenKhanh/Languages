# Tập hợp
- Chứa: số, logic, xâu, tuple (không thay đổi - immutability)
- Không chứa: list, dict, set (thay đổi được - mutability)
  
  
# Khởi tạo tập hợp
my_set = {1, 2, 3, "one"}
print(type(my_set)) # <class 'set'>


# Tập hợp không cho phép các phần tử trùng nhau
my_set = {1, 1, "one", "one"}
print(my_set)   # {1, 'one'}


# Tập hợp đóng băng - advanced
my_set = frozenset()


# Cách lọc list không có phần tử trùng: list -> set -> list
a = [1, 1, 2, 2, 3, 3]
my_set = set(a)
a = list(my_set)
print(a)    # [1, 2, 3]


# Tạo tập hợp rỗng
my_set = set()
print(type(my_set))   # <class 'set'>


# Chuyển xấu kí tự thành tập hợp các kí tự
s = "abcde"
set = set(s)
print(set)  # {'e', 'd', 'c', 'b', 'a'}


# Ép kiểu set cho từ điển sẽ tạo tập hợp khóa
d = {"1": "Khanh", "2": "Tony"}
set = set(d)
print(set)  # {'1', '2'}


# Hàm set tổng quát - set comprehension
set = {ord(ch) for ch in "abcdef"}
print(set)


# Lọc bằng if
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set = {x for x in list if x % 2 == 0}
print(set)  # {2, 4, 6, 8, 10}


# Thêm phần tử vào set
my_set = set()
print(my_set)   # set()
my_set.add(10)
print(my_set)   # {10}


# Xóa tất cả phần tử x khỏi tập hợp
set = {2, 4, 6, 8, 10, 2}
set.remove(2)   # xóa tất cả giá trị = 2
print(set)      # {4, 6, 8, 10} 
set.remove(11)  # KeyError: 11


# Sử dụng hàm copy() để chống bị tham chiếu
new_set = my_set.copy()


# Xóa tập hợp -> tập hợp rỗng
my_set.clear()


# Sử dụng toán tử in xem phần tử có nằm trong tập hợp không
set = {2, 4, 6, 8, 10, 2}
print(4 in set)     # True
print(5 in set)     # False


# 
