def factors(n):
    flist = []
    for i in range(1, n + 1):
        if not n % i:
            flist = flist + [i]
    return flist


def is_perfect_square(n):
    if n == 1:
        return True
    for i in factors(n)[1:-1]:
        if i ** 2 == n:
            return True
    return False


def sumofsquares(m):
    for i in range(1, m):
        if is_perfect_square(i) and is_perfect_square(m - i):
                return True
    return False


print(sumofsquares(41))
print(sumofsquares(30))
print(sumofsquares(17))
