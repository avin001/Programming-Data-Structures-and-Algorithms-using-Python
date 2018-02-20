import math

i = 5
j = 2 * i
j = j + 5
print(i)
print(j)
j = j - i
print(j)
print(7 / 2)
print(7 / 3.5)
print(8 + 2.6)
print(9 // 5)
print(9 % 5)
print(3 ** 4)

print(math.sqrt(36))
print(math.log2(2))
print(math.log2(4))

i = 5
print(type(i))
i = 7 * 1
print(type(i))
j = i / 3
print(type(i))
print(type(j))
i = 2 * j   # Not recommended to change the type of variables in a program
print(type(i))


print('True or False is: ', True or False)
print('False or True is: ', False or True)
print('True or True is: ', True or True)
print('False or False is: ', False or False)
print('True and False is: ', True and False)
print('False and True is: ', False and True)
print('False and False is: ', False and False)
print('True and True is: ', True and True)
print('Not applied to True gives us: ', not True)
print('Not applied to False gives us: ', not False)


def divides(m, n):
    return n % m == 0


def even(n):
    return divides(2, n)


def odd(n):
    return not divides(2, n)


print(divides(5, 25))
print(divides(3, 5))
print(even(2))
print(even(45))
print(odd(3))
print(odd(28))
