'''
Doing nothing

Recall: reading a number from keyboard


while(True):
    try:
        userdata = int(input("Enter a number: "))
    except ValueError:
        print("Not a number. Try again.")
    else:
        break


What if we just want to repeat the loop on an error?


while(True):
    try:
        userdata = int(input("Enter a number: "))
    except ValueError:
        # Do nothing
    else:
        break


Blocks such as except:, else:, ... cannot be empty
Use pass for a null statement


while(True):
    try:
        userdata = int(input("Enter a number: "))
    except ValueError:
        pass
    else:
        break



Removing a list entry

Want to remove l[4]?

del(l[4])

Automatically contracts the list and shifts elements in l[5:] left

Also works for dictionaries

del(d[k]) removes the key k and its associated value

Undefining a value

In general, del(x) removes the value associated with x, makes x undefined

x = 7
del(x)
y= x + 5

NameError: name 'x' is not defined

Checking undefined name

Assign a value to x only if x is undefined

try:
    x
except NameError:
    x = 5


The value None

"None" is a special keyword used to denote "nothing"
Use it to intialize a name and later check if it has been assigned a valid value

x = None
...

if x is not None:
    y = x

'''

while(True):
    try:
        userdata = int(input("Enter a number: "))
    except ValueError:
        pass
    else:
        break


l = list(range(10))
print(l)
del(l[4])
print(l)

x = 7
del(x)
try:
    y = x + 5
except NameError:
    print("x is undefined.")

try:
    x
except NameError:
    x = 5

print(x)
