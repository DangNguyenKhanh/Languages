# Interchange Sort - Đổi chỗ trực tiếp
def interchange_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
# Trường hợp xấu nhất: O(n * (n - 1) / 2) = O(n^2)
# Không gian hỗ trợ: O(1)
