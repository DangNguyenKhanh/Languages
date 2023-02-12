# Lệnh đọc, đầu đọc ở vị trí 0 đầu file
file = open(file.dat, 'r')


# Lệnh ghi lên file, nếu file đã có thì xóa file, nếu file chưa có thì tạo mới
file = open(file.dat, 'w')


# Hàm read() đọc tất cả nội dung file
content = file.read()
continue_content = file.read()  
print(continue_content)   # '' rỗng vì đầu đọc đã ở cuối file


#  
