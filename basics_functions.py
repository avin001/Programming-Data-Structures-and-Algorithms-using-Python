def power(x, n):  # Function name, arguments/parameters
    ans = 1
    for i in range(0, n):
        ans = ans * x
    return ans  # Return statement exits and returns a value.


# Passing values to functions - When we call a function we have to pass values for the arguments and this is done exactly the same way as assigning a value to a name

print(power(3, 5))  # Like an implicit assignment x = 3 and n = 5

# Same rules apply for mutable and immutable values

# Immutable values will not be affected at calling point

# Mutable values will be affected


def update(list, i, v):
    if i >= 0 and i < len(list):
        list[i] = v
        return True
    else:
        v = v + 1
        return False


ns = [3, 11, 12]
z = 8
print(update(ns, 2, z))

print(ns)  # If we pass through parameter a value which is mutable it can get updated in the function and this is sometimes called a side effect.

print(update(ns, 4, z))

print(z)  # If we pass through parameter a value which is immutable then the value doesn't change no matter what we do inside the function

# Return value may be ignored. If there is no return, function ends when last statement is reached. For example, a function which displays an error or warning message. Such a function just has to display a message and not compute or return anything.

# Scope of names

# Names within a function have local scope i.e. names within a function are disjoint from names outside a function.


def stupid(x):
    n = 17
    return x


n = 7
print(stupid(28))
print(n)

# A function must be defined before it is invoked


def f(x):
    return g(x + 1)


def g(y):
    return y + 3


print(f(77))

# If we define funtion g after invoking function f we will get an error saying NameError: name 'g' is not defined

# A function can call itself - recursion


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Functions are a good way to organise code in logical chunks

# Passing arguments to a function is like assigning values to names

# Only mutable values can be updated

# Names in functions have local scope

# Functions must be defined before use

# Recursion - a function can call itself
