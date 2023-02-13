# Vẽ hình vuông
import turtle as t
import time

t.shape()   # Mũi tên
def square(pixel):
    for i in range(4):
        t.fd(pixel)
        t.left(90)
square(100)

time.sleep(5)
