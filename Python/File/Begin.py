# inp.dat
hello world
1 2 3 4 5
1.1 2.2 3.3 4.4 5.5


# In ra tất cả nội dung file
file = open("inp.dat", 'r')     # 'r' là read
content = file.read()
print(content)


# Liên kết file ở desktop, xem địa chỉ ở properties của file
file = open("C:\\Users\\Admin\\OneDrive - hcmut.edu.vn\\Desktop\\lol.dat", 'r')
content = file.read()
print(content)


# Kiểu dữ liệu của file
file = open("inp.dat", 'r')
content = file.read()
print(type(file))       # <class '_io.TextIOWrapper'>
print(type(content))    # <class 'str'>


# Xem các hàm của file
print(dir(file))


