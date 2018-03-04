# Operating on lists

# Update an entire list

#   for x in l:
#       x = f(x)

# Define a function to do this in general

#   def applylist(f, l):
#       for x in l:
#           x = f(x)

# Built in function map()

# map(f, l) applies f to each element of l
# Output of map(f, l) is not a list!
# Use list(map(f, l)) to get a list
# Can be used directly in a for loop
# for i in map(f, l):
# Like range(i, j), d.keys()

# Selecting a sublist

# Extract list of primes fromlist numberlist

#   primelist = []
#   for i in numberlist:
#       if isprime(i):
#           primelist.append(i)
#   return primelist

# In general

#   def select(property, l):
#       sublist = []
#       for x in l:
#           if property(x):
#               sublist.append(x)
#       return sublist

# Note that property is a function that returns True or False for each element

# Built in function filter()

# filter(p, l) checks p for each element of l
# Output is sublist of values that satisfy p

# Find some of squares of even numbers from 0 to 99


def iseven(x):
    return x % 2 == 0


def square(x):
    return x * x


print(list(map(square, filter(iseven, range(100)))))


# List comprehension

# Pythagorean triple: x ** 2 + y ** 2 = z ** 2

# Find all Pythagorean triples (x, y, z) with values below n
# Conventional mathematics notation
# {(x, y, z) | 1 <= x, y, z <= n, x ** 2 + y ** 2 = z **2}
# In set theory, this is called set comprehension
# Building a new set from existing sets
# Extends to lists

print('*' * 356)

# Squares of even numbers below 100

print([square(x) for x in range(100) if iseven(x)])

print('*' * 356)

# Pythogorean triples with x, y, z below 100

print([(x, y, z) for x in range(100) for y in range(100) for z in range(100) if x ** 2 + y ** 2 == z ** 2])

# Multiple generators
# Later generators can depend on earlier ones
# Eliminating duplicates

print('*' * 356)

print([(x, y, z) for x in range(1, 100) for y in range(x, 100) for z in range(y, 100) if x ** 2 + y ** 2 == z ** 2])

print('*' * 356)

# Useful for initialising lists

# Initialise a 4 x 3 matrix, 4 rows, 3 columns, stored row-wise

matrix = [[0 for i in range(3)] for j in range(4)]
print(matrix)

print('*' * 356)

# Warning

zerolist = [0 for i in range(3)]
l = [zerolist for j in range(4)]
l[1][1] = 7
print(l)

# Each row in l points to same list zerolist.
# If you want to create a 2 dimensional matrix and initialize it, make sure you intialize it in one shot using a nested range, and not in 2 copies like this.
