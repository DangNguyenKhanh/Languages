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
print(t.screensize())   # canvas = (400, 300)


# Thiết lập lại canvas
t.screensize(2000, 1500)


# set màu nền canvas
t.screensize(bg="blue")


# Thiết lập tọa độ ảo đưa gốc tọa độ vào đó
t.setworldcoordinates(0, 0, 300, 200)
t.fd(100)


# Thiết lập màu vẽ cho bút vẽ
t.color("red")


# Vẽ hình tròn
t.circle(100, 360)    # Đường tròn bán kính 100 px
t.circle(100, 360, 5) # Lục giác 5 cạnh nội tiếp đường tròn = 5 nét
t.circle(50, 180)     # Nửa đường tròn
t.circle(50, 90)      # 1/4 đường tròn


# Tô màu cho hình
t.color("black", "violet")  # nét bút = black, tô màu = violet
t.pensize(3)    # Nét đậm của nét bút
t.begin_fill()
t.circle(100, 360)
t.end_fill()


# 
