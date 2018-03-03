'''
Variation on merge

List difference: elements in A but not in B
'''


def merge(A, B):  # Merge A[0:m], B[0:n]
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)  # Current positions in A, B
    while i + j < m + n:
        if i == m:  # Case 1: A is empty
            break
        elif j == n:  # Case 2: B is empty
            C.append(A[i])
            i = i + 1
            j = 0
        elif A[i] == B[j]:  # Case 3: Head of A is equal to head of B
            i = i + 1
            j = 0
        else:
            j = j + 1
    return C


A = list(range(0, 20, 2)) + list(range(30, 40, 2))
B = list(range(10, 30, 2))
print(A)
print(B)
print(merge(A, B))
