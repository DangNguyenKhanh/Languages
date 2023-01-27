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
# Số lần so sánh: (n - 1) + (n - 2) + ... + 1 = n/2 * [2 * (n - 1) - (n- 1)] = n * (n - 1) / 2 
# Số lần di chuyển: 3 * n * (n - 1) / 2 
# Trường hợp xấu nhất: T(n) = O(n^2) khi mảng bị sắp xếp giảm dần 



