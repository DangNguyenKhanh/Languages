# Đặt tiêu đề cho window
t.title("electus")


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


# Game click trên màn hình rùi con trỏ sẽ chạy tới
def print_coord(x, y):
    t.goto(x, y)
    print(x, y)

t.onscreenclick(print_coord)
t.mainloop()


# Khi nháy chuột lên con rùa, con rùa đổi hướng
def print_coord(x, y):
    t.goto(x, y)
    print(x, y)

def turn(x, y):
    t.left(90)

t.onclick(turn)
t.onscreenclick(print_coord)
t.mainloop()


# Kết thúc sự kiện
t.onclick(None)
t.onscreenclick(None)


# Tốc độ con trỏ
t.speed(1)  rất chậm
t.speed(3)  chậm  - mặc định của rùa
t.speed(5)  trung bình
t.speed(10) nhanh
t.speed(20) >10 rất nhanh


# Vẽ đường thẳng dấu đi con rùa
t.ht()          # hide turtle
t.forward(100)  # draw a line without the turtle's shape being visible
t.mainloop()


# Tắt chế độ hoạt hình bằng tracer
t.ht()
t.tracer(0, 0)  # Không có hoạt hình, giúp in ra liền
for alpha in range(0, 360, 15):
    t.seth(alpha)
    t.goto(0, 0)
    t.circle(100, steps=5)
t.update()
t.mainloop()


