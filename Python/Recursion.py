# Một lệnh lặp được bao nhiêu lần ?
import sys
print(sys.getrecursionlimit())  # 1000


# Hàm đệ quy Fibonacci - Nên sử dụng cách không đệ quy
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1)) # 1
print(fibonacci(2)) # 2
print(fibonacci(3)) # 3
print(fibonacci(4)) # 5
print(fibonacci(5)) # 8


# Hàm đệ quy factorial - giai thừa 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6
print(factorial(4)) # 24


# hàm đệ quy đảo ngược reverse_list, reverse_str

