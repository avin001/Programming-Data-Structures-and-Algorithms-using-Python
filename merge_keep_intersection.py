'''
Variation on merge

Logic as below:

Intersection of two sorted lists
if A[i] < b[j], increment i
if B[j] < a[i], increment j
if A[i] == B[j]
    while A[i] == B[j], increment j
    append A[i] to C and increment i
'''


def merge(A, B):  # Merge A[0:m], B[0:n]
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)  # Current positions in A, B
    while i + j < m + n:
        if i == m:  # Case 1: A is empty
            break
        elif j == n:  # Case 2: B is empty
            break
        elif A[i] < B[j]:  # Case 3: Head of A is smaller
            i = i + 1
        elif B[j] < A[i]:  # Case 4: Head of B is smaller
            j = j + 1
        elif A[i] == B[j]:  # Case 5: Head of A is equal to head of B
            j = j + 1
            C.append(A[i])
            i = i + 1
    return C


A = list(range(0, 20, 2))
B = list(range(10, 30, 2))
print(A)
print(B)
print(merge(A, B))
