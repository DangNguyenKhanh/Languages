# Cấu trúc while
while True:
    x = input()
    if x == '1':
        break

i = 0
while i < 10:
    i += 2
print(i)        
 
    
# Cấu trúc while-else thực thi khi kết thúc vòng lặp bằng điều kiện while
i = 0
while i < 3:
    i += 1
else:
    print('hello')  # hello

    
# Cấu trúc while-else sẽ không thực thi else nếu thực hiện break
i = 0
while True:
    i += 1
    if i >= 3:
        break
else:
    print('hello')  # Không in ra gì hết

    
# Cấu trúc lặp for cho mảng
count = 0
for i in [1, 2, 3, 4, 5]:
    count += 1
print(count)


# in ra các phần tử bằng for
for i in [1, 2, 3, 4, 5]:
    print(i)


# Sử dụng range trong for. Syntax: range(start, end, step) trong đó [start, end)
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4

for i in range(3, 5):
    print(i, end=" ")   # 3 4

    
