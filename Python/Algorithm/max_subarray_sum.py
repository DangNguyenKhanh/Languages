# Tổng con liên tiếp lớn nhất
def max_subarray_sum(arr):
    n = len(arr)
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, n):
        max_ending_here = max(max_ending_here + arr[i], arr[i])
        print("max_ending_here", max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
        print("max_so_far", max_so_far)
    return max_so_far

# [4, -1, 2, 1] có tổng là 6
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6

