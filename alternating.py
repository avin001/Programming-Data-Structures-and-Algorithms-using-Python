# Define a Python function alternating(l) that returns True if the values in the input list alternately go up and down (in a strict manner).


def alternating(l):
    for i in range(1, len(l) - 1):
        if not (l[i - 1] < l[i] > l[i + 1] or l[i - 1] > l[i] < l[i + 1]):
            return False
    return True


print(alternating([]))
print(alternating([1, 3, 2, 3, 1, 5]))
print(alternating([3, 2, 3, 1, 5]))
print(alternating([3, 2, 2, 1, 5]))
print(alternating([3, 2, 1, 3, 5]))
