# Without import math library
print(3 + 4)        # 7
print(3 - 4)        # -1
print(3 * 4)        # 12
print(3 / 4)        # 0.75

# Floor Division - div
print((-1) // 2)    # -1    phép chia lấy nguyên, làm tròn hướng về âm vô cùng
print(3 // 4)       # 0

# mod
print(3 % 4)        # 3

# absolute
print(abs(-1))      # 1

# power
print(pow(2, 3))    # 8
print(2 ** 3)       # 8
print(2 ** 2 ** 2)  # 2^(2^2) = 2^4 = 4 x 4 = 16


# when import math
import math
print(math.pi)                              # 3.141592653589793

print(math.sin(math.pi / 2))                # 1.0
print(math.cos(math.pi))                    # -1.0
print(math.tan(math.pi / 4))                # 0.9999999999999999

print(math.sqrt(4))                         # 2.0


# Làm tròn
print(math.ceil(3.9))                       # 4
print(math.ceil(3.1))                       # 4
print(math.ceil(math.tan(math.pi / 4)))     # 1

print(math.floor(3.9))                      # 3
print(math.floor(3.1))                      # 3


# Đẳng thức luôn đúng
a = b * (a // b) + (a % b)
