def gcd_naive(m, n):
    fm = []
    for i in range(1, m + 1):
        if m % i == 0:
            fm.append(i)
    fn = []
    for j in range(1, n + 1):
        if n % j == 0:
            fn.append(j)
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return cf[-1]


print(gcd_naive(14, 63))
print(gcd_naive(18, 25))
print(gcd_naive(9, 81))


def gcd_with_one_scan(m, n):
    cf = []
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            cf.append(i)
    return cf[-1]


print(gcd_with_one_scan(144, 288))
print(gcd_with_one_scan(180, 360))
print(gcd_with_one_scan(525, 1000))


def gcd_without_lists(m, n):
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            mrcf = i
    return mrcf


print(gcd_without_lists(12, 50))
print(gcd_without_lists(12, 78))
print(gcd_without_lists(12, 100))


def gcd_optimised(m, n):
    i = min(m, n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i
        else:
            i = i - 1


print(gcd_optimised(4, 50))
print(gcd_optimised(4, 144))
print(gcd_optimised(4, 25))
