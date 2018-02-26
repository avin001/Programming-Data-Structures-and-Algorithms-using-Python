# Define a Python function ascending(l) that returns True if each element in its input list is at least as big as the one before it.


def ascending(l):
    if len(l) < 2:
        return True
    return l[0] <= l[1] and ascending(l[1:])


print(ascending([]))
print(ascending([3, 3, 4, 5, 6, 6, 7]))
print(ascending([3, 3, 4]))
print(ascending([7, 18, 17, 19]))
