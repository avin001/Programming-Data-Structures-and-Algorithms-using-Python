# Tuples

# Simultaneous assignments

(age, name, primes) = (23, "Kamal", [2, 3, 5])
print(name, age, primes)

# Can assign a "tuple" of values to a name

point = (3.5, 4.8)
date = (16, 7, 2017)

# Extract positions, slices

xcoordinate = point[0]
monthyear = date[1:]
print(xcoordinate, monthyear)

# Tuples are immutable
# date[1] = 8 is an error

# Generalizing lists

l = [13, 46, 0, 25, 72]

# View l as a function, associating values to positions
# l : {0, 1, ..., 4} -> integers
# l(0) = 13, l(4) = 72, ... where we are looking at list as a function value
# 0, 1, 2, 3, 4 are keys
# l[0], l[1], ..., l[4] are corresponding values

# Dictionaries

# Allows keys other than range(0, n)
# Key could be a string

# test1["Dhawan"] = 84
# test1["Pujara"] = 16
# test1["Kohli"] = 200

# Python dictionary
# Any immutable value can be a key
# Can update dictionaries in place - mutable, like lists
# Empty dictionary is {}, not []
# Intialization: test1 = {}
# Note: test1 = [] is empty list, test1 = () is empty tuple
# Keys can be any immutable value - int, float, bool, string, tuple
# But not lists, or dictionaries
# Can nest dictionaries
# score["Test1"]["Dhawan"] = 84
# score["Test2"]["Kohli"] = 200
# score["Test2"]["Dhawan"] = 27

# Directly assign values to a dictionary

# score = {"Dhawan": 84, "Kohli": 200}
# score = {"Test1": {"Dhawan": 84, "Kohli": 200}, "Test2": {"Dhawan": 50}}

score = {}
print(score)
score["Test1"] = {}
score["Test2"] = {}
print(score)
score["Test1"]["Dhawan"] = 76
score["Test2"]["Dhawan"] = 27
score["Test1"]["Kohli"] = 200

print(score)

# Operating on dectionaries

# d.keys() returns sequence of keys of dictionary d
# for k in d.keys():
#   Process d[k]
# d.keys is not in any predictable order
# for k in sorted(d.keys()):
#   Process d[k]
# sorted(l) returns sorted copy of l, l.sort() sorts l in place
# d.keys() is not a list - use list(d.keys())

d = {}
for l in "abcdefghi":
    d[l] = l

print(d)
print(d["a"])
print(d["i"])
print(d.keys())
print(d.values())

# From Python 3.6 onwards dictionaries maintain insertion order by default. However, preserving the order is not "guaranteed" yet (it probably will be in 3.7):

# Similarly, d.values() is sequence of values in d

# total= 0
# for s in test1.values():
#   total = total + s

# Test for key using in, like list membership

# for n in ["Dhawan", "Kohli"]:
#   total[n] = 0
#   for match in score.keys():
#       if n in score[match].keys():
#           total[n] = total[n] + score[match][n]

# Dictionaries vs lists

# d = {}
# d[0] = 7  No problem, d == {0: 7}

# unlike a list
# l = []
# l[0] = 7  # IndexError!
