# Loops revisited

# Two types of loops

# for i in l:
#   ...

# Repeat body for each item in l

# while condition:
#   ...

# Repeat body till condition becomes False

# Sometimes we may want to cut short the loop

# Search for value in a list


def findpos(l, v):
    # Return first position of v in l
    # Return -1 if v not in l
    (found, i) = (False, 0)
    while i < len(l):
        if not found and l[i] == v:
            (found, pos) = (True, i)
        i = i + 1
    if not found:
        pos = -1
    return pos


print(findpos([1, 2, 3, 4, 5], 7))
print(findpos([23, 34, 45, 67, 78, 45, 89, 45], 45))


# A more natural strategy
# Scan list for value
# Stop scan as soon as we find the value
# If the scan completes without success, report -1


def findpos_optimised1(l, v):
    (pos, i) = (-1, 0)
    for x in l:
        if x == v:  # Exit, report position of x
            pos = i
            break
        i = i + 1
    # If pos not reset in loop, pos is -1
    return pos


print(findpos_optimised1([1, 2, 3, 4, 5], 7))
print(findpos_optimised1([23, 34, 45, 67, 78, 45, 89, 45], 45))


def findpos_optimised2(l, v):
    pos = -1
    for i in range(len(l)):
        if l[i] == v:  # Exit, report position
            pos = i
            break
    # If pos not reset in loop, pos is -1
    return pos


print(findpos_optimised2([1, 2, 3, 4, 5], 7))
print(findpos_optimised2([23, 34, 45, 67, 78, 45, 89, 45], 45))


# A loop (both for and while loops) can also have an else: - signals normal termination which gets executed if the loop terminates normally.


def findpos_optimised3(l, v):
    for i in range(len(l)):
        if l[i] == v:  # Exit, report position
            pos = i
            break
    else:
        pos = -1  # No break, v not in l
    return pos


print(findpos_optimised3([1, 2, 3, 4, 5], 7))
print(findpos_optimised3([23, 34, 45, 67, 78, 45, 89, 45], 45))
