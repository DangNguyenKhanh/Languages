# Truy xuất mảng 2 chiều mỗi dãy có số lượng phần tử không đều
array2D = [[1, 2],
           [3, 4, 5],
           [6, 7, 8, 9]]

for i in range(len(array2D)):
    print("Dãy", i+1, ":")
    for j in range(len(array2D[i])):
        print(array2D[i][j], sep='', end=' ')
    print()

    
# Lấy giá trị ánh xạ trực tiếp
a = [1, 2, 3]
x, y, z = a
print(x, y, z)      # 1 2 3



# Lấy dữ liệu trực tiếp trong list of list
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for x, y, z in a:
    print(x, y, z, end=' ')
    print()

# 1 2 3 
# 4 5 6 
# 7 8 9 
   
  
# List of list of list
a = [[1, 2, [3.1, 3.2, 3.3]],
     [4, 5, [6.1, 6.2, 6.3]],
     [7, 8, [9.1, 9.2, 9.3]]]

for x, y, z in a:
    print(x, y, end=' ')
    for i in z:
        print(i, end=' ')
    print()

# 1 2 3.1 3.2 3.3 
# 4 5 6.1 6.2 6.3 
# 7 8 9.1 9.2 9.3 















