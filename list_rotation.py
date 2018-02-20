def rotatelist(l, k):
    nl = l[:]
    if k <= 0:
        return l
    while k > 0:
        nl = nl[-1:] + nl[:-1]
        k = k - 1
    return nl


print(rotatelist([1, 2, 3, 4, 5], 1))
print(rotatelist([1, 2, 3, 4, 5], 3))
print(rotatelist([1, 2, 3, 4, 5], 12))
