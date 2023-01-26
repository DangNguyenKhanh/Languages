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


 
