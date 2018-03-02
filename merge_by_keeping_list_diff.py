'''
Variation on merge

List difference: elements in a but not in b
'''


def merge(a, b):  # Merge a[0:m], b[0:n]
    (c, m, n) = ([], len(a), len(b))
    (i, j) = (0, 0)  # Current positions in a, b
    while i + j < m + n:
        if i == m:  # Case 1: a is empty
            break
        elif j == n:  # Case 2: b is empty
            c.append(a[i])
            i = i + 1
            j = 0
        elif a[i] == b[j]:  # Case 3: Head of a is equal to head of b
            i = i + 1
            j = 0
        else:
            j = j + 1
    return c


a = list(range(0, 20, 2)) + list(range(30, 40, 2))
b = list(range(10, 30, 2))
print(a)
print(b)
print(merge(a, b))
