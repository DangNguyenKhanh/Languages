# hàm input() trả về chuỗi kí tự
x = input("Get x: ")
print(type(x))          # <class 'str'>


# Ép kiểu
x = int(input("Get x: "))
y = int(input("Get y: "))
print(type(x))          # <class 'int'>


# Nhập 2 số x và y tính tổng x + y
x = int(input("Get x: "))
y = int(input("Get y: "))
sum = x + y
print("Sum of x and y:", sum)

x = int(input("Get x: "))
y = int(input("Get y: "))
sum = x + y
print("Sum of " + str(x) + " and " + str(y) + ":", sum)


