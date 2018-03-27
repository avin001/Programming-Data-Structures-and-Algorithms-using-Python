'''
Global names that point to mutable values can be updated within a function

'''


def f():
    y = x[0]
    print(y)
    x[0] = 22


x = [7]
f()
