'''O(n**2) sorting algorithms

Selection and Insertion sort are both O(n**2)
O(n**2) sorting is infeasible for n over 5000

A different strategy?

Divide array in two equal parts
Separately sort left and right half
Combine the two sorted halves to get the full array sorted

Combining sorted lists

Given two sorted lists A and B, combine into a sorted list C
Compare first elements of A and B
Move it into C
Repeat until all elements in A and B are over

Merge Sort

Sort A[0:n//2]
Sort a[n//2:n]
Merge sorted halves into B[0:n]
How do we sort the halves?
Recursively, using the same strategy!

Divide and conquer

Break up problem into disjoint parts
Solve each part separately
Combine the solutions efficiently

Merging sorted lists

Combine two sorted lists A and B into C
If A is empty, copy B into C
If B is empty, copy A into C
Otherwise, compare first elements of A and B and move the smaller of the two into C
Repeat until all elements in A and B have been moved.

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
        elif a[i] <= b[j]:  # Case 3: Head of a is smaller
            c.append(a[i])
            i = i + 1
        elif a[i] > b[j]:  # Case 4: Head of b is smaller
            c.append(b[j])
            j = j + 1
    return c


a = list(range(0, 100, 2))
b = list(range(1, 75, 2))
print(merge(a, b))

'''
Merge Sort

To sort a[0:n] into b[0:n]
if n is 1, nothnig to be done
Otherwise
sort[0:n//2] into l(left)
sort[n//2:n] into r(right)
Merge l and r into b
'''


def mergesort(a, left, right):
    # Sort the slice a[left:right]
    if right - left <= 1:  # Base case
        return a[left:right]
    if right - left > 1:  # Recurisve call
        mid = (left + right) // 2
        l = mergesort(a, left, mid)
        r = mergesort(a, mid, right)
        return merge(l, r)


a = list(range(1, 100, 2)) + list(range(0, 100, 2))
print(mergesort(a, 0, len(a)))
