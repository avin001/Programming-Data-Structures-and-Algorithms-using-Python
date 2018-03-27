def f():
    def g(a):
        return a + 1

    def h(b):
        return 2 * b

    global x
    y = g(x) + h(x)
    print(y)
    x = 22


x = 7
f()


'''
Can define local "helper" functions
g() and h() are only visible to f()
Cannot be called directly from outside
If we look up x, y inside g() or h(), it will first look in f(), then outside
Can also declare names global inside g(), h()
Intermediate scope declaration: nonlocal (see Python documentation)

'''
