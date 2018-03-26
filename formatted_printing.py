'''
String format() method


By exmaple

>>> "First: {0}, second: {1}".format(47, 11)
'First: 47, second: 11'

>>> "Second: {1}, first: {0}".format(47, 11)
'Second: 11, first: 47'

Replace arguments by position in message string

Can also replace arguments by name

>>> "One: {f}, two: {s}".format(f = 47, s = 11)
'One: 47, two: 11'

>>> "One: {f}, two: {s}".format(s = 11, f = 47)
'One: 47, two: 11'


Now, real formatting

>>> "Value: {0:3d}".format(4)
'Value:   4'

3d desribes how to display the value 4
d is a code specifies that 4 should be treated as an integer value
3 is the width of the area to show 4


>>> "Value: {0:6.2f}".format(47.523)
'Value:  47.52'

6.2f describes how to display the value 47.523
f is a code specifies that 47 should be treated as a floating point value
6 - width of the area to show 47.523
2 - number of digits to show after decimal point

Codes for other types of values
String, octal number, hexadecimal ...

'''

s = "First: {0}, second: {1}".format(47, 11)
print(s)

t = "Second: {1}, first: {0}".format(47, 11)
print(t)

u = "One: {f}, two: {s}".format(f = 47, s = 11)
print(u)

v = "One: {f}, two: {s}".format(s = 11, f = 47)
print(v)

val = "Value: {0:3d}".format(4)
print(val)

val = "Value: {0:6.2f}".format(47.523)
print(val)
