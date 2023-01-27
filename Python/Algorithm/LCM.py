# LCM - Least Common Multiple: Bội chung nhỏ nhất
def GCD(a, b):
    if a < b:
        return GCD(b, a)
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# a * b = GCD * LCM
def LCM(a, b):
    res = (a * b) / GCD(a, b)
    return res


res = LCM(12, 4)
print(res)
