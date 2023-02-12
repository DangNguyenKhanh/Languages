# Tạo file.py và gọi hàm
# module_1.py
def f1():
  print('hello')

# main.py ta sử dụng gián tiếp
import module_1
module_1.f1()

# main.py ta sử dụng trực tiếp
from module_1 import *
f1()


