'''A positive integer m is a sum of squares if it can be written as k + l where k > 0, l > 0 and both k and l are perfect squares.

Write a Python function sumofsquares(m) that takes an integer m returns True if m is a sum of squares and False otherwise. (If m is not positive, your function should return False.)'''


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
