# Tạo ra con rùa ở giữa màn hình (tọa độ 0,0) đang hướng về phải và đi 100 bước
import turtle as t
import time

t.fd(100)         # Tiến về phía trước 100 bước = 100 pixel
t.shape("turtle") # Nếu không có sẽ là mũi tên
time.sleep(5)     # ngăn đóng window


# Kích thước canvas - khung vẽ
- Kích thước 640 x 480 mặc định của window
         90 độ
180 độ            0 độ
        -90 độ

  
# Cho biết hướng - heading()
print(t.heading())  # 0 độ



# Xem tọa độ (x, y)
print(t.xcor(), t.ycor())   # 100.0 0.0


# Nâng bút
t.penup()


# Hạ bút (mặc định)
t.pendown()


# Kiểm tra đang hạ bút 
if t.isdown():
  
  
