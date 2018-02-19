msg = 'Hello World!'
print(type(msg))
letter = 'A'  # In Python, a single character is a string of length 1; No separate type char
print(type(letter))

city = 'Chennai'
print(city)
title = "Hitchhiker's guide to the Galaxy"  # One reason to use double quotes is that if you need to use single quote as part of the string. Another way to do it is to use a backslash and a quote in the middle of a string.
print(title)

title_same = 'Hitchhiker\'s guide to the Galaxy'
print(title_same)

quote = '"Every day is a new day." - \'Earnest Hemmingway\''
print(quote)
# A single quote can include double quotes and a double quote can include single quotes without any confusion. What if you wanted to include both double quotes and single quotes in a string. Python allows that with the use of triple quotes.

dialogue = '''He said his favourite book is "Hitchhiker's Guide to the Galaxy"'''
print(dialogue)

newline = "first line\nsecond line\nthird line"
print(newline)

s = 'hello'
print(len(s))
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print('*****')
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])

t = s + ', there'
print(t)
print(s[1:4])  # slice of a string
print(s[:2])
print(s[1:])
print(s[3:1])  # slicing an invalid range returns an empty string
print(s[0:7])  # doesn't give error though 7 is out of range, but prints the string till the end.
# s[3] = 'p' gives an error: TypeError: 'str' object does not support item assignment. In Python, we cannot update a string "in place" i.e. we cannot change parts of a string as it stands. In Python, strings are immutable. Instead, we can use slicing and concatenation to modify strings.
s = s[:3] + 'p!'
print(s)
