# Mã ASCII
- Viết tắt của "American Standard Code for Information Interchange"
- Vì có 256 = 2^8 phần tử nên còn gọi là bảng ký tự 8 bits
- Hiện nay đã có bảng mã mới 16 bit = Unicode (Python có hỗ trợ Unicode)
- ASCII là một phần của Unicode


# In ra giá trị Dec trong bảng Unicode bằng ký tự
print(ord('a'))     # 97


# In ra ký tự bằng số Dec cho trước
print(chr(97))     # 'a'


# In ra ký tự mở rộng
print(ord('Á'))     # 193
print(chr(193))     # Á


# Chuyển đổi ký tự hoa sang thường và ngược lại, không đúng với tiếng việt
print(chr(ord('a') - 32))   # A
print(chr(ord('A') + 32))   # a
print(chr(ord('Ấ') + 32))   # Ễ   Sai


# So sánh 2 xâu 
"hoa" > "hanh" vì 'h' = 'h' và lần đầu tiên 'o' < 'a'


