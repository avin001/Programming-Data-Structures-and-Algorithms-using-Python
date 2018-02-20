# Shortcuts for conditions

# Numeric value 0 is treated as False

# Empty sequence "", [] is treated as False

# Everything else is True

import math


def gcd(m, n):
    if m % n:  # This is another way of using condition m % n != 0
        (m, n) = (n, m % n)
    else:
        return n


print(gcd(16, 4))

# Multiway branching, elif: Replace nested else-if with elif


def line(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    else:  # else is optional while using elif for multiway branching
        return 4


print(line(2))
print(line(4))

# Loops: repeated actions

# Repeat a fixed number of times

list1 = [1, 2, 3, 4]
list2 = [1, 1, 1, 1]


def loop1():
    for i in list1:
        list1[i-1] = i ** 2
        list2[i-1] = math.sqrt(list1[i-1])


print('****')
loop1()
print(list1)
print(list2)

list3 = [0, 0, 0, 0]


def loop2():
    for x in range(0, len(list1)):
        list3[x] = math.log2(list1[x])


print(list1)
loop2()
print(list3)


def factors(n):
    flist = []
    for i in range(1, n + 1):
        if not n % i:
            flist = flist + [i]
    return flist


print(factors(25))
print(factors(256))


# loop based on a condition - Often we don't know the number of repetitions in advance


def gcd_using_euclids_algo(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n:
        (m, n) = (n, m % n)
    return n


print(gcd_using_euclids_algo(12, 144))
print(gcd_using_euclids_algo(25, 2))
