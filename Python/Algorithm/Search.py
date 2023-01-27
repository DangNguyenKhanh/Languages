# Sequential search
def sequential_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i      # if found return index
    return -1             # not found return -1

a = [1, 2, 5, 7, 8, 9]
res = sequential_search(a, 9)
print(res)
  
    
# Binary search
def binary_search(a, x):
    index = -1
    i = 0
    j = len(a) - 1
    while i <= j:
        k = int((i + j) / 2)
        if x < a[k]:
            j = k - 1
        elif x == a[k]:
            index = k
            break
        else:
            i = k + 1
    return index

a = [1, 2, 5, 7, 8, 9]
res = binary_search(a, 9)
print(res)
  
