# Thay đổi hình dáng con rùa
t.shape("turtle")
t.shape("arrow")        # tam giác đều
t.shape("triangle")     # tam giác cân
t.shape("circle")
t.shape("square")
t.shape("classic")      # mũi tên


# Lấy ảnh khác từ *.gif
dùng addshape() hoặc register_shape()
t.addshape("Electus.gif")
t.shape("Electus.gif")


# Cho biết các shape hiện có
t.getshapes()


# Thiết lập màu của rùa - những hình mặc định có sẵn
t.shape("turtle")
t.fillcolor("red")


# Thay đổi kích thước của rùa
shapesize() hoặc turtlesize()
shapesize(Chiều rộng gấp, chiều dài gấp, độ rộng của viền) đơn vị pixel


# Phân thân rùa
t.shape("turtle")
t1 = t.clone()
t.fd(100)
t.mainloop()


