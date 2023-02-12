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


# Hàm đệ quy đảo ngược reverse_str
def reverse_str(s):
    if s == "":
        return ""
    else:
        return s[-1] + reverse_str(s[:-1])  # s[:-1] = s[-len():-1] bắt đầu từ -len() đến -2

print(reverse_str("abcde")) # edcba
print("abcde"[ : : -1]) # edcba - Kỹ thuật slicing


# Hàm đệ quy đảo ngược reverse_list
def reverse_list(A):
    if A == []:
        return []
    else:
        return A[len(A)-1 : ] + reverse_list(A[ : len(A)-1])

print(reverse_list([1, 2, 3, 4, 5]))
print([1, 2, 3, 4, 5][ : : -1]) # [5, 4, 3, 2, 1]   - Kỹ thuật slicing


