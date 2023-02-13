# Vẽ hình vuông đi từ trái qua phải
import turtle as t
import time

t.shape()   # Mũi tên
def square(pixel):
    for i in range(4):
        t.fd(pixel)
        t.left(90)
square(100)

time.sleep(5)


# Vẽ hình vuông đi từ phải qua trái (đi hơi ngược)
def square(pixel):
    for i in range(4):
        t.back(pixel)
        t.right(90)
square(100)


# Tam giác đều sử dụng điều hướng setheading - seth()
def triangle(pixel):
    t.fd(pixel)
    t.seth(120)     # bẻ hướng chéo lên trái 
    t.fd(pixel)
    t.seth(-120)    # bẻ hướng chéo xuống trái
    t.fd(pixel)
triangle(100)


# Tam giác đều sử dụng di chuyển nhanh goto(x, y)
import math
def triangle(pixel):
    t.goto(pixel, 0)
    t.goto(pixel / 2, (math.sqrt(3) / 2) * pixel)
    t.goto(0, 0)    # t.home()
triangle(100)


# Tạo xoắn ốc
def spiral():
    pixel = 10
    while True:
        t.fd(pixel)
        t.right(90)
        pixel += 10
spiral()






