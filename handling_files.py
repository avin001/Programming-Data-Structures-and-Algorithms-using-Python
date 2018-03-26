'''
Dealing with files

Standard input and output is not convenient for large volumes of data
Instead, read and write files on the disk
Disk read/write is much slower than memory

Disk buffers

Disk data is read/written in large blocks
"Buffer" is a temporary parking place for disk data


    _____________                         ____________
    |           |                         |          |
    |           |     ______________      |          |
    |   memory  |<--->|   Buffer   |<---->|   disk   |
    |           |     |____________|      |          |
    |___________|                         |__________|


Reading/writing disk data

Open a file - create file handle to file on disk
Like setting up a buffer for the file

Read and write operations are to file handle

Close a file
Write out buffer to disk(flush)
Disconnect file handle

Opening a file

fh = open("gcd.py", "r")

First argument to open is file name
Can give a full path

Second argument is mode for opening file
Read, "r": opens a file for reading only
Write, "w": creates an empty file to write to
Append, "a": append to an existing file

Read through file handle

contents = fh.read()
Reads entire file into name as a single string

contents = fh.readline()
Reads one line into name - lines end with '\n'
String includes the '\n', unlike input()

contents = fh.readlines()
Reads entire file as list of strings
Each string is one line, ending with '\n'


Reading files


    ______________________________________________
    |                 File                       |
    |____________________________________________|
    |_______________|_______________________|
    |  readline()   |    readline()         |
    |
  open()



Reading is a sequential operation
When file is opened, point to position 0, the start
Each successive readline() moves forward
fh.seek(n) - moves pointer to position n
block = fh.read(12) - read a fixed number of characters


End of File

When reading incrementally, important to know when file has ended
The following both signal end of file
fh.read() returns empty string ""
fh.readline() returns empty string ""


Writing to a file

fh.write(s)
Write string s to file
Returns number of characters written
Include '\n' explicitly to go to a new line
fh.writelines(l)
Write a list of lines l to file
Must include '\n' explicitly for each string


Closing a file

fh.close()
Flushes output buffer and decouples file handle
All pending writes copied to disk

fh.flush()
Manually forces write to disk


Processing file line by line

contents = fh.readlines()
for l in contents:
    ...

Even better
for l in fh.readlines():
    ...

Copying a file

infile = open("input.txt", "r")
outfile = open("output.txt", "w")
for line in infile.readlines():
    outfile.write(line)
infile.close()
outfile.close()

Alternate way

infile = open("input.txt", "r")
outfile = open("output.txt", "w")
contents = infile.readlines()
outfile.writelines(content)
infile.close()
outfile.close()


Strip new line character

Get rid of trailing '\n'

contents = fh.readlines()
for line in contents:
    s = line[:-1]

Instead, use rstrip() to remove trailing whitespace

for line in contents:
    s = line.rstrip()

Also, strip() - both sides, lstrip() - from left

'''

fh = open("input.txt", "r")
for line in fh.readlines():
    print(line, end="")

print()
print(fh.read())
print(fh.read() == '')  # reached the end of the file

fh.close()

print("***********")

try:
    contents = fh.readlines()
except ValueError:
    fh = open("input.txt", "r")
    for line in fh.readlines():
        print(line, end="")
else:
    pass

fh.close()


fh = open("input.txt", "r")
gh = open("output.txt", "w")
for line in fh.readlines():
    gh.write(line)
fh.close()
gh.close()

fh = open("input.txt", "r")
gh = open("output.txt", "a")
for line in fh.readlines():
    gh.write(line)
fh.close()
gh.close()


