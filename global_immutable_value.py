'''
Global immutable values

What if we want a global integer: say to count the number of times a function is called
Declare a name to be global

'''


def f():
    global x
    y = x
    print(y)
    x = 22


x = 7
f()
print(x)
