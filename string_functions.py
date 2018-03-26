'''
String processing

Easy to read ad write text files
String processing functions make it easy to analyse and transform contents

Strip whitespace

s.rstrip() removes trailing whitespace

for line in contents:
    s = line.rstrip()

s.lstrip() removes leading whitespace
s.strip() removes leading and trailing whitespace


Searching for text

s.find(pattern)

Returns first position in s where pattern occurs, -1 if no occurrence of pattern

s.find(pattern, start, end)

Search for pattern in slice s[start:end]

Another version of the is index as provided below:

s.index(pattern)
s.index(pattern, l, r)

Like find, but raise ValueError if pattern not found


Search and replace

s.replace(fromstr, tostr)

Returns copy of s with each occurrence of fromstr replaced by tostr

s.replace(fromstr, tostr, n)

Replace at most first n copies

Note that s itself is unchanged - strings are immutable


Splitting a string

Export spreadsheet as "comma separated value" text file
Want to extract columns from a line of text
Split the line into chunks between commas

columns = s.split(",")

Can split using any separator string
Split into at most n chucks

columns = s.split(" : ", n)


Joining strings

Recombine a list of strings using a separator

columns = s.split(",")
joinstring = ","
csvline = joinstring.join(columns)

date = "26"
month = "03"
year = "2018"
today = "-".join([date, month, year])


Converting case

Convert lower case to upper case, ...
s.capitalize() - return new string with first letter uppercase, rest lower
s.lower() - convert all uppercase to lowercase
s.upper() - convert all lowercase to uppercase
s.title(), s.swapcase(), ...


Resizing strings

s.center(n)

Returns string of length n with s centered, rest blank

s.center(n, "*")

Fill the rest with * instead of blanks

s.ljust(n), s.ljust(n, "*"), s.rjust(n), s.rjust(n, "*")

Similar, but left/right justify s in returned string


Other functions

Check the nature of characters in a string

s.isalpha(), s.isnumeric(), ...

Many other functions
Check the Python documentation

'''

s = "       Hello Avin!          "
print(s)
print(s.rstrip())
print(s)    # strings are immutable, rstrip(), lstrip(), strip() return new string

print(s.lstrip())
print(s.strip())

print("*********")

s = "brown fox grey dog brown fox"
print(s.find("brown"))
print(s.find("brown", 5, len(s)))
print(s.find("cat"))
try:
    print(s.index("cat"))
except ValueError:
    print("Can't find the pattern in the given string.")

print(s.replace("brown", "black"))
print(s.replace("brown", "black", 1))
t = "ababa"
print(t.replace("aba", "DD"))

print("*********")

csvline = "6,7,8"
print(csvline.split(","))
print(csvline.split(",", 1))
csvline = "6#?7#?8"
print(csvline.split("#?"))

print("*********")

date = "26"
month = "03"
year = "2018"
today = "-".join([date, month, year])
print(today)

print("*********")

s = "brown fox grey dog brown fox"
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())
t = "pYTHON"
print(t.swapcase())

print("*********")

s = "hello"
print(s.center(50))
print(s.center(50, "-"))
print(s.ljust(50, "-"))
print(s.rjust(50, "-"))

print("*********")

s = "try01"
print(s.isalpha())
print(s.isnumeric())
s = "try"
print(s.isalpha())
s = "123"
print(s.isnumeric())
