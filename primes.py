def factors(n):
    flist = []
    for i in range(1, n + 1):
        if not n % i:
            flist = flist + [i]
    return flist


def is_prime(n):
    return factors(n) == [1, n]


print(is_prime(2))
print(is_prime(1))
print(is_prime(11))
print(is_prime(25))
print(is_prime(28))


def primes_upto(n):
    prime_list = []
    for i in range(2, n):  # We know that we have to scan from 1 to n, use for
        if is_prime(i):
            prime_list = prime_list + [i]
    return prime_list


print(primes_upto(30))
print(primes_upto(60))
print(primes_upto(90))


def first_n_primes(n):
    (count, i, plist) = (0, 2, [])
    while count < n:  # Range to scan not known in advance, hence using while
        if is_prime(i):
            (count, plist) = (count + 1, plist + [i])
        i = i + 1
    return plist


print(first_n_primes(10))


# for and while

# Can use while to simulate for

'''
# for loop using range

for n in range(i, j):
    statement

# while loop to simulate for

n = i
while n < j:
    statement
    n = n + 1

# for loop using iteration through elements of a list

for n in l:
    statement

# while loop to simulate for

i = 0
while i < len(l):
    n = l[i]
    statement
    i = i + 1

* Can use while to simulate for
* However, use for where it is natural which makes for more readable code
* What makes a good program? - Correctness and efficiency - algorithm
* Readability, ease of maintenance - style
* There are two parts to programming.
    * First is what you want to say, which is the algorithm
    * Second is how you want to say it, which is the style

'''
