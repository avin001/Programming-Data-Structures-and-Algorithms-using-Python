'''
Interacting with the user

Program needs to interact with the user
Receive input
Display output

Standard input and output
Input from keyboard
Output to screen

Reading from the keyboard

Read a line of input and assign to userdata
userdata = input()

Display a message prompting the user
userdata = input("Enter a number")

Add space, newline to make message readable
userdata = input("Enter a number: ")
userdata = input("Enter a number:\n")

Input is always a string, convert as required
userdata = input("Enter a number")
usernum = int(userdata)
or
usernum = int(input("Enter a number: "))

Use exception handling to deal with errors

while(True):
    try:
        userdata = int(input("Enter a number: "))
    except ValueError:
        print("Not a number. Try again.")
    else:
        break


Printing to screen

Print values of names, separated by spaces
print(x, y)
print(a, b, c)

Print a message
print("Not a number. Try again.")

Intersperse message with values of names
print("Values are x:", x, "y:", y)


Fine tuning print()

By default, print() appends new line character '\n' to whatever is printed
Each print() appears on a new line
Specify what to append with argument end="..."

print("Continue on the", end=" ")
print("same line", end=".\n")
print("Next line.")

Output:
Continue on the same line.
Next line.

Items are separated by space by default
(x, y) = (7, 10)
print("x is", x, "and y is", y, ".")

Output:
x is 7 and y is 10 .

Specify separator with argument sep="..."
print("x is ", x, " and y is ", y, ".", sep="")

Output:
x is 7 and y is 10.


Formatting print

May need more control over printing
specify width to align text
Align text withtin width - left, right, center
How many digits before/after decimal point?

'''
