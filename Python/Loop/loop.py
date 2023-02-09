# Cấu trúc while khi out loop bằng break
while True:
    x = input()
    if x == '1':
        break

# Cấu trúc while khi out loop bằng điều kiện        
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


# Duyệt index
for i in range([start, end), step):
 
                
# Duyệt phần tử
for i in list:
                
                
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

for i in range(1, 8, 2):
    print(i, end=" ")   # 1 3 5 7
    
for i in range(5, 0, -1):
    print(i, end=' ')   # 5 4 3 2 1

    
# Từ khóa continue
for x in [1, 2, 3, 4, 5]:
    if x % 2 == 0:
        print(x, end=' ')   # 2 4
    else:
        continue

        
# Vòng lặp kép cho bảng cửu chương
for i in range(2, 10):
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)

        
# Tam giác * 
n = int(input())
for i in range(n):
    chuoi = ''
    for j in range(n - i - 1):
        chuoi += ' '
    for k in range(2 * i + 1):
        chuoi += '*'
    print(chuoi)
    

# Cấu trúc while-in lặp vô tận
x = "abcdef"
i = 'a'
while i in x:
    print(i, end=' ')    # a a a a a ...       

    


