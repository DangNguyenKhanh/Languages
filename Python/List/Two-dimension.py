# Khởi tạo mảng 2 chiều và in mảng 2 chiều
array2D = []
m = int(input())    # row
n = int(input())    # col
for i in range(m):
    b = []
    for j in range(n):
        x = int(input("a[" + str(j) + "] = "))
        b += [x]
    array2D.append(b)

for i in range(m):
    for j in range(n):
        print(array2D[i][j], sep='', end=' ')
    print()

        
# Random matrix n x n
from random import random
n = 3
array2D = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(int(100 * random()) + 1)
    array2D.append(x)

for i in range(n):
    for j in range(n):
        print(array2D[i][j], end=' ')
    print() 
