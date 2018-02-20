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
