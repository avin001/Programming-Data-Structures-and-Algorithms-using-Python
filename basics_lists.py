factors = [1, 2, 5, 10]
names = ['Anand', 'April', 'Justin']
mixed = [3, True, 'Yellow']
print(factors[3])
print(names[0])
print(mixed[0:2])
print(len(names))

s = 'hello'

# For a string, both a single position and a slice return strings
print(type(s[0]))
print(type(s[0:1]))

# For a list, a single position returns a value, a slice returns a list

print(factors[1])
print(factors[0:1])
print(type(factors[1]))
print(type(factors[0:1]))

# nested lists

nested = [[2, [37]], 4, ['hello']]
print(nested)
print(nested[0])
print(nested[1])
print(nested[2][0][3])
print(nested[0][1:2])

# Unlike strings, lists can be updated in place i.e. In Python, lists are mutable unlike strings

nested[1] = 7
print(nested)
nested[0][1][0] = 19
print(nested)

# Does assignment copy the value or make both the names point to the same value?

# For immutable values, we can assume that assignment makes a fresh copy of a value. Updating one value does not affect the copy. Values of type int, float, bool, str are immutabe.

x = 5
y = x
x = 7
print(y)

# For mutable values, assignment does not make a fresh copy. It rather makes both the names point to the same value. So with either name if we happen to update the mutable value the other name is also affected. 'list1' and 'list2' in the below example are the two names for the same list.

list1 = [1, 3, 5, 7]
list2 = list1
list1[2] = 4
print(list2)

# How can we make a copy of a list?

# A slice creates a new (sub)list from an old one. The outcome of a slice operation is a new list. We know that l[:k] is l[0:k], l[k:] is l[k:len(l)] Omitting both end points gives us a full slice l[:] = l[0:len(l)]

list2 = list1[:]
list1[0] = 2
print(list1)
print(list2)

# Digression on equality

list1 = [1, 3, 5, 7]
list2 = [1, 3, 5, 7]
list3 = list2

# All three lists are equal, but there is a difference in the way they are equal

# list1 and list2 are two different lists but they have the same value. So if we operate on one it need not preserve this equality anymore.

# list2 and list3 and equal because they precisely point to the same value. list2 and list3 are two names for the same list. Now, if we update list3 or list2 they continue to remain equal.

# x == y checks if x annd y have same value

# x is y checks if x and y refer to the same object

# We can use '==' and 'is' to check whether two names are equal to only in value or physically pointing to the same object

print(list1 == list2)
print(list2 == list3)
print(list2 is list3)
print(list1 is list2)

list2[2] = 4
print(list2)
print(list1 == list2)
print(list2 == list3)

# Concatenation

# Like strings, lists can be glued together using +

list1 = [1, 3, 5, 7]
list2 = [4, 5, 6, 8]
list3 = list1 + list2
print(list3)

# Note that + always produces a new list

list1 = [1, 3, 5, 7]
list2 = list1
list1 = list1 + [9]  # list1 and list2 no longer point to the same object
print(list1 is list2)
print(list1)
