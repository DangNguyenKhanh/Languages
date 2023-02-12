# Lệnh đọc, đầu đọc ở vị trí 0 đầu file
file = open(file.dat, 'r')


# Lệnh ghi lên file, nếu file đã có thì xóa file, nếu file chưa có thì tạo mới
file = open(file.dat, 'w')


# Hàm read() đọc tất cả nội dung file
content = file.read()
continue_content = file.read()  
print(continue_content)   # '' rỗng vì đầu đọc đã ở cuối file


# Hàm f.tell() cho biết vị trí đọc cũng chính là số lượng byte đã đọc được
f = open("inp.dat", 'r')
print(f.tell())     # 0
content = f.read()
print(content)
print(f.tell())     # 45 số lượng byte đã đọc được


# Đóng tệp đang mở
f = open("inp.dat", 'r')
content = f.read()
f.close()   # Khi đóng tệp không còn dùng được tell() nữa


# Hàm f.readline() đọc dữ liệu 1 dòng
f = open("inp.dat", 'r')
print(f.tell())                 # 0
print(f.readline(), end='')     # hello world
print(f.tell())                 # 13
print(f.readline(), end='')     # 1 2 3 4 5
print(f.tell())                 # 24
print(f.readline(), end='')     # 1.1 2.2 3.3 4.4 5.5
print(f.tell())                 # 45
f.close()

# Đưa 1 2 3 4 5 vào list
f = open("inp.dat", 'r')
print(f.readline(), end='')     # hello world
s = f.readline()
a = s.split()
print(a)        # ['1', '2', '3', '4', '5']
for i in range(len(a)):
    a[i] = int(a[i])
print(a)        # [1, 2, 3, 4, 5]
f.close()


# Mỗi dòng sẽ là 1 list và bỏ tất cả list từng dòng vào 1 list chung
f = open("inp.dat", 'r')
a = f.readlines()
print(a)    # ['hello world\n', '1 2 3 4 5\n', '1.1 2.2 3.3 4.4 5.5\n']
f.close()


# In ra từng dòng trong file bằng for 
f = open("inp.dat", 'r')
for line in f:
    print(line, end='')
f.close()


# 


