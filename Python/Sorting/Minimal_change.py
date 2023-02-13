def insert_num(n, a, k):
    new_list = []
    if k == 0:
        new_list = [n] + a
    elif k == len(a) + 1:
        new_list = a + [n]
    else:
        new_list = a[ : k] + [n] + a[k : ]
    return new_list

def insert_all(n, a):
    new_list = []
    for k in range(len(a) + 1):
        new_list.append(insert_num(n, a, k))
    return new_list

def permutation(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [[1, 2], [2, 1]]
    else:
        new = []
        a = permutation(n - 1)
        for pe in a:
            new = new + insert_all(n, pe)
        return new

a = permutation(4)
print(a)
