def partition(a, p, r):
    pivod = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < pivod:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    if a[i + 1] > a[r]:
        a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)

a = [5, 4, 3, 2, 1]
print(partition(a, 0, len(a) - 1))
quick_sort(a, 0, len(a) - 1)
print(a)
