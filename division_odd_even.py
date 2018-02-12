def divides(m, n):
    if n % m == 0:
        return True
    else:
        return False


def even(n):
    return divides(2, n)


def odd(n):
    return not divides(2, n)


print(divides(2, 7))
print(even(4))
print(even(5))
print(odd(3))
print(odd(6))
