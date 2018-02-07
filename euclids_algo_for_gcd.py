def gcd_recursive(m, n):
    # Assume m >= n
    if m < n:
        (m, n) = (n, m)
    if m % n == 0:
        return n
    else:
        diff = m - n
        # diff > n? Possible!
        return gcd_recursive(max(n, diff), min(n, diff))


print(gcd_recursive(97, 2))
print(gcd_recursive(2, 97))
print(gcd_recursive(14, 63))


def gcd(m, n):
    if m < n:   # Assume m >= n
        (m, n) = (n, m)
    while m % n != 0:
        diff = m - n
        # diff > n? Possible!
        (m, n) = (max(n, diff), min(n, diff))
    return n


print(gcd(12, 50))
print(gcd(12, 78))
print(gcd(12, 100))


def euclids_algo_gcd_optimised_recursive(m, n):
    if m < n:   # Assume m >= n
        (m, n) = (n, m)
    if m % n == 0:
        return n
    else:
        return euclids_algo_gcd_optimised_recursive(n, m % n)   # m % n < n, always!


print(euclids_algo_gcd_optimised_recursive(4, 50))
print(euclids_algo_gcd_optimised_recursive(4, 144))
print(euclids_algo_gcd_optimised_recursive(4, 25))


def euclids_algo_gcd_optimised_using_while(m, n):
    if m < n:   # Assume m >= n
        (m, n) = (n, m)
    while m % n != 0:
        (m, n) = (n, m % n)     # m % n < n, always!
    return n


print(euclids_algo_gcd_optimised_using_while(144, 288))
print(euclids_algo_gcd_optimised_using_while(180, 360))
print(euclids_algo_gcd_optimised_using_while(525, 1000))
