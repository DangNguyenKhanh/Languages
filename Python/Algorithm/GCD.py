def GCD(a, b):
    if a < b:
        return GCD(b, a)
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

res = GCD(12, 4)
print(res)
