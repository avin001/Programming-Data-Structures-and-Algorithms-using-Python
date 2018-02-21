# Lists are mutable. Both names list1 and list2 point to the same object. Any change by either list1 or list2 affects both the lists which are pointing to the same object.

list1 = [1, 3, 5, 6]
list2 = list1
list1[2] = 7
print(list1)
print(list2)

# Concatenation produces a new list. If we start reassigning a list using plus, we get a new list. This also applies whenwe do it inside a function. If inside a function, we want to update a list, then so long as we do not reassign it we are OK, but if we put a reassignment using plus then the list that has been updated inside the function will not reflect outside the function.

list1 = [1, 3, 5, 6]
list2 = list1
list1 = list1[:2] + [7] + list1[3:]
print(list1)
print(list2)

# Extending a list
# Adding an element to a list, in place

# Suppose we want to stick a new value at the end of a list; one way to do this is as below:

list1 = [1, 3, 5, 6]
list1 = list1 + [22]
print(list1)

# But as we saw, this plus operator will create a new list, so if you wanted to append a value to a list and maintain the same list so that for instance if it is inside a function we do not lose the connection between the argument and the value being manipulated inside the function, this would not do. We use the function append(v) for this. So, append is a function which extends a list with a new value without changing it. list1.append(v) - extends list1 by a single value v.

list1 = [1, 3, 5, 6]
list2 = list1
list1.append(22)
print(list1)
print(list2)

# Now, what if we wanted to append not a single value but a list of values; we actually take a list and expand it by adding a list at the end.
# lis1.extend(list2) - extends list1 by a list of values.
# In place equivalet of list1 = list1 + list2

list1 = [3, 6, 9]
list2 = [12, 15, 18]
list1.extend(list2)
print(list1)

# There is also away to remove an element from a list
# list1.remove(x) - removes first occurrence of x. Error if no copy of x exists in list1.

list1 = [1, 2, 3, 4, 5]
list2 = list1 + list1
print(list2)
list2.remove(5)
print(list2)

list3 = list(range(10))
list3.append(12)
print(list3)
list3.append([13, 14, 15])
print(list3)
list3.remove([13, 14, 15])
print(list3)
list3.extend([13, 14])
print(list3)

# Further list manipulation
# Can also assign to a slice in place.

list1 = [1, 3, 5, 6]
list2 = list1
list1[2:] = [7, 8]
print(list1)
print(list2)

# Can expand/shrink slices.

list1 = [1, 3, 5, 6]
list1[2:] = [9, 10, 11]
print(list1)
list1[:2] = [7]
print(list1)

# List membership

# x in l return True if value x is found in list l

# Safely remove x from l

l = [1, 2, 3, 4, 5]
x = 7

if x in l:
    l.remove(x)
print(l)

x = 5
if x in l:
    l.remove(x)
print(l)

# Remove all occurrences of x from l

list1 = [1, 2, 3, 4, 5]
list1 = list1 + list1
print(list1)

x = 5
while x in list1 :
    list1.remove(x)
print(list1)

# Other functions

# l.reverse() - reverse l in place
# l.sort() - sort l in ascending order
# l.index(x) - find leftmost position of x in l. Avoid error by checking if x in l
# l.rindex(x) - find rightmost position of x in l

list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)
list1.sort()
print(list1)

x = 2
if x in list1:
    print(list1.index(x))
