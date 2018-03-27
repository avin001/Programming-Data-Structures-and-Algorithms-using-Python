'''
Scope of name

Scope of name is the portion of code where it is available to read and update
By default, in Python, scope is local to functions: But only if we update the name inside the function


'''

# Example 1


def f():
    y = x
    print(y)


x = 7
f()


'''
Example 2


def f():
    y = x   # UnboundLocalError: local variable x referenced before assignment
    print(y)
    x = 22


x = 7
f()

'''

# If x is not found in f(), Python looks at enclosing function for global x
# If x is updated in f(), it becomes a local name!
# Actually this applies only to immutable values
