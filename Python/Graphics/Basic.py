# Xóa màn hình, quay về vị trí mặc định
t.reset()


# Khởi đầu tại vị trí mình muốn 
t.penup()
t.setx(100)
t.sety(100)
t.pendown()


# Quay về gốc tọa độ
t.home()


# Thiết lập cửa sổ 
t.setup(480, 360, startx=100, starty=200)
- Ngang 480 dọc 360 cách bên trái màn hình desktop 100 và cách bên trên 200


# Kiểm tra độ rộng canvas
t.setup(480, 360, startx=100, starty=200)
print(t.screensize())   # canvas = (400, 300)


# 
