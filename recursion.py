# Recursive functions are typically based on what we call inductive definitions

# Inductive Definitions

# Many arithmetic functions are naturally defined inductively

# Factorial
# 0! = 1
# n! = n * (n - 1)!

# Multiplication - repeated addition
# m * 1 = m
# m * (n + 1) = m + (m * n)
# m * n = m + (m * (n - 1))

# Define one or more base cases
# Inductive steps define f(n) in terms of smaller arguments

# Recursive computation

# Inductive definitions naturally give rise to recursive programs


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def multiply(m, n):
    if n == 1:
        return m
    return m + multiply(m, n - 1)


print(multiply(12, 12))
print(multiply(9, 6))


# Inductive definitions for lists

# Lists can be decomposed as
# First (or last) element
# Remaining list with one less element

# Define list functions inductively
# Base case: empty list or list of size 1
# Inductive step: f(l) in ters of smaller sublists of l


def length_of_list(l):
    if l == []:
        return 0
    return 1 + length_of_list(l[1:])


print(length_of_list([1, 2, 3, 4, 5, 6, 7]))
l = [10, 20, 30, 40, 50]
print(length_of_list(l))


def sum_of_list(l):
    if l == []:
        return 0
    return l[0] + sum_of_list(l[1:])


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_list(l))


# Recursive insertion sort

# Base case: if list has length 1 or 0, return the list
# Inductive step:
# Inductively sort slice l[0:len(l)- 1]
# Insert l[len(l) - 1] into this sorted slice


def Insertion_Sort(seq):
    isort(seq, len(seq))


def isort(seq, k):  # Sort slice seq[0:k]
    if k > 1:
        isort(seq, k - 1)
        insert(seq, k - 1)


def insert(seq, k):  # Insert seq[k] into sorted seq[0:k-1]
    pos = k
    while pos > 0 and seq[pos] < seq[pos - 1]:
        (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
        pos = pos - 1


seq = [74, 32, 89, 55, 21, 64]
Insertion_Sort(seq)
print(seq)
seq = list(range(500, 0, -1))
Insertion_Sort(seq)
print(seq)


# T(n), time to run insertion sort on length n
# Time T(n - 1) to sort slice seq[0:n - 1]
# n - 1 steps to insert seq[n - 1] in sorted slice
# Recurrence

# T(n) = n - 1 + T(n - 1)
# T(1) = 1

# T(n) = n - 1 + T(n - 1) = n - 1 + ((n - 2) + T(n - 2)) = ... =
# (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 = O(n**2)
