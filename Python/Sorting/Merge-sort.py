def merge(left, right):
    res = []
    while left != [] and right != []:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right = right[1:]
        if len(left) == 0:
            res.extend(right)
            break
        if len(right) == 0:
            res.extend(left)
            break
    return res

def merge_sort(A):
    if len(A) <= 1:
        return A
    left = A[:len(A)//2]
    right = A[len(A)//2:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

A = [5, 4, 3, 2, 1]
A = merge_sort(A)
print(A)    # [1, 2, 3, 4, 5]
