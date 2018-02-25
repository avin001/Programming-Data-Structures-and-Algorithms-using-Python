'''A string with parentheses is well bracketed if all parentheses are matched: every opening bracket has a matching closing bracket and vice versa.

Write a Python function wellbracketed(s) that takes a string s containing parentheses and returns True if s is well bracketed and False otherwise.'''


def wellbracketed(s):
    nd = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            nd = nd + 1
        elif s[i] == ')':
            nd = nd - 1
    return nd == 0


print(wellbracketed("22)"))
print(wellbracketed("(a+b)(a-b)"))
print(wellbracketed("(a(b+c)-d)((e+f)"))
