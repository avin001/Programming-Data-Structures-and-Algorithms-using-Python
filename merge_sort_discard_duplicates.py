'''
Variation on merge

Logic as below:
Union of two sorted lists(discard duplicates i.e. keep a single copy)
while a[i] == b[j], increment j
append a[i] to c and increment i
'''


def merge(a, b):  # Merge a[0:m], b[0:n]
    (c, m, n) = ([], len(a), len(b))
    (i, j) = (0, 0)  # Current positions in a, b
    while i + j < m + n:
        if i == m:  # Case 1: a is empty
            c.append(b[j])
            j = j + 1
        elif j == n:  # Case 2: b is empty
            c.append(a[i])
            i = i + 1
        elif a[i] < b[j]:  # Case 3: Head of a is smaller
            c.append(a[i])
            i = i + 1
        elif a[i] > b[j]:  # Case 4: Head of b is smaller
            c.append(b[j])
            j = j + 1
        elif a[i] == b[j]:  # Case 5: Head of a is equal to head of b
            while a[i] == b[j]:
                j = j + 1
            c.append(a[i])
            i = i + 1

    return c


def mergesort(a, left, right):
    # Sort the slice a[left:right]
    if right - left <= 1:  # Base case
        return a[left:right]
    if right - left > 1:  # Recurisve call
        mid = (left + right) // 2
        l = mergesort(a, left, mid)
        r = mergesort(a, mid, right)
        return merge(l, r)


a = list(range(0, 20, 2)) + list(range(10, 30, 2))
print(mergesort(a, 0, len(a)))
