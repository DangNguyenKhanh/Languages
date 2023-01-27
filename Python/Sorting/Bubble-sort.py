# Bubble sort - Sắp xếp nổi bọt
def bubble_sort(a):
    n = len(a)
    for i in range(0, n-1, 1):
        for j in range(n-1, i, -1):
            if a[j] < a[j - 1]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
    return a


a = [9, 1, 8, 2, 7]
a = bubble_sort(a)
print(a)
# Trường hợp xấu nhất: 
