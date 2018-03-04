# Passing values to functions

# Argument value is substituted for name

# def power(x, n):                  pow(3, 5)
#   ans = 1                         x = 3
#   for i in range(0, n):           n = 5
#       ans = ans * x               ans = 1
#   return x                        for i in range(0, n) ...

# Like an implicit assignment statement

# Pass arguments by name


def power(x, n):
    ans = 1
    for i in range(0, n):
        ans = ans * x
    return ans


print(power(3, 4))
print(power(n=4, x=3))


# Default arguments

# Recall int(s) that converts string to integer
# int("76") is 76
# int("A5") generates an error
# Actually int(s, b) takes two arguments, string s and base b
# b has default value 10
# int("A5", 16) is 165 (10 * 16 + 5)

print(int("76"))
print(int("A5", 16))

# def int(s, b=10):
#   ...

# Default value is provided in function definition
# If parameter is omitted, default value is used
# Default value must be available at definition time
# def QuickSort(A, l=0, r=len(A)): does not work
# def f(a, b, c=14, d=22):
#   ...
# f(13, 12) is interpreted as f(13, 12, 14, 22)
# f(13, 12, 16) is interpreted as f(13, 12, 16, 22)
# Default values are identified by position, must come at the end
# Order is important

# Function definitions

# def associates a function body with a name
# Flexible, like other value assignments to name
# Definition can be conditional

# if conditon:
#   def f(a, b, c):
#       ...
# else:
#   def f(a, b, c):
#       ...

# Can assign a function to a new name
#   def f(a, b, c):
#       ...

# g = f
# Now g is another name for f

g = power

print(g(3, 4))
print(g(n=4, x=3))


# Can pass functions


def square(x):
    return x * x


def apply(f, x, n):  # Apply f to x n times
    res = x
    for i in range(n):
        res = f(res)
    return res


print(apply(square, 5, 2))


# Useful for customizing functions such as sort
# Define cmp(x, y) that returns -1 if x < y, 0 if x == y and 1 if x > y
# cmp("aab", "ab") is -1 in dictionary order
# cmp("aab", "ab") is 1 if we compare length
# def sortfunction(l, cmpfn=defaultcmpfn):
