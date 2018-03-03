'''
Merge Sort: Shortcomings

Merging A and B creates a new array C
No efficient way to manage merge in place

Extra storage can be costly
Inherently recursive
Recursive call and return are expensive

Alternative approach

Extra space is required to merge
Merging happens because elements in left half must move right and vice versa
Can we divide so that everything to the left is smaller than everything to the right?

No need to merge!

Divide and conquer without merging

Suppose the median value in A is m
Move all values <= m to left half of A
Right half has values > m
This shifting can be done in place, in time O(n)
Recursively sort left and right halves
A is sorted! No need to merge

How do we find median?
Sort and pick up middle element
But our aim is to sort!

Instead, pick up some value in A, pivot
Split A with respect to this pivot element

Choose a pivot element, typically the first element in the array
Partition A into lower and upper parts with respect to pivot
Move pivot between lower and upper partition
Recursively sort the two partitions
'''


def quick_sort(A, l, r):  # Sort A[l:r]
    if r - l <= 1:
        return
    # Partition with respect to pivot, A[l]
    yellow = l + 1
    for green in range(l + 1, r):
        if A[green] <= A[l]:
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow = yellow + 1
    # Move pivot into place
    (A[l], A[yellow - 1]) = (A[yellow - 1], A[l])
    # Recursive calls
    quick_sort(A, l, yellow - 1)
    quick_sort(A, yellow, r)


l = list(range(100, 0, -2))
print(l)
quick_sort(l, 0, len(l))
print(l)
